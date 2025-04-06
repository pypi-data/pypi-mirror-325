---
title: pysh.gravmag
keywords: spherical harmonics, gravity field, magnetic field, python, pyshtools
sidebar: mydoc_sidebar
permalink: python-gravity-magnetics.html
summary: This module provides routines for working with gravity and magnetic field data expressed in spherical harmonics.
toc: true
folder: mydoc
---

<style>
table:nth-of-type(n) {
    display:table;
    width:100%;
}
table:nth-of-type(n) th:nth-of-type(2) {
    width:75%;
}
</style>

## Gravity routines

| Function name | Description |
| ------------- | ----------- |
| [MakeGravGridDH](pymakegravgriddh.html) | Create 2D cylindrical maps on a flattened and rotating ellipsoid of all three components of the gravity field, the gravity disturbance, and the gravitational potential. |
| [MakeGravGridPoint](pymakegravgridpoint.html) | Determine the vector components of the gravitational acceleration at a single point. |
| [MakeGravGradGridDH](pymakegravgradgriddh.html) | Calculate the components of the gravity "gradient" tensor on a flattened ellipsoid. |
| [MakeGeoidGridDH](pymakegeoidgriddh.html) | Create a global map of the geoid. |
| [CilmPlusDH](pycilmplusdh.html) | Calculate the gravitational potential exterior to relief along a spherical interface using the finite-amplitude algorithm of *Wieczorek and Phillips* (1998) on a *Driscoll and Healy* (1994) grid. |
| [CilmMinusDH](pycilmminusdh.html) | Calculate the gravitational potential interior to relief along to a spherical interface using the finite-amplitude algorithm of *Wieczorek and Phillips* (1998) on a *Driscoll and Healy* (1994) grid. |
| [CilmPlusRhoHDH](pycilmplusrhohdh.html) | Calculate the gravitational potential exterior to relief along a spherical interface with laterally varying density using the finite amplitude algorithm of *Wieczorek* (2007) on a *Driscoll and Healy* (1994) grid. |
| [CilmMinusRhoHDH](pycilmminusrhohdh.html) | Calculate the gravitational potential interior to relief along a spherical interface with laterally varying density using the finite amplitude algorithm of *Wieczorek* (2007) on a *Driscoll and Healy* (1994) grid. |
| [BAtoHilmDH](pybatohilmdh.html) | Calculate iteratively the relief along an interface with constant density contrast that corresponds to a given Bouguer anomaly using the algorithm of *Wieczorek and Phillips* (1998). |
| [BAtoHilmRhoHDH](pybatohilmrhohdh.html) | Iteratively calculate the relief along an interface with laterally varying density contrast that corresponds to a given Bouguer anomaly using the algorithm of *Wieczorek and Phillips* (1998). |
| [DownContFilterMA](pydowncontfilterma.html) | Compute the minimum-amplitude downward continuation filter of *Wieczorek and Phillips* (1998). |
| [DownContFilterMC](pydowncontfiltermc.html) | Compute the minimum-curvature downward continuation filter of *Wieczorek and Phillips* (1998). |
| [NormalGravity](pynormalgravity.html) | Calculate the normal gravity on a flattened ellipsoid using the formula of Somigliana. |

## Magnetics routines

| Function name | Description |
| ------------- | ----------- |
| [MakeMagGridDH](pymakemaggriddh.html) | Create 2D cylindrical maps on a flattened ellipsoid of all three vector components of the magnetic field, the magnitude of the magnetic field, and the magnetic potential. |
| [MakeMagGridPoint](pymakemaggridpoint.html) | Determine the vector components of the magnetic field at a single point. |
| [MakeMagGradGridDH](pymakemaggradgriddh.html) | Calculate the components of the magnetic field tensor on a flattened ellipsoid. |
| [mag_spectrum](mag_spectrum.html) | Compute the spectrum of either the magnetic potential or magnetic field strength. |

## References

* Wieczorek, M. A. and R. J. Phillips, Potential anomalies on a sphere: applications to the thickness of the lunar crust, J. Geophys. Res., 103, 1715-1724, doi:[10.1029/97JE03136](https://doi.org/10.1029/97JE03136), 1998.
* Wieczorek, M. A. Gravity and topography of the terrestrial planets, Treatise on Geophysics, 10, 165-206, doi:[10.1016/B978-044452748-6/00156-5](https://doi.org/10.1016/B978-044452748-6/00156-5), 2007.
