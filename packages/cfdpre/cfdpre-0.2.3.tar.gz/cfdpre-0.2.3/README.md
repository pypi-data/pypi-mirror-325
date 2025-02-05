<h1 align="center">
<img src="https://raw.githubusercontent.com/phsheth/cfdpre/refs/heads/main/cfdprelogo.png" width="300">
</h1><br>


What is CFDPre?
----------------------

CFDPre is an open-source collection of object-oriented software tools for
calculating boundary layer mesh dimensions for Computational Fluid Dynamics simulations.
Among other things, it can be used to:

* Calculate First Layer Thickness, Growth Ratio and Final Layer Thickess


Installation
----------------------

[![Install](https://img.shields.io/pypi/v/cfdpre?label=CFDPre)](
https://pypi.org/project/cfdpre/) [![PyPI Downloads](https://img.shields.io/pypi/dm/cfdpre?label=PyPI%20Downloads)](
https://pypistats.org/packages/cfdpre)

In your command line, within Python environment:
```pythom
    pip install cfdpre
```
- The Python module can also be installed using pip on Windows, macOS, and Linux.


Usage
----------------------

```python
from cfdpre import yhgrcalc
yhgrcalc('Air', 50, 10, 2.5, 125, 1, 8)
```

Output:
```python
{'fluid': 'Air',
 'temperature [C]': 50,
 'pressure [bar]': 10,
 'massflow [kg/sec]': 2.5,
 'hydraulicdia [mm]': 125,
 'target yplus': 1,
 'number of layers': 8,
 'dynvisc [N-sec/m^2]': 1.9762497305390764e-05,
 'thermal conductivity [W/m-k]': 0.028357331300649127,
 'specific heat [cp] [J/kg-k]': 1019.3146170790077,
 'density [kg/m^3]': 10.792698589669245,
 'kinematic viscosity [m^2/s]': 1.8310987878701066e-06,
 'flow velocity [m/sec]': 18.875569021507275,
 'reynolds number': 1288541.1444310248,
 'prandtl number': 0.7103701741111368,
 'skin friction coefficient [cf]': 0.0035835733898580227,
 'wall shear stress [tau_wall]': 6.889956204766106,
 'yplus [m]': 2.2917570116263887e-06,
 'first layer height [m]': 4.5835140232527775e-06,
 'Growth Ratio': 2.3120331242085856,
 'Final Layer Thickness [m]': 0.0016186648187374525}
```

Documentation
----------------------

In progress - not yet made!

- **Project Home Page:** https://cfdpre.github.io/ [under construction]
- **Users Group:** https://groups.google.com/g/cfdpre
- **Source code:** https://github.com/phsheth/cfdpre
- **PyPI Page:** https://pypi.org/project/cfdpre/



Call for Contributors
----------------------

The CFDPre project welcomes your expertise and enthusiasm! Better to discuss on the users group before starting to contribute!


Project Log
----------------------
January 2025:
1. Created Library


Project RoadMap:
----------------------

1. Documentation for existing functionality.
2. Include example data within library.






