### Power and Pin Router Control

This family of memory compilers implements a power mesh configuration. Power mesh is created by interlaced `Metal4` mesh straps of `VDD` and `VSS` over the memory. These straps run orthogonal to the `Metal3 layers` below and are connected to their respective `VDD` and `VSS` straps. At the chip level, users must make connections to the `Metal4 straps` from a higher metal. Users can control the signal routing layer separately from the power ring layers.

> Note: Please consult the foundry for the required orientation of the Instance. `R0` is the compiler default value and meets the design rule requirements.

