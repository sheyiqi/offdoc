#### Self Time Bypass

[Company Name] memory compilers support the Self Time Bypass mode.

In the Self Time bypass mode is controlled by toggling the `T_ICLKBYP` pin. In this mode (`T_ICLKBYP=1`), the memory self time circuitry is bypassed. The memory timing is controlled by the external clock signal (`CLK`). Self Time bypass mode is initiated after the rising edge of `CLK` and is terminated by the falling edge. The Self Time bypass mode may be used to determine the margin of the internal self-timed circuitry.

