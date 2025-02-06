use arrow::datatypes::ArrowPrimitiveType;

use crate::georaster::{ArrowRaster, ArrowRasterNum};

/// Macro to generate numeric raster operations.
macro_rules! arrow_raster_op {
    (   $op_trait:path, // name of the trait e.g. std::ops::Add
        $op_assign_trait:path, // name of the trait with assignment e.g. std::ops::AddAssign
        $op_assign_ref_trait:path, // name of the trait with reference assignment e.g. std::ops::AddAssign<&ArrowRaster<T>>
        $op_fn:ident, // name of the operation function inside the trait e.g. add
        $op_assign_fn:ident, // name of the assignment function inside the trait e.g. add_assign
        $op_nodata_fn:ident, // name of the operation function with nodata handling e.g. add_nodata_aware
        $op_assign_nodata_fn:ident // name of the assignment function with nodata handling e.g. add_assign_nodata_aware
    ) => {
        impl<T> $op_trait for ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            type Output = ArrowRaster<T>;

            fn $op_fn(self, other: ArrowRaster<T>) -> ArrowRaster<T> {
                self.binary_mut(&other, |x, y| x.$op_nodata_fn(y))
            }
        }

        impl<T> $op_trait for &ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            type Output = ArrowRaster<T>;

            fn $op_fn(self, other: &ArrowRaster<T>) -> ArrowRaster<T> {
                self.binary(other, |x, y| x.$op_nodata_fn(y))
            }
        }

        impl<T> $op_assign_trait for ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            fn $op_assign_fn(&mut self, other: ArrowRaster<T>) {
                self.binary_inplace(&other, |x, y| {
                    x.$op_assign_nodata_fn(y);
                });
            }
        }

        impl<T> $op_assign_ref_trait for ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            fn $op_assign_fn(&mut self, other: &ArrowRaster<T>) {
                self.binary_inplace(&other, |x, y| {
                    x.$op_assign_nodata_fn(y);
                });
            }
        }
    };
}

/// Macro to generate numeric raster operations.
macro_rules! arrow_raster_op_scalar {
    (   $scalar_op_trait:path, // name of the trait with scalar argument e.g. std::ops::Add<T>
        $op_assign_scalar_trait:path, // name of the trait with scalar assignment e.g. std::ops::AddAssign<T>
        $op_fn:ident, // name of the operation function inside the trait e.g. add
        $op_assign_fn:ident, // name of the assignment function inside the trait e.g. add_assign
        $op_nodata_fn:ident, // name of the operation function with nodata handling e.g. add_nodata_aware
        $op_assign_nodata_fn:ident // name of the assignment function with nodata handling e.g. add_assign_nodata_aware
    ) => {
        impl<T> $op_assign_scalar_trait for ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            fn $op_assign_fn(&mut self, scalar: T) {
                self.unary_inplace(|x| {
                    x.$op_assign_nodata_fn(scalar);
                });
            }
        }

        impl<T> $scalar_op_trait for ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            type Output = ArrowRaster<T>;

            fn $op_fn(self, scalar: T) -> ArrowRaster<T> {
                self.unary_mut(|x| x.$op_nodata_fn(scalar))
            }
        }

        impl<T> $scalar_op_trait for &ArrowRaster<T>
        where
            T: ArrowRasterNum<T>,
            T::TArrow: ArrowPrimitiveType<Native = T>,
        {
            type Output = ArrowRaster<T>;

            fn $op_fn(self, scalar: T) -> ArrowRaster<T> {
                self.unary(|x| x.$op_nodata_fn(scalar))
            }
        }
    };
}

arrow_raster_op!(
    std::ops::Add,
    std::ops::AddAssign,
    std::ops::AddAssign<&ArrowRaster<T>>,
    add,
    add_assign,
    add_nodata_aware,
    add_assign_nodata_aware
);

arrow_raster_op!(
    raster::ops::AddInclusive,
    raster::ops::AddAssignInclusive,
    raster::ops::AddAssignInclusive<&ArrowRaster<T>>,
    add_inclusive,
    add_assign_inclusive,
    add_inclusive_nodata_aware,
    add_assign_inclusive_nodata_aware
);

arrow_raster_op_scalar!(
    std::ops::Add<T>,
    std::ops::AddAssign<T>,
    add,
    add_assign,
    add_nodata_aware,
    add_assign_nodata_aware
);

arrow_raster_op!(
    std::ops::Sub,
    std::ops::SubAssign,
    std::ops::SubAssign<&ArrowRaster<T>>,
    sub,
    sub_assign,
    sub_nodata_aware,
    sub_assign_nodata_aware
);

arrow_raster_op!(
    raster::ops::SubInclusive,
    raster::ops::SubAssignInclusive,
    raster::ops::SubAssignInclusive<&ArrowRaster<T>>,
    sub_inclusive,
    sub_assign_inclusive,
    sub_inclusive_nodata_aware,
    sub_assign_inclusive_nodata_aware
);

arrow_raster_op_scalar!(
    std::ops::Sub<T>,
    std::ops::SubAssign<T>,
    sub,
    sub_assign,
    sub_nodata_aware,
    sub_assign_nodata_aware
);

arrow_raster_op!(
    std::ops::Mul,
    std::ops::MulAssign,
    std::ops::MulAssign<&ArrowRaster<T>>,
    mul,
    mul_assign,
    mul_nodata_aware,
    mul_assign_nodata_aware
);

arrow_raster_op_scalar!(
    std::ops::Mul<T>,
    std::ops::MulAssign<T>,
    mul,
    mul_assign,
    mul_nodata_aware,
    mul_assign_nodata_aware
);

arrow_raster_op!(
    std::ops::Div,
    std::ops::DivAssign,
    std::ops::DivAssign<&ArrowRaster<T>>,
    div,
    div_assign,
    div_nodata_aware,
    div_assign_nodata_aware
);

arrow_raster_op_scalar!(
    std::ops::Div<T>,
    std::ops::DivAssign<T>,
    div,
    div_assign,
    div_nodata_aware,
    div_assign_nodata_aware
);
