#### Logic Truth Tables

##### Memory Function Truth Table

> Note: Before starting normal memory operation (read/write), a `Negedge(1->0)` must be performed on `REDRST` first.\
>       `NC`: `Q` output remains unchanged.\
>       `NCM`: Memory bit-cell contents remain unchanged.\
>       `Q-1`: Maintains the state of the previous cycle.\
>       `Q`: Output without `CLK` latency.

The following table shows the memory function truth table for this compiler.



Table: Memory Function Truth Table

> Note: In the above truth table, the state of test signals is `ETC=L`.

***

##### Power Mode Truth Table

The following table shows the truth table for Power mode.

> Note: This function is valid when the `Power Gating feature` is selected.\
>       In Periphery Off modes, the Periphery supply `VDD` is allowed to be powered down.\
>       `QP-1` = Pipe output maintains the state of the previous cycle.\
>       `Q-1` = Memory output maintains the state of the previous cycle.\
>       `PUD-1` = PUD output maintains the state of the previous cycle.\
>       `Qr` = Memory output restores to the state before entering power down mode.



Table: Power Mode Truth Table



##### Redundancy Scan Mode Truth Table

The following table shows the truth table for Redundancy Scan mode.

> Note: When `REDCK` is not running, please keep it at `H` or `L`.




Table: Redundancy Scan Mode Truth Table


