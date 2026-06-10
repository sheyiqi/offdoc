#### CEB-Gating

[Company Name] memory compilers optionally support the Chip Enable Gating feature.

By default, the address `A` pins and data input `DI` pins are not gated by the `CEB` pin to reduce toggle power. In this case, `CEB` requires a relatively small setup time.

To reduce the toggle power of the address `A` pins and data input `DI` pins, users can enable the `CEB-Gating feature`; however, the setup time of CEB may increase.