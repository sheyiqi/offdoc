#### Power Mesh Requirements

The figure below shows the power mesh connections in this compiler. The power connection requirements for the `M4` and `My` layers are listed below.

- The power routing runs in `M4` vertical mesh.
- User has to connect the Metal Mesh at every `M4/My` intersection. For all `VSS`, `VDD`, and `VDDC` lines, the connection pitch of the `M4 mesh` should be `=<2.5µ`.
- Vias should be placed as densely as possible at all `M4/My` intersections.
- The signal pins of the memory instance are implemented on `M2` and can be accessed through `M3` or higher metal layers.




![Power Mesh Connections]([Template Path]\Public\[IP Prefix]\power_mesh_connections.png)









