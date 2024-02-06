# Piecewise Linear Interface Construction

Piecewise Linear Interface Construction (PLIC) is a numerical method used in computational fluid dynamics (CFD) for reconstructing the interface between fluids in motion in a Volume of Fluid (VOF) framework. It relies on the proper computation of the normal vector **n** of the interface for every cell, based in the color function values of the surrounding cells. Then, some geometrical transformations are applied to obtain the linear approximation of this interface.

<p align="center">
  <img src=https://user-images.githubusercontent.com/97102775/220935427-e8f59fac-9c79-4cfd-9d4d-2d9918680306.jpg width="150" height="150"/>
</p>
Blue line represents the real interface between gray and white fluids and red dotted line represents the linear estimation of the interface.

<!--
Example:

<img src=https://user-images.githubusercontent.com/97102775/210425079-f3b72f9f-88b7-4570-a3e5-a0cbdec57018.jpg align="center" width="250" height="250"/>
-->
