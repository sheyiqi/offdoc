#### Metal Layer Usage

The figure below shows the usage of Metal Layers in this compiler.

- `M1`, `M2` and `M3` layers are completely blocked.
- `M1` is Bitline. `M2` and `M4` are used for Wordline.
- `M4` direction is parallel to SRAM poly. Connection to `M4` power pins should only be made from `My` over the memory (`M5` or above).
- `M5` and above are available for routing over the instance. `M5` is mainly used for power routing and can also be used for signal routing.




![Metal Layer Direction]([Template Path]\Public\[IP Prefix]\metal_layer_direction.png)

The following table explains the routing guidelines for different metal layers.


Table: Metal Layer Routing






