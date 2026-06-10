#### Bit Write

[Company Name] memory compilers provide the Bit Write feature.

Bit Write provides bit write option which instances I/O can write independently. When bit write option is ON, BWENA/BWENB becomes a bus. When bit write option is OFF, there is no BWENA/BWENB pin.

- If the `BWENA/BWENB` pin for an I/O is low, the data on the input pin (`DA/DB`) is written to the corresponding bit cell in the addressed location.
- If the `BWENA/BWENB` pin for an I/O is high, the data on the input pin (`DA/DB`) is not written to the corresponding bit cell in the addressed location.

There is no loss of power or speed when the Bit Write feature is enabled. However, power will be reduced by disabling writes using these pins.

