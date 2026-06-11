---
title: "XYZ High Density Via Rom Compiler User Manual"
toc-title: "Contents"
---

::: {.section-break}
:::


## Product Overview

This chapter provides an overview of the embedded memories of High Density Via Rom Compiler memory compiler.


###  Memory Compilers




### Compiler Naming Convention

The following table shows the structure of the name for the compiler.







+----------------+----------------------------+---------------+
| Name Segment   | Character in "XYZHDVOSR"   | Description   |
+================+============================+===============+
| Technology &   | XYZ                        | Process Node  |
| Process        |                            |               |
+----------------+----------------------------+---------------+
| Product type   | HD                         | High Density  |
+----------------+----------------------------+---------------+
| Ports          | VO                         | Via Rom       |
+----------------+----------------------------+---------------+
| Product        | SR                         | Compiler      |
| subfamily      |                            |               |
+----------------+----------------------------+---------------+

Table: Compiler Naming Rule Description







### Expanded Instance Naming Rules

`XYZHS1PRF1024X32M4B2VT0W0C1T0P0S0R0A0ME0E0_HSHC`

The breakdown of the name is as follows, see Table for details:

`XYZ HS 1P RF 1024 X 32 M4 B2 VT0 W0 C1 T0 P0 R0 S0 A0 ME0 E0 _ HSHC`

`1    2  3  4  5     6  7  8  9   10  11 12 13 14 15 16  17  18  19`




+----------------------+---------------+------------------------------------------------------------------------+
| Auto-Name  Segment   | Description   | Taken From:                                                            |
+======================+===============+========================================================================+
| 1                    | Process       | Process node (XYZ)                                                     |
+----------------------+---------------+------------------------------------------------------------------------+
| 2                    | Memory Type   | Base compiler name (HS, UHS, HD, UHD)                                  |
+----------------------+---------------+------------------------------------------------------------------------+
| 3                    | Memory Type   | Base compiler name (1P, SP, 2P, DP)                                    |
+----------------------+---------------+------------------------------------------------------------------------+
| 4                    | Memory Type   | Base compiler name (RF: Register File, SR: SRAM Compiler/Compiler)     |
+----------------------+---------------+------------------------------------------------------------------------+
| 5                    | NW value      | User-specified Number of Words (NW) value                              |
+----------------------+---------------+------------------------------------------------------------------------+
| 6                    | NB value      | User-specified Number of Bits (NB) value                               |
+----------------------+---------------+------------------------------------------------------------------------+
| 7                    | M <n>         | User-specified Column Mux (CM) value                                   |
+----------------------+---------------+------------------------------------------------------------------------+
| 8                    | B <n>         | User-specified Bank (BK) value                                         |
+----------------------+---------------+------------------------------------------------------------------------+
| 9                    | VT<n>         | Periphery Vt option(0: ELVT, 1:ULVT, 2:LVT, 3: SVT)                    |
+----------------------+---------------+------------------------------------------------------------------------+
| 10                   | W<0,1>        | Write Enable Bit (1 on, 0 off)                                         |
+----------------------+---------------+------------------------------------------------------------------------+
| 11                   | C<0,1>        | Center Decode (Always 1)                                               |
+----------------------+---------------+------------------------------------------------------------------------+
| 12                   | T<0,1,2,3>    | Bist mux enable & Scan Chain enable & Mbist enable (0 Bist Mux off /   |
|                      |               | Scan Chain off/ Mbist off, 1 Bist Mux on / Scan Chain off/ Mbist off,  |
|                      |               | 2  Bist Mux on / Scan Chain on/ Mbist off, 3  Bist Mux on / Scan Chain |
|                      |               | on/ Mbist on)                                                          |
+----------------------+---------------+------------------------------------------------------------------------+
| 13                   | P<0,1,2,3,4>  | Power gating enable & Dual Rail enable (0 Power Gating off / Dual Rail |
|                      |               | off, 1 Power Gating on / Dual Rail off, 2 Power Gating off  / Dual     |
|                      |               | Rail on, 3 Power Gating on / Dual Rail on / Periphery Off off, 4 Power |
|                      |               | Gating on / Dual Rail on / Periphery Off on)                           |
+----------------------+---------------+------------------------------------------------------------------------+
| 14                   | R<0,1,2>      | Memory Redundancy (0 No Redundancy,  1 Column Redundancy, 2 Column &   |
|                      |               | Row Redundancy)                                                        |
+----------------------+---------------+------------------------------------------------------------------------+
| 15                   | S<0,1>        | Self Time Bypass(0 off, 1on)                                           |
+----------------------+---------------+------------------------------------------------------------------------+
| 16                   | A<0,1,2,3>    | Read & Write Assist(0 Write Assist off / Read Assist off, 1 Write      |
|                      |               | Assist on/ Read Assist off, 2 Write Assist off / Read Assist on, 3     |
|                      |               | Write Assist on / Read Assist on)                                      |
+----------------------+---------------+------------------------------------------------------------------------+
| 17                   | ME<0,1>       | Memory Gating(0 off, 1 on)                                             |
+----------------------+---------------+------------------------------------------------------------------------+
| 18                   | E<0,1>        | Anti-Signature(0 off, 1 on), only support ROM                          |
+----------------------+---------------+------------------------------------------------------------------------+
| 19                   | <HC, HSHC>    | Bitcell type(HC, HSHC)                                                 |
+----------------------+---------------+------------------------------------------------------------------------+

Table: Breakdown of Automatic Naming Calculation






### Compiler Features

Memory compilers support the following features:

#### Periphery Transistor Threshold Voltage Option


The default setting and available options of `Periphery_Vt` are shown in the following table.


+-----------------+---------------------------------+
| Compiler Name   | High Density Via Rom Compiler   |
+=================+=================================+
| SVT             | Default                         |
+-----------------+---------------------------------+
| LVT             | Low                             |
+-----------------+---------------------------------+
| ULVT            | UltraLow                        |
+-----------------+---------------------------------+

Table: Periphery Vt Settings


The devices used by different `Periphery_Vt` options are listed in the following table.


+-----------------+---------------------------------+
| Compiler Name   | High Density Via Rom Compiler   |
+=================+=================================+
| SVT             | lvtll and lvt,                  |
|                 | ulvtll, ulvt                    |
+-----------------+---------------------------------+
| LVT             | lvt and lvtll,                  |
|                 | ulvtll, ulvt                    |
+-----------------+---------------------------------+
| ULVT            | ulvt and lvtll,                 |
|                 | lvt, ulvtll                     |
+-----------------+---------------------------------+

Table: Devices in Periphery Vt






#### Performance Shape

Memory compilers provide multiple performance shapes. The following table lists the parameters used to enable these options.


+---------------+---------------------------------------------------------------------+
| Feature       | Description                                                         |
+===============+=====================================================================+
| Center Decode | If "center decode" feature is enabled(C1), it can improve instance  |
|               | performance but increase area. There is one repair elements.\       |
|               | If "center decode" feature is disabled(C0), it can improve instance |
|               | area but decrease performance. There is one repair elements.\       |
|               | The Center decode of this version is always True.                   |
+---------------+---------------------------------------------------------------------+
| Banks         | Defining the number of banks of memory.                             |
+---------------+---------------------------------------------------------------------+
| Column Mux    | Providing different aspect ratio of memory.                         |
+---------------+---------------------------------------------------------------------+

Table: Performance Shape Settings




#### CEN-Gating


+------------+------------------------------------------------------------------------+
| Feature    | Description                                                            |
+============+========================================================================+
| CEN-Gating | By default, the A input pins are not gated by the CEN pin may increase |
|            | toggle power. In this case, CEN requires a relatively small setup      |
|            | time.\                                                                 |
|            | To reduce the toggle power of the input pins, users can enable the     |
|            | CEN-Gating feature; however, the setup time of CEN may increase.       |
+------------+------------------------------------------------------------------------+

Table: CEN-Gating





#### Power Gating




+------------------------+----------------+------------------------------------------------------------------------+
| Power Gating Setting   | Product Mode   | Function Description                                                   |
+========================+================+========================================================================+
| Disabled               | Default        | LS (Light Sleep) - Control the WL driver source biasing to reduce      |
|                        |                | static power. \                                                        |
|                        |                | Active high. The output state remains unchanged.                       |
+------------------------+----------------+------------------------------------------------------------------------+
| Enabled                | Advanced       | LS (Light Sleep) - Control the WL driver source biasing.\              |
|                        |                | DS (Deep Sleep) - Control the periphery circuit power gating, bitcell  |
|                        |                | array hold the original data and memory outputs remain Logic Low.\     |
|                        |                | SD (Shut Down) - Control the periphery circuit and bitcell array power |
|                        |                | gating, it performs a complete shutdown, bitcell array lose original   |
|                        |                | data, and memory outputs remain Logic Low.                             |
+------------------------+----------------+------------------------------------------------------------------------+

Table: Power Gating Mode






#### Self Time Bypass

Memory compilers support the Self Time Bypass mode.

In this mode (T\_ICLKBYP=1), the memory’s internal self-timing loop is breakdown, and memory operation timing is controled by external CLK. It’s for memory debug purpose.


#### Timing Margin Control

Memory compilers provide the Timing Margin Control feature.

The read operation time of ROM is controlled by Timing Margin.The read operation process of single-end ROM is as follows:

- The read bit line be precharged to logic 1.
- The word line transitions to a high voltage level, and the read bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down or keep the corresponding bit line through the transmission gate, then read bit line will pulled down to logic 0 or keep logic 1.
- The single end sense amplifier is activated to drive read bit line`s voltage to output data.


Read operations in ROM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of ROM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, ROM bitcell exhibits varying variability, leading to distinct characteristics in its read  capabilities. This variability can be mitigated by extending the duration of read  operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed.

Memory compiler controls the operating frequency of the compiler and the robustness of ROM read operations through `Timing Margin Control`.

+---------------+--------------------------------------------------------------+
| Timing Mode   | Description                                                  |
+===============+==============================================================+
| DEFAULT       | Recommended for operation at (VDD nom) ± 10% Nominal Voltage |
+---------------+--------------------------------------------------------------+

Table: Timing Mode Settings

Memory compiler provides the enable signal through the `TMEH/TMEL` pin. The `TMEH/TMEL` pin allows for the selection between internal default margin control and external margin control. When `TMEH/TMEL` is low, the instance uses the default self-timing control.

There are `Timing Margin Control` bus pins available in the memory compiler. `TMH/TML` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `TMH/TML` pins, including `TMEH/TMEL`, is provided for debug and yield analysis purposes. 

When `TMEH/TMEL` is high, instance margin could be adjusted by the Timing input pins. 
The margin sequentially increases as `TMH/TML` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Timing Margin Control` settings are user-adjustable. The user-side `TMH/TML` interface is uniformly encoded, ensuring that all compilers have the same default `TMH/TML` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

+----------------+-------+--------------------+--------------------+
| Periphery_Vt   | Mux   | Default TMH[3:0]   |   Default TML[5:0] |
+================+=======+====================+====================+
| SVT            | 8     | 1000               |             000100 |
+----------------+-------+--------------------+--------------------+
| SVT            | 16    | 1000               |             000100 |
+----------------+-------+--------------------+--------------------+
| SVT            | 32    | 1000               |             000100 |
+----------------+-------+--------------------+--------------------+
| SVT            | 64    | 1000               |             000100 |
+----------------+-------+--------------------+--------------------+
| LVT            | 8     | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| LVT            | 16    | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| LVT            | 32    | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| LVT            | 64    | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 8     | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 16    | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 32    | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 64    | 1100               |             001100 |
+----------------+-------+--------------------+--------------------+

Table: Default TM Bus Settings

> Note: For additional characterization data of TM settings, users can contact the Support Team.









## Compiler Profile




### Specifications

The specifications of High Density Via Rom Compiler.

#### Pin Description






+-----------+------------------+-----------------------------------------------------------------------+
| Signal    | Enabled          | Description                                                           |
+===========+==================+=======================================================================+
| A [m-1:0] | Always           | Address input.                                                        |
+-----------+------------------+-----------------------------------------------------------------------+
| CEN       | Always           | Chip Enable input. The memory is enabled and can perform read/write   |
|           |                  | operations when CEN is Logic Low; the memory is disabled when it is   |
|           |                  | Logic High.                                                           |
+-----------+------------------+-----------------------------------------------------------------------+
| CLK       | Always           | External Clock input.                                                 |
+-----------+------------------+-----------------------------------------------------------------------+
| T_ICLKBYP | Self Time Bypass | This pin must be controlled by software/firmware in silicon.  \       |
|           | feature          | In this mode (T_ICLKBYP=1), the memory’s internal self-timing loop is |
|           |                  | breakdown, and memory operation timing is controled by external CLK.  |
|           |                  | It’s for memory debug purpose.                                        |
+-----------+------------------+-----------------------------------------------------------------------+
| TME       | Always           | This pin must be controlled by software/firmware in silicon. \        |
|           |                  | Timing Margin Control Enable input.\                                  |
|           |                  | TME = 0, select the default Timing Margin Control setting; \          |
|           |                  | TME = 1, select the external Timing Margin Control pin setting.       |
+-----------+------------------+-----------------------------------------------------------------------+
| TMH [3:0] | Always           | This pin must be controlled by software/firmware in silicon.  \       |
|           |                  | Precharge Timing Margin Control Input bus. \                          |
|           |                  | The setting of TMH[3:0] controls the Tcq and Tcyc value of memory. \  |
|           |                  | TMH[3:0] = 4’b0000 is the slowest operating mode.                     |
+-----------+------------------+-----------------------------------------------------------------------+
| TML [5:0] | Always           | This pin must be controlled by software/firmware in silicon.  \       |
|           |                  | Discharge Timing Margin Control Input bus. \                          |
|           |                  | The setting of TML[5:0] controls the Tcq and Tcyc value of memory. \  |
|           |                  | TML[5:0] = 6’b001000 is the slowest operating mode.                   |
+-----------+------------------+-----------------------------------------------------------------------+
| SD        | Power Gating     | Shut Down Mode Contorl  Input. This pin turns off the power supply to |
|           | feature          | the periphery. Rom can always retain the memory data.                 |
+-----------+------------------+-----------------------------------------------------------------------+
| ASE       | Anti Signature   | Anti Signature Enable Input. When user specify the programmed rom     |
|           | feature          | code, ROM will store the anti signature code. Anti signature code is  |
|           |                  | calculated using a dedicated encryption algorithm. When ASE set to    |
|           |                  | logic HIGH, the anti signature code will be available on the output   |
|           |                  | pins independent of address being applied.                            |
+-----------+------------------+-----------------------------------------------------------------------+

Table: Input Pin Description






+-----------+----------------------+----------------------------------------------------------------------+
| Signal    | Enabled              | Description                                                          |
+===========+======================+======================================================================+
| Q [n-1:0] | always               | Data Output bus.                                                     |
+-----------+----------------------+----------------------------------------------------------------------+
| PUR       | Power Gating feature | “Power Up Ready” pin is used to reduce the peak power during wake-up |
|           |                      | from SD modes when instances are cascaded. When memory is in         |
|           |                      | operation, this flag pin must be high.                               |
+-----------+----------------------+----------------------------------------------------------------------+

Table: Output Pin Description




> Note: In the table above, `m` represents the maximum number of addresses supported by the compiler, and `n` represents the maximum number of bits supported by the compiler.



#### Compiler Range Information







+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| Column\   | Bank   | Word\   |   Word\ |   Word\ |   Bit\ |   Bit\ |   Bit\ | Maximum\   |
| Mux       |        | Step    |     Min |     Max |   Step |    Min |    Max | Density    |
+===========+========+=========+=========+=========+========+========+========+============+
| 8         | 1      | 32      |      64 |    2048 |      2 |      8 |    160 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 8         | 2      | 32      |     128 |    4096 |      2 |      8 |    160 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 8         | 4      | 32      |     256 |    8192 |      2 |      8 |    160 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 8         | 8      | 32      |     512 |    8192 |      2 |      8 |    160 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 1      | 64      |     128 |    4096 |      2 |      4 |     80 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 2      | 64      |     256 |    8192 |      2 |      4 |     80 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 4      | 64      |     512 |   16384 |      2 |      4 |     80 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 8      | 64      |    1024 |   16384 |      2 |      4 |     80 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 32        | 1      | 128     |     256 |    8192 |      2 |      4 |     40 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 32        | 2      | 128     |     512 |   16384 |      2 |      4 |     40 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 32        | 4      | 128     |    1024 |   32768 |      2 |      4 |     40 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 32        | 8      | 128     |    2048 |   32768 |      2 |      4 |     40 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 64        | 1      | 256     |     512 |   16384 |      2 |      4 |     20 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 64        | 2      | 256     |    1024 |   32768 |      2 |      4 |     20 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 64        | 4      | 256     |    2048 |   65536 |      2 |      4 |     20 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 64        | 8      | 256     |    4096 |   65536 |      2 |      4 |     20 | 1.25Mb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+

Table: Compiler Range








#### Logic Truth Tables

##### Memory Function Truth Table

> Note:  In the above truth table, the state of test signals is `T_ICLKBYP=L`.\
>      `NCM`: Memory bit-cell contents remain unchanged.\
>       `Q-1`: Maintains the state of the previous cycle.\
>       `Q`: Output without `CLK` latency.

The following table shows the memory function truth table for this compiler.



+------------+-------+-------+-----+------------+
| Function   | CLK   | CEN   | Q   | Memory\    |
|            |       |       |     | Contents   |
+============+=======+=======+=====+============+
| Idle       | L     | X     | Q-1 | NCM        |
+------------+-------+-------+-----+------------+
| Disabled   | H     | H     | Q-1 | NCM        |
+------------+-------+-------+-----+------------+
| Read       | H     | L     | Q   | NCM        |
+------------+-------+-------+-----+------------+

Table: Memory Function Truth Table



##### Power Mode Truth Table

The following table shows the truth table for Power mode.

> Note: This function is valid when the `Power Gating feature` is selected.\
>       In Periphery Off modes, the Periphery supply `VDD` is allowed to be powered down.\
>       `Q-1` = Memory output maintains the state of the previous cycle.



+-------------+-------+------+------+-------+-----+----------------------+
| Mode        | CEN   | LS   | SD   |   PUR | Q   | Comments             |
+=============+=======+======+======+=======+=====+======================+
| Normal      | 0/1   | 0    | 0    |     1 | Q-1 | Normal mode          |
+-------------+-------+------+------+-------+-----+----------------------+
| Light Sleep | 0/1   | 1    | 0    |     1 | Q-1 | Xdec power gate,\    |
|             |       |      |      |       |     | Bitline Discharge    |
+-------------+-------+------+------+-------+-----+----------------------+
| Shut Down\  | X     | X    | 0->1 |     0 | 0   | Periphery shutdown,\ |
|  enable     |       |      |      |       |     | array shutdown       |
+-------------+-------+------+------+-------+-----+----------------------+
| Shut Down\  | X     | X    | 1->0 |     1 | X   | Periphery wakeup,\   |
|  disable    |       |      |      |       |     | array wakeup         |
+-------------+-------+------+------+-------+-----+----------------------+

Table: Power Mode Truth Table







#### Waveform Diagrams

This section presents various timing waveforms.



>Note: If `CEN` is Low, it must be ensured that each signal meets the timing specification relative to the clock.\
>      If `CEN` is High, there is no need to meet the timing specification for each signal.\
>      This note also applies to Power Management pins such as `LS`.\
>      When `CEN=1`, `LS` can be asynchronously asserted and de-asserted.


The figure below shows the conventions used in the waveform diagrams.



![Waveform Conventions](../Template/SC/V02/Figure\High Density Via Rom Compiler\waveform_conventions.png)



![Read Cycle Timing Diagram](../Template/SC/V02/Figure\High Density Via Rom Compiler\read_cycle_timing_diagram.png)




![Light Sleep Mode Work Function Diagram](../Template/SC/V02/Figure\High Density Via Rom Compiler\light_sleep_mode_work_function_diagram.png)






![Shut Down Mode Work Function Diagram](../Template/SC/V02/Figure\High Density Via Rom Compiler\shut_down_mode_work_function_diagram.png)




#### Standard Operating Characterization Conditions



+------------------------------------------+-----------+--------+---------+----------------+------------------+
| PVT Corners                              | Process   | VDD\   | VDDC\   | Temperature\   | RC Extraction    |
|                                          |           | (V)    | (V)     | (C)            |                  |
+==========================================+===========+========+=========+================+==================+
| TT_0P75V_0P75V_25C_Typical               | TT        | 0.75   | 0.75    | 25             | Typical          |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| TT_0P75V_0P75V_85C_Typical               | TT        | 0.75   | 0.75    | 85             | Typical          |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| FFGNP_0P825V_0P825V_M40C_Cbest_CCbest_T  | FFGNP     | 0.825  | 0.825   | -40            | Cbest_CCbest_T   |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| FFGNP_0P825V_0P825V_0C_Cbest_CCbest_T    | FFGNP     | 0.825  | 0.825   | 0              | Cbest_CCbest_T   |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| FFGNP_0P825V_0P825V_125C_Cbest_CCbest_T  | FFGNP     | 0.825  | 0.825   | 125            | Cbest_CCbest_T   |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| SSGNP_0P675V_0P675V_M40C_Cworst_CCworst_ | SSGNP     | 0.675  | 0.675   | -40            | Cworst_CCworst_T |
| T                                        |           |        |         |                |                  |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| SSGNP_0P675V_0P675V_0C_Cworst_CCworst_T  | SSGNP     | 0.675  | 0.675   | 0              | Cworst_CCworst_T |
+------------------------------------------+-----------+--------+---------+----------------+------------------+
| SSGNP_0P675V_0P675V_125C_Cworst_CCworst_ | SSGNP     | 0.675  | 0.675   | 125            | Cworst_CCworst_T |
| T                                        |           |        |         |                |                  |
+------------------------------------------+-----------+--------+---------+----------------+------------------+

Table: Standard PVT Corners - Single Rail


> Note: `VDD`: Periphery Voltage;\
>       `VDDC`: Array Voltage


