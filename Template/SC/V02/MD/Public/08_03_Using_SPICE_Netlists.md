### SPICE Netlist Usage

 `SPICE netlist` (transistor-level netlist) can only be used for `LVS verification`.
 
The compiler `SPICE netlist` contains the subcircuit representations of leaf cells used for building an instance.

The compiler library of subcircuits use the same prefix as the `GDSII library`. So, you can combine netlists when combining instances from different compilers on to one design. The `SPICE subcircuits` match with the `GDSII leaf cells`.

