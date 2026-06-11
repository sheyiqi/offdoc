---
title: "XYZ High Speed Two Port Register File User Manual"
toc-title: "Contents"
---

::: {.section-break}
:::


## Product Overview

This chapter provides an overview of the embedded memories of High Speed Two Port Register File memory compiler.


###  Memory Compilers




### Compiler Naming Convention

The following table shows the structure of the name for the compiler.







+----------------+----------------------------+---------------+
| Name Segment   | Character in "XYZHS2PRF"   | Description   |
+================+============================+===============+
| Technology &   | XYZ                        | Process Node  |
| Process        |                            |               |
+----------------+----------------------------+---------------+
| Product type   | HS                         | High Speed    |
+----------------+----------------------------+---------------+
| Ports          | 2P                         | Two Port      |
+----------------+----------------------------+---------------+
| Product        | RF                         | Register File |
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


+-----------------+-------------------------------------+
| Compiler Name   | High Speed Two Port Register File   |
+=================+=====================================+
| LVT             | Low                                 |
+-----------------+-------------------------------------+
| ULVT            | UltraLow                            |
+-----------------+-------------------------------------+

Table: Periphery Vt Settings


The devices used by different `Periphery_Vt` options are listed in the following table.


+-----------------+-------------------------------------+
| Compiler Name   | High Speed Two Port Register File   |
+=================+=====================================+
| LVT             | lvt and lvtll,                      |
|                 | ulvt, ulvtll,                       |
|                 | elvt                                |
+-----------------+-------------------------------------+
| ULVT            | ulvt and lvt,                       |
|                 | lvtll, ulvtll,                      |
|                 | elvt                                |
+-----------------+-------------------------------------+

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




#### Bit Write



+-----------+---------------------------------------------------------------------+
| Feature   | Description                                                         |
+===========+=====================================================================+
| Bit Write | Memory compilers provide the Bit Write Enable feature.\             |
| Enable    | - If the BWENA = 0,  the corresponding bit’s data is written to the |
|           | bit cell array.\                                                    |
|           | - If the BWENA = 1,  the corresponding bit’s data is not written to |
|           | the bit cell array.                                                 |
+-----------+---------------------------------------------------------------------+

Table: Bit Write Enable

#### CEN-Gating


+------------+------------------------------------------------------------------------+
| Feature    | Description                                                            |
+============+========================================================================+
| CEN-Gating | By default, the AA/AB/DA/BWENA input pins are not gated by the         |
|            | CENA/CENB pin may increase toggle power. In this case, CENA/CENB       |
|            | requires a relatively small setup time.\                               |
|            | To reduce the toggle power of the input pins, users can enable the     |
|            | CEN-Gating feature; however, the setup time of CENA/CENB may increase. |
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






#### Interface Dual Rail

Memory compilers support the Interface Dual Rail feature.

Users can enable independent voltage rails for the `input/output interface logic` and the `internal periphery logic + array` at the instance level. Level shifters are used in the `input interface logic`. This option is controlled by setting the `Interface Dual Rail feature`. For more information, see “Standard Operating Characterization Conditions” in Chapter 2. This option allows the array to remain within the safe operating voltage range of VDD nom +/- 10%.

When the `Interface Dual Rail feature` is selected, Light Sleep mode is also supported. After the dual-rail option is enabled, Deep Sleep and Shut Down modes can be enabled independently when the `Power Gating feature` is selected. When the `Periphery Off feature` is further selected, periphery power shutoff can be enabled. For more information, see “Periphery Off” in this chapter.


#### Redundancy

Memory compilers can generate memory instances with built-in redundancy for memory repair purposes.


Redundancy is enabled via the `Redundancy feature`.

    When the `Column Redundancy feature` is selected, column redundancy is enabled; 
    When the `Row Redundancy feature` is selected, both row and column redundancy resources are provided.



+------------------+------------------------------+
| Compiler Group   | Redundancy Architecture      |
+==================+==============================+
| Register File    | Column Redundancy Resources  |
+------------------+------------------------------+
| SRAM Compiler    | Column Redundancy Resources\ |
|                  | Row Redundancy Resources     |
+------------------+------------------------------+
| Rom Compiler     | nan                          |
+------------------+------------------------------+

Table: Repair Elements Mode



![Column Redundancy Replace Mechanism](../Template/SC/V02/Figure\High Speed Two Port Register File\Column_Redundancy_replace_mechanism.png)

Figure show an example of the column redundancy replace mechanism in a 8 bits column Mux memory instance. In the case, 6th IO needs to be repaired. Once redundancy DFF chain be configured, redundancy scheme works. Q[7] receives the output of the redundant sub-array, Q[6] receives the output of Q[7], then replacement complete. The rest IO[0]~IO[5] receive the output of themselves.

One IO where defect is detected can be replaced by redundancy. All data flip-flop which used to configure redundancy logic to column redundant substitution. The redundant substitution of configure choose based on memory`s bit width of input data bus.

![Column Redundancy Waveform](../Template/SC/V02/Figure\High Speed Two Port Register File\1_Column_redundancy.png)

Figure shows the scan sequence of 1 column redundant substitution is followed by least significant bit of io address (0), then io address increasing until most significant bit of io address (N-2) is captured, and finally redundancy enable signal (N-1) is the last signal of scan sequence.








#### Self Time Bypass

Memory compilers support the Self Time Bypass mode.

In this mode (T\_ICLKBYP=1), the memory’s internal self-timing loop is breakdown, and memory operation timing is controled by external CLK. It’s for memory debug purpose.


#### Timing Margin Control

Memory compilers provide the Timing Margin Control feature.

The read and write operation time of SRAM is controlled by Timing Margin.The read operation process of single-end SRAM is as follows:

- The word line transitions to a high voltage level, and the read bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down or keep the corresponding bit line through the transmission gate, then read bit line will pulled down to logic 0 or keep logic 1.
- The single end sense amplifier is activated to drive read bit line`s voltage to output data.

The write operation process of differential SRAM is as follows:

- The word line is activated, and the input data is driven to the bit line pair, maintaining logic 0 and 1 respectively.
- The bit line of logic 0 pulls down the memory storage node of the bitcell through the transmission gate.
- The storage node changes logic 1 to logic 0 through the cross-couple structure

Both read and write operations in SRAM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of SRAM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, SRAM bitcell exhibits varying variability, leading to distinct characteristics in its read and write capabilities. This variability can be mitigated by extending the duration of read and write operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed.

Memory compiler controls the operating frequency of the compiler and the robustness of SRAM read and write operations through `Timing Margin Control`.

+---------------+--------------------------------------------------------------+
| Timing Mode   | Description                                                  |
+===============+==============================================================+
| DEFAULT       | Recommended for operation at (VDD nom) ± 10% Nominal Voltage |
+---------------+--------------------------------------------------------------+

Table: Timing Mode Settings

Memory compiler provides the enable signal through the `TMEA/TMEB` pin. The `TMEA/TMEB` pin allows for the selection between internal default margin control and external margin control. When `TMEA/TMEB` is low, the instance uses the default self-timing control.

There are `Timing Margin Control` bus pins available in the memory compiler. `TMA/TMB` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `TMA/TMB` pins, including `TMEA/TMEB`, is provided for debug and yield analysis purposes. 

When `TMEA/TMEB` is high, instance margin could be adjusted by the Timing input pins. 
The margin sequentially increases as `TMA/TMB` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Timing Margin Control` settings are user-adjustable. The user-side `TMA/TMB` interface is uniformly encoded, ensuring that all compilers have the same default `TMA/TMB` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

+----------------+-------+--------------------+--------------------+
| Periphery_Vt   | Mux   | Default TMA[3:0]   |   Default TMB[3:0] |
+================+=======+====================+====================+
| LVT            | 1     | 0100               |               0100 |
+----------------+-------+--------------------+--------------------+
| LVT            | 2     | 0100               |               0100 |
+----------------+-------+--------------------+--------------------+
| LVT            | 4     | 0100               |               0100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 1     | 0100               |               0100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 2     | 0100               |               0100 |
+----------------+-------+--------------------+--------------------+
| ULVT           | 4     | 0100               |               0100 |
+----------------+-------+--------------------+--------------------+

Table: Default TM Bus Settings

> Note: For additional characterization data of TM settings, users can contact the Support Team.









## Compiler Profile




### Specifications

The specifications of High Speed Two Port Register File.

#### Pin Description






+---------------+--------------------+------------------------------------------------------------------------+
| Signal        | Enabled            | Description                                                            |
+===============+====================+========================================================================+
| AA [m-1:0]    | Always             | A Port Address input.                                                  |
+---------------+--------------------+------------------------------------------------------------------------+
| AB [m-1:0]    | Always             | B Port Address input.                                                  |
+---------------+--------------------+------------------------------------------------------------------------+
| DA [n-1:0]    | Always             | A Port Data input.                                                     |
+---------------+--------------------+------------------------------------------------------------------------+
| BWENA [n-1:0] | Bit Write feature  | A Port Bit Write Enable. Bit Write is enabled when BWENA is Logic Low. |
|               |                    | When the Bit Write feature is included,  write operation can be        |
|               |                    | performed by enabled I/Os bits.                                        |
+---------------+--------------------+------------------------------------------------------------------------+
| CENA          | Always             | A Port Chip Enable input. The memory is enabled and can perform write  |
|               |                    | operations when CENA is Logic Low; the memory is disabled when it is   |
|               |                    | Logic High.                                                            |
+---------------+--------------------+------------------------------------------------------------------------+
| CENB          | Always             | B Port Chip Enable input. The memory is enabled and can perform read   |
|               |                    | operations when CENB is Logic Low; the memory is disabled when it is   |
|               |                    | Logic High.                                                            |
+---------------+--------------------+------------------------------------------------------------------------+
| CLKA          | Always             | A Port External Clock input.                                           |
+---------------+--------------------+------------------------------------------------------------------------+
| CLKB          | Always             | B Port External Clock input.                                           |
+---------------+--------------------+------------------------------------------------------------------------+
| FRSIN         | Redundancy feature | Faulty Repair Register Scan Input.  Redundancy Scan input bit.         |
+---------------+--------------------+------------------------------------------------------------------------+
| FRSE          | Redundancy feature | Faulty Repair Register Scan Enable Input.  Redundancy Scanning enable, |
|               |                    | active high.                                                           |
+---------------+--------------------+------------------------------------------------------------------------+
| FRSRST        | Redundancy feature | Faulty Repair Register Scan Asynchronous Reset Input. Before memory    |
|               |                    | normal access,  FRSRST must be performed a high to low(negative edge)  |
|               |                    | control signal.                                                        |
+---------------+--------------------+------------------------------------------------------------------------+
| FRSCLK        | Redundancy feature | Faulty Repair Register Scan Clock.                                     |
+---------------+--------------------+------------------------------------------------------------------------+
| T_ICLKBYP     | Self Time Bypass   | This pin must be controlled by software/firmware in silicon.  \        |
|               | feature            | In this mode (T_ICLKBYP=1), the memory’s internal self-timing loop is  |
|               |                    | breakdown, and memory operation timing is controled by external CLK.   |
|               |                    | It’s for memory debug purpose.                                         |
+---------------+--------------------+------------------------------------------------------------------------+
| TMEA          | Always             | This pin must be controlled by software/firmware in silicon. \         |
|               |                    | A Port Timing Margin Control Enable input.\                            |
|               |                    | TMEA = 0, select the default Timing Margin Control setting; \          |
|               |                    | TMEA = 1, select the external Timing Margin Control pin setting.       |
+---------------+--------------------+------------------------------------------------------------------------+
| TMEB          | Always             | This pin must be controlled by software/firmware in silicon. \         |
|               |                    | B Port Timing Margin Control Enable input.\                            |
|               |                    | TMEB = 0, select the default Timing Margin Control setting; \          |
|               |                    | TMEB = 1, select the external Timing Margin Control pin setting.       |
+---------------+--------------------+------------------------------------------------------------------------+
| TMA [3:0]     | Always             | This pin must be controlled by software/firmware in silicon.  \        |
|               |                    | A Port Timing Margin Control Input bus. \                              |
|               |                    | The setting of TMA[3:0] controls the Tcq and Tcyc value of memory. \   |
|               |                    | TMA[3:0] = 4’b0000 is the slowest operating mode.                      |
+---------------+--------------------+------------------------------------------------------------------------+
| TMB [3:0]     | Always             | This pin must be controlled by software/firmware in silicon.  \        |
|               |                    | B Port Timing Margin Control Input bus. \                              |
|               |                    | The setting of TMB[3:0] controls the Tcq and Tcyc value of memory. \   |
|               |                    | TMB[3:0] = 4’b0000 is the slowest operating mode.                      |
+---------------+--------------------+------------------------------------------------------------------------+
| LS            | Always             | Light Sleep Mode Control Input. When the memory is disabled and this   |
|               |                    | pin is set, the memory enters low leakage mode. The output state       |
|               |                    | remains unchanged.                                                     |
+---------------+--------------------+------------------------------------------------------------------------+
| DS            | Power Gating       | Deep Sleep Mode Control Input. It turns off the periphery power supply |
|               | feature            | while retaining the memory contents. Memory outputs keep low.          |
+---------------+--------------------+------------------------------------------------------------------------+
| SD            | Power Gating       | Shut Down Mode Control Input. It performs a complete shutdown( both    |
|               | feature            | periphery and memory array), bitcell array lose original data, and     |
|               |                    | memory outputs remain Logic Low.                                       |
+---------------+--------------------+------------------------------------------------------------------------+

Table: Input Pin Description






+------------+----------------------+----------------------------------------------------------------------+
| Signal     | Enabled              | Description                                                          |
+============+======================+======================================================================+
| QB [n-1:0] | always               | B Port Data Output bus.                                              |
+------------+----------------------+----------------------------------------------------------------------+
| FRSOUT     | Redundancy feature   | Faulty Repair Register Scan Output. It is used to output the Faulty  |
|            |                      | Repair Register Scan bit. When the Power Gating feature mode is      |
|            |                      | selected, its content will be lost if the power supply of the        |
|            |                      | periphery is turned off.                                             |
+------------+----------------------+----------------------------------------------------------------------+
| PUR        | Power Gating feature | “Power Up Ready” pin is used to reduce the peak power during wake-up |
|            |                      | from DS and SD modes when instances are cascaded. When memory is in  |
|            |                      | operation, this flag pin must be high.                               |
+------------+----------------------+----------------------------------------------------------------------+

Table: Output Pin Description




> Note: In the table above, `m` represents the maximum number of addresses supported by the compiler, and `n` represents the maximum number of bits supported by the compiler.\
>           A Port means Write Port.\
>           B Port Means Read Port.



#### Compiler Range Information







+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| Column\   | Bank   | Word\   |   Word\ |   Word\ |   Bit\ |   Bit\ |   Bit\ | Maximum\   |
| Mux       |        | Step    |     Min |     Max |   Step |    Min |    Max | Density    |
+===========+========+=========+=========+=========+========+========+========+============+
| 1         | 1      | 4       |       8 |      64 |      4 |     16 |    256 | 16Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 1         | 2      | 8       |      16 |     128 |      4 |     16 |    256 | 32Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 1         | 4      | 16      |      32 |     256 |      4 |     16 |    256 | 64Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 1         | 8      | 32      |      64 |     256 |      4 |     16 |    256 | 64Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 2         | 1      | 8       |      16 |     128 |      2 |      8 |    256 | 32Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 2         | 2      | 16      |      32 |     256 |      2 |      8 |    256 | 64Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 2         | 4      | 32      |      64 |     512 |      2 |      8 |    256 | 128Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 2         | 8      | 64      |     128 |     512 |      2 |      8 |    256 | 128Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 4         | 1      | 16      |      32 |     256 |      1 |      8 |    128 | 32Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 4         | 2      | 32      |      64 |     512 |      1 |      8 |    128 | 64Kb       |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 4         | 4      | 64      |     128 |    1024 |      1 |      8 |    128 | 128Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 4         | 8      | 128     |     256 |    1024 |      1 |      8 |    128 | 128Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+

Table: Compiler Range








#### Logic Truth Tables

##### Memory Function Truth Table

> Note: In the above truth table, the state of test signals is `T_ICLKBYP=L`.\
>       After Power up, before starting normal memory operation (read/write), a `Negedge(1->0)` must be performed on `FRSRST` first.\
>       `NCM`: Memory bit-cell contents remain unchanged.\
>       `Q-1`: Maintains the state of the previous cycle.\
>       `Q`: Output without `CLK` latency.



+------------+--------+--------+--------+--------+---------+---------+------+------------+
| Function   | CLKA   | CLKB   | CENA   | CENB   | BWENA   | DA      | QB   | Memory\    |
|            |        |        |        |        |         |         |      | Contents   |
+============+========+========+========+========+=========+=========+======+============+
| Idle       | L      | L      | X      | X      | X       | X       | Q-1  | NCM        |
+------------+--------+--------+--------+--------+---------+---------+------+------------+
| Disabled   | H      | H      | H      | H      | X       | X       | Q-1  | NCM        |
+------------+--------+--------+--------+--------+---------+---------+------+------------+
| Read       | X      | H      | H      | L      | H       | X       | Q    | NCM        |
+------------+--------+--------+--------+--------+---------+---------+------+------------+
| Write      | H      | X      | L      | H      | L       | Data-in | Q-1  | Data-in    |
+------------+--------+--------+--------+--------+---------+---------+------+------------+
| Write Mask | H      | X      | L      | H      | H       | X       | Q-1  | NCM        |
+------------+--------+--------+--------+--------+---------+---------+------+------------+

Table: Memory Function Truth Table



##### Power Mode Truth Table

The following table shows the truth table for Power mode.

> Note: This function is valid when the `Power Gating feature` is selected.\
>       In Periphery Off modes, the Periphery supply `VDD` is allowed to be powered down.\
>       `Q-1` = Memory output maintains the state of the previous cycle.



+-------------+-------------+------+------+------+-------+------+----------------------+
| Mode        | CENA/CENB   | LS   | DS   | SD   |   PUR | QB   | Comments             |
+=============+=============+======+======+======+=======+======+======================+
| Normal      | 0/1         | 0    | 0    | 0    |     1 | Q-1  | Normal mode          |
+-------------+-------------+------+------+------+-------+------+----------------------+
| Light Sleep | 0/1         | 1    | 0    | 0    |     1 | Q-1  | Xdec power gate,\    |
|             |             |      |      |      |       |      | Bitline Discharge    |
+-------------+-------------+------+------+------+-------+------+----------------------+
| Deep Sleep\ | X           | X    | 0->1 | 0    |     0 | 0    | Periphery shutdown   |
|  enable     |             |      |      |      |       |      |                      |
+-------------+-------------+------+------+------+-------+------+----------------------+
| Deep Sleep\ | X           | X    | 1->0 | 0    |     1 | X    | Periphery wakeup     |
|  disable    |             |      |      |      |       |      |                      |
+-------------+-------------+------+------+------+-------+------+----------------------+
| Shut Down\  | X           | X    | X    | 0->1 |     0 | 0    | Periphery shutdown,\ |
|  enable     |             |      |      |      |       |      | array shutdown       |
+-------------+-------------+------+------+------+-------+------+----------------------+
| Shut Down\  | X           | X    | X    | 1->0 |     1 | X    | Periphery wakeup,\   |
|  disable    |             |      |      |      |       |      | array wakeup         |
+-------------+-------------+------+------+------+-------+------+----------------------+

Table: Power Mode Truth Table



##### Redundancy Scan Mode Truth Table

The following table shows the truth table for Redundancy Scan mode.

> Note: When `FRSCLK` is not running, please keep it at `H` or `L`.




+------------+----------+--------+-----------+-------------+----------+----------+
| Function   | FRSCLK   | FRSE   | FRSIN     | CENA/CENB   | FRSRST   | FRSOUT   |
+============+==========+========+===========+=============+==========+==========+
| Disable    | X        | X      | X         | H           | L        | X        |
+------------+----------+--------+-----------+-------------+----------+----------+
| Normal     | X        | L      | X         | L           | L        | X        |
+------------+----------+--------+-----------+-------------+----------+----------+
| Scan       | L->H     | H      | Fuse_Data | X           | L        | X        |
+------------+----------+--------+-----------+-------------+----------+----------+
| Reset      | X        | X      | X         | X           | H        | L        |
+------------+----------+--------+-----------+-------------+----------+----------+

Table: Redundancy Scan Mode Truth Table



#### Waveform Diagrams

This section presents various timing waveforms.



>Note: If `CEN` is Low, it must be ensured that each signal meets the timing specification relative to the clock.\
>      If `CEN` is High, there is no need to meet the timing specification for each signal.\
>      This note also applies to Power Management pins such as `LS`.\
>      When `CEN=1`, `LS` can be asynchronously asserted and de-asserted.


The figure below shows the conventions used in the waveform diagrams.



![Waveform Conventions](../Template/SC/V02/Figure\High Speed Two Port Register File\waveform_conventions.png)



![Read Cycle Timing Diagram](../Template/SC/V02/Figure\High Speed Two Port Register File\read_cycle_timing_diagram.png)




![Write Cycle Timing Diagram](../Template/SC/V02/Figure\High Speed Two Port Register File\write_cycle_timing_diagram.png)



![Light Sleep Mode Work Function Diagram](../Template/SC/V02/Figure\High Speed Two Port Register File\light_sleep_mode_work_function_diagram.png)






![Deep Sleep Mode Work Function Diagram](../Template/SC/V02/Figure\High Speed Two Port Register File\deep_sleep_mode_work_function_diagram.png)




![Shut Down Mode Work Function Diagram](../Template/SC/V02/Figure\High Speed Two Port Register File\shut_down_mode_work_function_diagram.png)




#### Standard Operating Characterization Conditions


> Note: `VDD`: Periphery Voltage;\
>       `VDDC`: Array Voltage

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





