#### Write Assistance

[Company Name] memory compilers provide the Write Assistance feature.

The `NBL` pin provides control settings for the negative BL voltage to improve write capability. `NBL[2]` is used to enable the negative BL function and is active high. The write capability of a memory instance can be adjusted through the additional input pins `NBL[1:0]`. The write capability increases as `NBL[1:0]` changes sequentially from `00`, `01`, `10`, to `11`.

The default setting of `NBL[2:0]` is `000`.


                                       

Table: Default NBL Bus Settings

The `DLN` pin is used to control the pulse width of the negative voltage on the SRAM bitline. When `DLN[2:0]` is set to `000`, the pulse width is the slowest. When `DLN[2:0]` is set to `111`, the pulse width is the fastest.


                                       

Table: Default DLN Bus Settings





