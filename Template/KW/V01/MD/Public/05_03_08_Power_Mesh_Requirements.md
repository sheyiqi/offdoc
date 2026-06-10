#### Power Mesh Requirements

The figure below shows the power mesh connections in this compiler. The power connection requirements for the `M3` and `Mye` layers are listed below.

- The power routing runs in `M3` vertical mesh.
- User has to connect the `Metal Mesh (Mxe-vertical)` at every `M3/My` intersection. For all `VSS`, `VDD`, and `VDDC` lines, the connection pitch of the `M3 mesh` should be `=<2.5µ`.
- Vias should be placed as densely as possible at all `M3/My` intersections.
- The signal pins of the memory instance are implemented on `M1` and can be accessed through `M2` or higher metal layers.




![Power Mesh Connections]([Template Path]\[Compiler Name]\power_mesh_connections.png)







