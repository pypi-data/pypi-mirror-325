---
title: "SHGrid class"
keywords: spherical harmonics software package, spherical harmonic transform, legendre functions, multitaper spectral analysis, fortran, Python, gravity, magnetic field
sidebar: mydoc_sidebar
permalink: python-shgrid.html
summary: Classes for global gridded data.
toc: true
folder: mydoc
---

<style>
table:nth-of-type(n) {
    display:table;
    width:100%;
}
table:nth-of-type(n) th:nth-of-type(2) {
    width:70%;
}
</style>

## Subclasses

| Subclass name | Description |
| ------------- | ----------- |
| DHRealGrid | Class for real *Driscoll and Healy* (1994) sampled grids.|
| DHComplexGrid | Class for complex *Driscoll and Healy* (1994) sampled grids. |
| GLQRealGrid | Class for real Gauss-Legendre quadrature sampled grids.| 
| GLQComplexGrid | Class for complex Gauss-Legendre quadrature sampled grids.|

## Initialization

| Initialization method | Description |
| --------------------- | ----------- |
| `x = SHGrid.from_array()` | Initialize using an array. |
| `x = SHGrid.from_xarray()` | Initialize using an xarray DataArray. |
| `x = SHGrid.from_netcdf()` | Initialize using a netcdf file or object. |
| `x = SHGrid.from_file()` | Initialize using an array from a file. |
| `x = SHGrid.from_zeros()` | Initialize using an array of zeros. |
| `x = SHGrid.from_cap()` | Initialize using a rotated spherical cap. |
| `x = SHGrid.from_ellipsoid()` | Initialize using a triaxial ellipsoid. |


## Class attributes

| Attribute | Description |
| --------- | ----------- |
| `data` | Array of the gridded data. |
| `nlat`, `nlon` | The number of latitude and longitude bands in the grid. |
| `n` | The number of samples in latitude for `'DH'` grids. |
| `lmax` | The maximum spherical harmonic degree that can be resolved by the grid sampling. |
| `sampling` | The longitudinal sampling for Driscoll and Healy grids. Either 1 for equally sampled grids (`nlon` = `nlat`) or 2 for equally spaced grids in degrees. |
| `kind` | Either `'complex'` or `'real'` for the data type. |
| `grid` | Either `'DH'` or `'GLQ'` for Driscoll and Healy grids or Gauss-Legendre quadrature grids. |
| `units` | The units of the gridded data. |
| `zeros` | The $$\cos(\theta)$$ nodes used with Gauss-Legendre quadrature grids. Default is `None`. |
| `weights` | The latitudinal weights used with Gauss-Legendre quadrature grids. Default is `None`. |
| `extend` | True if the grid contains the redundant column for 360 E and (for `'DH'` grids) the unnecessary row for 90 S. |

## Class methods

| Method | Description |
| ------ | ----------- |
| `to_array()` | Return a numpy array of the gridded data. |
| `to_xarray()` | Return the gridded data as an xarray DataArray. |
| `to_netcdf()` | Return the gridded data as a netcdf formatted file or object. |
| `to_file()` | Save raw gridded data to a text or binary file. |
| `to_real()` | Return a new SHGrid class instance of the real component of the data. |
| `to_imag()` | Return a new SHGrid class instance of the imaginary component of the data. |
| `lats()` | Return a vector containing the latitudes of each row of the gridded data. |
| `lons()` | Return a vector containing the longitudes of each column of the gridded data. |
| `histogram()` | Return an area-weighted histogram of the gridded data. |
| `expand()` | Expand the grid into spherical harmonics. |
| `min()` | Return the minimum value of data. |
| `max()` | Return the maximum value of data. |
| `copy()` | Return a copy of the class instance. |
| `plot()` | Plot the data. |
| `plotgmt()` | Plot projected data using the generic mapping tools (GMT). |
| `plot3d()` | Plot a 3-dimensional representation of the data. |
| `info()` | Print a summary of the data stored in the SHGrid instance. |
