use arrow::{
    array::{Array, ArrayData, PrimitiveArray},
    datatypes::ArrowPrimitiveType,
    pyarrow::PyArrowType,
};

use crate::{
    array::{Columns, Rows},
    ArrayNum,
};
use pyo3::{pyclass, pymethods};

use crate::{
    raster::{
        arrow::arrowutil::{self, ArrowType},
        DenseRaster,
    },
    GeoReference, RasterSize,
};

#[derive(Clone)]
#[pyclass(name = "RasterMetadata")]
pub struct PyRasterMetadata {
    // The raw projection string
    pub projection: String,
    // The EPSG code of the projection
    pub epsg: Option<u32>,
    /// The size of the image in pixels (width, height)
    pub size: (usize, usize),
    /// The cell size of the image (xsize, ysize)
    pub cell_size: (f64, f64),
    /// The affine transformation.
    pub geo_transform: [f64; 6],
    /// The nodata value.
    pub nodata: Option<f64>,
}

impl From<&GeoReference> for PyRasterMetadata {
    fn from(meta: &GeoReference) -> Self {
        PyRasterMetadata {
            projection: meta.projection().to_string(),
            epsg: meta.projected_epsg().map(|crs| crs.into()),
            size: (meta.columns().count() as usize, meta.rows().count() as usize),
            cell_size: (meta.cell_size().x(), meta.cell_size().y()),
            geo_transform: meta.geo_transform(),
            nodata: meta.nodata(),
        }
    }
}

impl From<&PyRasterMetadata> for GeoReference {
    fn from(val: &PyRasterMetadata) -> Self {
        GeoReference::new(
            val.projection.clone(),
            RasterSize {
                rows: Rows(val.size.1 as i32),
                cols: Columns(val.size.0 as i32),
            },
            val.geo_transform,
            val.nodata,
        )
    }
}

#[pymethods]
impl PyRasterMetadata {
    fn __repr__(&self) -> String {
        let mut str = format!(
            "Meta ({}x{}) cell size [x {} y {}]",
            self.size.0, self.size.1, self.cell_size.0, self.cell_size.1
        );
        if self.epsg.is_some() {
            str += &format!(" EPSG: {}\n", self.epsg.unwrap_or_default());
        }
        str
    }

    fn __str__(&self) -> String {
        self.__repr__()
    }
}

#[pyclass(name = "Raster")]
pub struct PyRaster {
    pub meta: PyRasterMetadata,
    pub data: ArrayData,
}

impl PyRaster {
    pub fn new<T: ArrayNum<T> + ArrowType + Send + Sync>(raster: DenseRaster<T>) -> Self
    where
        T::TArrow: ArrowPrimitiveType<Native = T>,
        arrow::array::PrimitiveArray<<T as arrowutil::ArrowType>::TArrow>: std::convert::From<std::vec::Vec<T>>,
    {
        let (meta, data) = raster.into_raw_parts();
        let arr = PrimitiveArray::<T::TArrow>::from(data);

        let array: &PrimitiveArray<T::TArrow> = arr.as_any().downcast_ref().expect("Failed to downcast arrow array");

        PyRaster {
            meta: PyRasterMetadata::from(&meta),
            data: array.into_data(),
        }
    }
}

#[pymethods]
impl PyRaster {
    #[getter]
    fn meta_data(&self) -> PyRasterMetadata {
        self.meta.clone()
    }

    #[getter]
    fn arrow_data(&self) -> PyArrowType<ArrayData> {
        let data = self.data.clone();
        PyArrowType(data)
    }

    fn __repr__(&self) -> String {
        format!("Raster ({}x{}) ({})", self.meta.size.0, self.meta.size.1, self.data.data_type())
    }

    fn __str__(&self) -> String {
        self.__repr__()
    }
}
