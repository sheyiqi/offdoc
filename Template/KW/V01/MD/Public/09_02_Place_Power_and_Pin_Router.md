### Power and Pin Router Control

This memory compilers family implements power mesh configuration. The power mesh consists of interleaved `Metal4` grid `VDD` and `VSS` straps above the memory. These straps are orthogonal to the underlying `Metal3 layers`, and are connected to the corresponding `VDD` and `VSS` straps respectively. At the chip level, users must connect to the `Metal4 straps` from higher-level metals. Users can also separately control the signal routing layer and the power ring layers.For signal routing, `Metal1` is supported.

> Note: Please consult the foundry for the required orientation of the Instance. `R0` is the compiler default value and meets the design rule requirements.
