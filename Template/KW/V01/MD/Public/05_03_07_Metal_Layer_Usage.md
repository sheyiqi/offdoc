#### Metal Layer Usage

The figure below shows the usage of Metal Layers in this compiler.

- `M0`、`M1` and `M2` layers are completely blocked.
- `M0` is Bitline. `M1` and `M3` are used for Wordline.
- `M3` direction is parallel to SRAM poly. Connection to `M3` power pins should only be made from `My` over the memory (`M4` or above).
- `M4` and above are available for routing over the instance. `M4` is mainly used for power routing and can also be used for signal routing.




![Metal Layer Direction]([Template Path]\[Compiler Name]\metal_layer_direction.png)

The following table explains the routing guidelines for different metal layers.


Table: Metal Layer Routing






