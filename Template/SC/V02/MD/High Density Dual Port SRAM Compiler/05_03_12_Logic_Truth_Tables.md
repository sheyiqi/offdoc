#### Logic Truth Tables

##### Memory Function Truth Table

> Note: In the above truth table, the state of test signals is `T_ICLKBYP=L`.\
>       Before starting normal memory operation (read/write), a `Negedge(1->0)` must be performed on `FRSRST` first.\
>       `NCM`: Memory bit-cell contents remain unchanged.\
>       `Q-1`: Maintains the state of the previous cycle.\
>       `Q`: Output without `CLK` latency.

The following table shows the memory function truth table for this compiler.



Table: Memory Function Truth Table



##### Power Mode Truth Table

The following table shows the truth table for Power mode.

> Note: This function is valid when the `Power Gating feature` is selected.\
>       In Periphery Off modes, the Periphery supply `VDD` is allowed to be powered down.\
>       `Q-1` = Memory output maintains the state of the previous cycle.\




Table: Power Mode Truth Table



##### Redundancy Scan Mode Truth Table

The following table shows the truth table for Redundancy Scan mode.

> Note: When `FRSCLK` is not running, please keep it at `H` or `L`.




Table: Redundancy Scan Mode Truth Table


