#### Write Assistance

[Company Name] memory compilers provide the Write Assistance feature.

The `WA` pin provides control settings for the negative BL voltage to improve write capability. `WA[2]` is used to enable the negative BL function and is active high. The write capability of a memory instance can be adjusted through the additional input pins `WA[1:0]`. The write capability increases as `WA[1:0]` changes sequentially from `00`, `01`, `10`, to `11`.



                                       

Table: Default WA Bus Settings

The `WPULSE` pin is used to control the pulse width of the negative voltage on the SRAM bitline. When `WPULSE[2:0]` is set to `000`, the negative bitline boost is the latest. When `WPULSE[2:0]` is set to `111`, the negative bitline boost is the earliest.


                                       

Table: Default WPULSE Bus Settings





