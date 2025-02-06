use arrow::{
    array::{Array, ArrowNativeTypeOp, PrimitiveArray, PrimitiveBuilder, PrimitiveIter},
    buffer::ScalarBuffer,
    datatypes::ArrowPrimitiveType,
};

use num::NumCast;
use raster::{Cell, Raster, RasterNum};

use crate::{
    georaster::{GeoRaster, GeoRasterCreation},
    GeoReference,
};

use super::arrowutil::ArrowType;

pub trait ArrowRasterNum<T: num::ToPrimitive>: RasterNum<T> + ArrowType + ArrowNativeTypeOp + ToString {}

impl ArrowRasterNum<i8> for i8 {}
impl ArrowRasterNum<u8> for u8 {}
impl ArrowRasterNum<i16> for i16 {}
impl ArrowRasterNum<u16> for u16 {}
impl ArrowRasterNum<i32> for i32 {}
impl ArrowRasterNum<u32> for u32 {}
impl ArrowRasterNum<i64> for i64 {}
impl ArrowRasterNum<u64> for u64 {}
impl ArrowRasterNum<f32> for f32 {}
impl ArrowRasterNum<f64> for f64 {}

/// Perform a deep copy of the array, not just the underlying ARC buffer
fn primitive_array_copy<T: ArrowRasterNum<T>>(array: &PrimitiveArray<T::TArrow>) -> PrimitiveArray<T::TArrow> {
    let mut builder = PrimitiveBuilder::<T::TArrow>::new();
    array.iter().for_each(|x| builder.append_option(x));
    builder.finish()
}

pub struct ArrowRaster<T: ArrowRasterNum<T>> {
    pub(super) metadata: GeoReference,
    pub(super) data: PrimitiveArray<T::TArrow>,
}

impl<T: ArrowRasterNum<T>> Clone for ArrowRaster<T> {
    fn clone(&self) -> Self {
        ArrowRaster {
            metadata: self.metadata.clone(),
            data: self.data.clone(),
        }
    }
}

impl<T: ArrowRasterNum<T>> Default for ArrowRaster<T> {
    fn default() -> Self {
        ArrowRaster {
            metadata: GeoReference::default(),
            data: PrimitiveArray::<T::TArrow>::new_null(0),
        }
    }
}

impl<T: ArrowRasterNum<T>> GeoRaster<T> for ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    fn geo_reference(&self) -> &GeoReference {
        &self.metadata
    }
}

impl<T: ArrowRasterNum<T>> GeoRasterCreation<T> for ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    fn new(metadata: GeoReference, data: Vec<T>) -> Self {
        let nod = metadata.nodata();
        let data: PrimitiveArray<T::TArrow> = data.iter().map(|&v| (v.to_f64() != nod).then_some(v)).collect();
        ArrowRaster { metadata, data }
    }

    fn from_iter<Iter>(metadata: GeoReference, iter: Iter) -> Self
    where
        Self: Sized,
        Iter: Iterator<Item = Option<T>>,
    {
        ArrowRaster {
            metadata,
            data: iter.collect(),
        }
    }

    fn zeros(meta: GeoReference) -> Self {
        ArrowRaster::filled_with(T::zero(), meta)
    }

    fn filled_with(val: T, meta: GeoReference) -> Self {
        let data_size = meta.rows() * meta.columns();
        ArrowRaster::new(meta, vec![val; data_size])
    }

    fn filled_with_nodata(metadata: GeoReference) -> Self {
        let mut builder = PrimitiveBuilder::<T::TArrow>::new();
        builder.append_nulls(metadata.rows() * metadata.columns());

        ArrowRaster {
            metadata,
            data: builder.finish(),
        }
    }
}

impl<T: ArrowRasterNum<T>> ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    pub fn mask_vec(&self) -> Vec<Option<T>> {
        self.data.iter().collect()
    }

    /// make sure the null entries in the raster contain the nodata value
    /// Call this function before writing the raster to disk
    pub fn flatten_nodata(&mut self) {
        if self.data.null_count() == 0 {
            return;
        }

        if let Some(nodata) = self.metadata.nodata() {
            let nodata = NumCast::from(nodata).unwrap_or(T::nodata_value());
            self.metadata.set_nodata(nodata.to_f64());

            if let (_dt, data, Some(mask)) = self.data.clone().into_parts() {
                let mut vec_data = data.to_vec();
                (0..data.len()).for_each(|i| {
                    if mask.is_null(i) {
                        vec_data[i] = nodata;
                    }
                });

                self.data = PrimitiveArray::<T::TArrow>::new(ScalarBuffer::from(vec_data), Some(mask));
            }
        }
    }

    pub fn arrow_array(&self) -> &PrimitiveArray<T::TArrow> {
        &self.data
    }

    pub fn unary<F: Fn(T) -> T>(&self, op: F) -> Self {
        ArrowRaster {
            metadata: self.metadata.clone(),
            data: self.data.unary(op),
        }
    }

    pub fn unary_inplace<F: Fn(&mut T)>(&mut self, op: F) {
        let mut temp_array = PrimitiveBuilder::<T::TArrow>::new().finish();
        std::mem::swap(&mut self.data, &mut temp_array);

        let unary_result = temp_array.unary_mut(|mut x| {
            op(&mut x);
            x
        });

        temp_array = match unary_result {
            Ok(data) => data,
            Err(data) => {
                // The operation failed because the underlying data is shared
                // Perform a deep copy of the array and try again
                primitive_array_copy::<T>(&data)
                    .unary_mut(|mut x| {
                        op(&mut x);
                        x
                    })
                    .expect("Our deep copy should not be shared!")
            }
        };

        std::mem::swap(&mut self.data, &mut temp_array);
    }

    pub fn unary_mut<F: Fn(T) -> T>(mut self, op: F) -> Self {
        match self.data.unary_mut(op) {
            Ok(data) => {
                self.data = data;
                self
            }
            Err(e) => panic!("Error on raster operation: {:?}", e),
        }
    }

    pub fn binary<F: Fn(T, T) -> T>(&self, other: &Self, op: F) -> Self {
        raster::algo::assert_dimensions(self, other);

        let data = match arrow::compute::binary(&self.data, &other.data, op) {
            Ok(data) => data,
            Err(e) => panic!("Error on raster operation: {:?}", e),
        };

        ArrowRaster {
            metadata: self.metadata.clone(),
            data,
        }
    }

    pub fn binary_inplace<F: Fn(&mut T, T)>(&mut self, other: &Self, op: F) {
        raster::algo::assert_dimensions(self, other);

        let mut temp_array = PrimitiveBuilder::<T::TArrow>::new().finish();
        std::mem::swap(&mut self.data, &mut temp_array);

        let binary_result = arrow::compute::binary_mut(temp_array, &other.data, |mut x, y| {
            op(&mut x, y);
            x
        });

        temp_array = match binary_result {
            Ok(data) => data.expect("Binary operations should be infallible"),
            Err(data) => {
                // The opartion failed because the underlying data is shared
                // Perform a deep copy of the array and try again
                arrow::compute::binary_mut(primitive_array_copy::<T>(&data), &other.data, |mut x, y| {
                    op(&mut x, y);
                    x
                })
                .expect("Our deep copy should not be shared!")
                .expect("Binary operations should be infallible")
            }
        };

        std::mem::swap(&mut self.data, &mut temp_array);
    }

    pub fn binary_mut<F: Fn(T, T) -> T>(mut self, other: &Self, op: F) -> Self {
        raster::algo::assert_dimensions(&self, other);

        let data = match arrow::compute::binary_mut(self.data, &other.data, &op) {
            Ok(data) => data.expect("Binary operations should be infallible"),
            Err(data) => {
                // The opartion failed because the underlying data is shared
                // Perform a deep copy of the array and try again
                arrow::compute::binary_mut(primitive_array_copy::<T>(&data), &other.data, op)
                    .expect("Our deep copy should not be shared!")
                    .expect("Binary operations should be infallible")
            }
        };

        self.data = data;
        self
    }
}

impl<T: ArrowRasterNum<T>> Raster for ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    type Pixel = T;
    type ReTyped<U: RasterNum<U> + ArrowPrimitiveType<Native = U>> = ArrowRaster<U>;

    fn width(&self) -> usize {
        self.metadata.columns()
    }

    fn height(&self) -> usize {
        self.metadata.rows()
    }

    fn as_mut_slice(&mut self) -> &mut [T] {
        //self.data.values().inner().as_mut_slice()
        unimplemented!();
    }

    fn as_slice(&self) -> &[T] {
        self.data.values().inner().typed_data()
    }

    fn nodata_value(&self) -> Option<T> {
        match self.metadata.nodata() {
            Some(nodata) => NumCast::from(nodata),
            None => None,
        }
    }

    fn nodata_count(&self) -> usize {
        self.data.null_count()
    }

    fn index_has_data(&self, index: usize) -> bool {
        self.data.is_valid(index)
    }

    fn masked_data(&self) -> Vec<Option<T>> {
        self.data.iter().collect()
    }

    fn value(&self, index: usize) -> Option<T> {
        if self.index_has_data(index) {
            Some(self.data.value(index))
        } else {
            None
        }
    }

    fn sum(&self) -> f64 {
        // using the sum from compute uses the same data type as the raster so is not accurate for e.g. f32
        self.data
            .iter()
            .filter_map(|x| x.and_then(|v| v.to_f64()))
            .fold(0.0, |acc, x| acc + x)
    }

    fn iter_opt(&self) -> impl Iterator<Item = Option<T>> {
        self.data.iter()
    }

    fn iter(&self) -> std::slice::Iter<T> {
        todo!()
    }

    fn iter_mut(&mut self) -> std::slice::IterMut<T> {
        todo!()
    }

    fn set_cell_value(&mut self, _cell: raster::Cell, _val: Option<T>) {
        todo!()
    }
}

impl<T: RasterNum<T>> std::ops::Index<Cell> for ArrowRaster<T> {
    type Output = T;

    fn index(&self, cell: Cell) -> &Self::Output {
        self.data
            .value(cell.row as usize * self.metadata.columns() + cell.col as usize)
    }
}

impl<T: RasterNum<T>> std::ops::IndexMut<Cell> for ArrowRaster<T> {
    fn index_mut(&mut self, cell: Cell) -> &mut Self::Output {
        unsafe {
            // SAFETY: The index is checked to be within bounds
            self.data
                .get_unchecked_mut(cell.row as usize * self.size.cols + cell.col as usize)
        }
    }
}

impl<'a, T: ArrowRasterNum<T>> IntoIterator for &'a ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    type Item = Option<T>;
    type IntoIter = PrimitiveIter<'a, T::TArrow>;

    fn into_iter(self) -> Self::IntoIter {
        self.data.into_iter()
    }
}

impl<T: ArrowRasterNum<T>> PartialEq for ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    fn eq(&self, other: &Self) -> bool {
        if self.metadata != other.metadata {
            return false;
        }

        self.data.iter().zip(other.data.iter()).all(|(a, b)| a == b)
    }
}

impl<T: ArrowRasterNum<T>> std::fmt::Debug for ArrowRaster<T>
where
    T::TArrow: ArrowPrimitiveType<Native = T>,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "ArrowRaster: {:?}", &self.metadata)?;
        let rows = self.metadata.rows();
        let cols = self.metadata.columns();
        if rows * cols < 100 {
            for row in self.as_slice().chunks(cols) {
                writeln!(
                    f,
                    "{}",
                    row.iter()
                        .map(|&val| val.to_string())
                        .collect::<Vec<String>>()
                        .join(", ")
                )?;
            }
        } else {
            write!(f, "Data too big for debug output")?;
        }

        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use raster::{Nodata, RasterSize};

    use super::*;
    use crate::georaster::{algo, testutils::*};

    #[test]
    fn cast_arrow_raster() {
        let ras = ArrowRaster::new(test_metadata_2x2(), vec![1, 2, <i32 as Nodata<i32>>::nodata_value(), 4]);

        let f64_ras = algo::cast::<f64, _, ArrowRaster<f64>, _>(&ras);
        compare_fp_vectors(
            f64_ras.as_slice(),
            &[1.0, 2.0, <f64 as Nodata<f64>>::nodata_value(), 4.0],
        );
    }

    #[test]
    fn clone_raster() {
        let ras = ArrowRaster::new(test_metadata_2x2(), vec![1, 2, <i32 as Nodata<i32>>::nodata_value(), 4]);
        let ras2 = ras.clone();

        assert_eq!(ras, ras2);
    }

    #[test]
    fn test_flatten() {
        let metadata = GeoReference::new(
            "EPSG:4326".to_string(),
            RasterSize { rows: 2, cols: 2 },
            [0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
            Some(-9999.0),
        );

        let data1 = vec![1, 2, -9999, 4];
        let data2 = vec![-9999, 6, 7, 8];
        let raster1 = ArrowRaster::new(metadata.clone(), data1);
        let raster2 = ArrowRaster::new(metadata.clone(), data2);

        let mut result = &raster1 + &raster2;
        // The first element should be nodata
        assert!(!result.index_has_data(0));
        assert!(!result.index_has_data(2));
        // The internal buffer value is undefined, due to the operation will no longer match the nodata value
        assert!(result.as_slice()[0] != -9999);
        assert!(result.as_slice()[2] != -9999);

        // Flatten the nodata values
        result.flatten_nodata();

        // The first element should still be nodata
        assert!(!result.index_has_data(0));
        assert!(!result.index_has_data(2));
        // The internal buffer value should now match the nodata value
        assert_eq!(result.as_slice()[0], -9999);
        assert_eq!(result.as_slice()[2], -9999);
    }
}
