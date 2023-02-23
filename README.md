# Piecewise Linear Interface Construction

Piecewise Linear Interface Construction (PLIC) is a numerical method used in computational fluid dynamics (CFD) for simulating the behavior of fluids in motion. The method involves dividing the fluid domain into a mesh of cells, and then constructing a piecewise linear approximation of the fluid interface between cells.

The method calculates the position and slope of the interface within each cell by interpolating values from the surrounding cells. This allows for a continuous representation of the interface that can be used to compute various fluid properties, such as pressure and velocity.

<img src=https://user-images.githubusercontent.com/97102775/220935427-e8f59fac-9c79-4cfd-9d4d-2d9918680306.jpg width="150" height="150"/>
Blue line represents the real interface between gray and white fluids and red dotted line represents the linear estimation of the interface with its normal vector **n**.


Example:
![vof_interface](https://user-images.githubusercontent.com/97102775/210425079-f3b72f9f-88b7-4570-a3e5-a0cbdec57018.jpg)

