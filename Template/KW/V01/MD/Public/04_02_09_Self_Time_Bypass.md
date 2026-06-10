#### Self Time Bypass

[Company Name] memory compilers support the Self Time Bypass mode.

In the Self Time bypass mode is controlled by toggling the `ETC` pin. In this mode (`ETC=1`), the memory self time circuitry is bypassed. The memory timing is controlled by the external clock signal (`CK`). Self Time bypass mode is initiated after the rising edge of `CK` and is terminated by the falling edge. The Self Time bypass mode may be used to determine the margin of the internal self-timed circuitry.