---
title: "XYZ High Speed Single Port SRAM Compiler User Manual"
toc-title: "Contents"
---

::: {.section-break}
:::


## Product Overview

This chapter provides an overview of the embedded memories of High Speed Single Port SRAM Compiler memory compiler.


###  Memory Compilers




### Compiler Naming Convention

The following table shows the structure of the name for the compiler.







+----------------+----------------------------+---------------+
| Name Segment   | Character in "XYZHSSPSR"   | Description   |
+================+============================+===============+
| Technology &   | XYZ                        | Process Node  |
| Process        |                            |               |
+----------------+----------------------------+---------------+
| Product type   | HS                         | High Speed    |
+----------------+----------------------------+---------------+
| Ports          | SP                         | Single Port   |
+----------------+----------------------------+---------------+
| Product        | SR                         | SRAM Compiler |
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


+-----------------+----------------------------------------+
| Compiler Name   | High Speed Single Port SRAM Compiler   |
+=================+========================================+
| LVT             | Low                                    |
+-----------------+----------------------------------------+
| ULVT            | UltraLow                               |
+-----------------+----------------------------------------+

Table: Periphery Vt Settings


The devices used by different `Periphery_Vt` options are listed in the following table.


+-----------------+-------------------------------------+
| Compiler Name   | High Speed One Port Register File   |
+=================+=====================================+
| LVT             | lvtll, lvt,                         |
|                 | ulvtll and ulvt                     |
+-----------------+-------------------------------------+
| ULVT            | lvtll, lvt,                         |
|                 | ulvtll and                          |
|                 | ulvt, elvt                          |
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

XYZ memory compilers provide the Bit Write feature.

Bit Write provides bit write option which instances I/O can write independently. When bit write option is ON, BWEN becomes a bus. When bit write option is OFF, there is no BWEN pin.

- If the `BWEN` pin for an I/O is low, the data on the input pin (`D`) is written to the corresponding bit cell in the addressed location.
- If the `BWEN` pin for an I/O is high, the data on the input pin (`D`) is not written to the corresponding bit cell in the addressed location.

There is no loss of power or speed when the Bit Write feature is enabled. However, power will be reduced by disabling writes using these pins.


#### CEN-Gating

XYZ memory compilers optionally support the Chip Enable Gating feature.

By default, the address `A` pins and data input `D` pins are not gated by the `CEN` pin may increase toggle power. In this case, `CEN` requires a relatively small setup time.

To reduce the toggle power of the address `A` pins and data input `D` pins, users can enable the `CEN-Gating feature`; however, the setup time of CEN may increase.


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



![Column Redundancy Replace Mechanism](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\Column_Redundancy_replace_mechanism.png)

Figure show an example of the column redundancy replace mechanism in a 8 bits column Mux memory instance. In the case, 6th IO needs to be repaired. Once redundancy DFF chain be configured, redundancy scheme works. Q[7] receives the output of the redundant sub-array, Q[6] receives the output of Q[7], then replacement complete. The rest IO[0]~IO[5] receive the output of themselves.

One IO where defect is detected can be replaced by redundancy. All data flip-flop which used to configure redundancy logic to column redundant substitution. The redundant substitution of configure choose based on memory`s bit width of input data bus.

![Column Redundancy Waveform](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\1_Column_redundancy.png)

Figure shows the scan sequence of 1 column redundant substitution is followed by least significant bit of io address (0), then io address increasing until most significant bit of io address (N-2) is captured, and finally redundancy enable signal (N-1) is the last signal of scan sequence.








#### Self Time Bypass

Memory compilers support the Self Time Bypass mode.

In this mode (T\_ICLKBYP=1), the memory’s internal self-timing loop is breakdown, and memory operation timing is controled by external CLK. It’s for memory debug purpose.


#### Timing Margin Control

Memory compilers provide the Timing Margin Control feature.

The read and write operation time of SRAM is controlled by Timing Margin.The read operation process of differential SRAM is as follows:

- The word line transitions to a high voltage level, and the bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down the corresponding bit line through the transmission gate, creating a small voltage difference.
- The differential sense amplifier is activated to amplify this voltage difference to the full-scale voltage difference.

The write operation process of differential SRAM is as follows:

- The word line is activated, and the input data is driven to the bit line pair, maintaining logic 0 and 1 respectively.
- The bit line of logic 0 pulls down the memory storage node of the bitcell through the transmission gate.
- The storage node changes logic 1 to logic 0 through the cross-couple structure.

Both read and write operations in SRAM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of SRAM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, SRAM bitcell exhibits varying variability, leading to distinct characteristics in its read and write capabilities. This variability can be mitigated by extending the duration of read and write operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed.

Memory compiler controls the operating frequency of the compiler and the robustness of SRAM read and write operations through  `Timing Margin Control`.

+---------------+--------------------------------------------------------------+
| Timing Mode   | Description                                                  |
+===============+==============================================================+
| DEFAULT       | Recommended for operation at (VDD nom) ± 10% Nominal Voltage |
+---------------+--------------------------------------------------------------+

Table: Timing Mode Settings

Memory compiler provides the enable signal through the `TME` pin. The `TME` pin allows for the selection between internal default margin control and external margin control. When `TME` is low, the instance uses the default self-timing control.

There are `Timing Margin Control` bus pins available in the memory compiler. `TM` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `TM` pins, including `TME`, is provided for debug and yield analysis purposes. 

When `TME` is high, instance margin could be adjusted by the Timing input pins. 
The margin sequentially increases as `TM` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Timing Margin Control` settings are user-adjustable. The user-side `TM` interface is uniformly encoded, ensuring that all compilers have the same default `TM` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

+----------------+-------+-------------------+
| Periphery_Vt   | Mux   | Default TM[3:0]   |
+================+=======+===================+
| LVT            | 4     | 0011              |
+----------------+-------+-------------------+
| LVT            | 8     | 0011              |
+----------------+-------+-------------------+
| LVT            | 16    | 0011              |
+----------------+-------+-------------------+
| ULVT           | 4     | 0011              |
+----------------+-------+-------------------+
| ULVT           | 8     | 0011              |
+----------------+-------+-------------------+
| ULVT           | 16    | 0011              |
+----------------+-------+-------------------+

Table: Default TM Bus Settings

> Note: For additional characterization data of TM settings, users can contact the Support Team.









## Compiler Profile




### Specifications

The specifications of High Speed Single Port SRAM Compiler.

#### Pin Description






+--------------+--------------------+------------------------------------------------------------------------+
| Signal       | Enabled            | Description                                                            |
+==============+====================+========================================================================+
| A [m-1:0]    | Always             | Address input.                                                         |
+--------------+--------------------+------------------------------------------------------------------------+
| D [n-1:0]    | Always             | Data input.                                                            |
+--------------+--------------------+------------------------------------------------------------------------+
| BWEN [n-1:0] | Bit Write feature  | Bit Write Enable. Bit Write is enabled when BWEN is Logic Low. When    |
|              |                    | the Bit Write feature is included,  write operation can be performed   |
|              |                    | by enabled I/Os bits.                                                  |
+--------------+--------------------+------------------------------------------------------------------------+
| WEN          | Always             | Global Write Enable input. The memory is in the Write cycle when the   |
|              |                    | Global Write Enable input is Logic Low; the memory is in the Read      |
|              |                    | cycle when it is Logic High.                                           |
+--------------+--------------------+------------------------------------------------------------------------+
| CEN          | Always             | Chip Enable input. The memory is enabled and can perform read/write    |
|              |                    | operations when CEN is Logic Low; the memory is disabled when it is    |
|              |                    | Logic High.                                                            |
+--------------+--------------------+------------------------------------------------------------------------+
| CLK          | Always             | External Clock input.                                                  |
+--------------+--------------------+------------------------------------------------------------------------+
| FRSIN        | Redundancy feature | Faulty Repair Register Scan Input.  Redundancy Scan input bit.         |
+--------------+--------------------+------------------------------------------------------------------------+
| FRSE         | Redundancy feature | Faulty Repair Register Scan Enable Input.  Redundancy Scanning enable, |
|              |                    | active high.                                                           |
+--------------+--------------------+------------------------------------------------------------------------+
| FRSRST       | Redundancy feature | Faulty Repair Register Scan Asynchronous Reset Input. Before memory    |
|              |                    | normal access,  FRSRST must be performed a high to low(negative edge)  |
|              |                    | control signal.                                                        |
+--------------+--------------------+------------------------------------------------------------------------+
| FRSCLK       | Redundancy feature | Faulty Repair Register Scan Clock.                                     |
+--------------+--------------------+------------------------------------------------------------------------+
| T_ICLKBYP    | Self Time Bypass   | This pin must be controlled by software/firmware in silicon.  \        |
|              | feature            | In this mode (T_ICLKBYP=1), the memory’s internal self-timing loop is  |
|              |                    | breakdown, and memory operation timing is controled by external CLK.   |
|              |                    | It’s for memory debug purpose.                                         |
+--------------+--------------------+------------------------------------------------------------------------+
| TME          | Always             | This pin must be controlled by software/firmware in silicon. \         |
|              |                    | Timing Margin Control Enable input.\                                   |
|              |                    | TME = 0, select the default Timing Margin Control setting; \           |
|              |                    | TME = 1, select the external Timing Margin Control pin setting.        |
+--------------+--------------------+------------------------------------------------------------------------+
| TM[3:0]      | Always             | This pin must be controlled by software/firmware in silicon.  \        |
|              |                    | Timing Margin Control Input bus. \                                     |
|              |                    | The setting of TM[3:0] controls the Tcq and Tcyc value of memory. \    |
|              |                    | TM[3:0] = 4’b0000 is the slowest operating mode.                       |
+--------------+--------------------+------------------------------------------------------------------------+
| LS           | Always             | Light Sleep Mode Contorl Input. When the memory is disabled and this   |
|              |                    | pin is set logic High, the memory enters low leakage mode. The output  |
|              |                    | state remains unchanged.                                               |
+--------------+--------------------+------------------------------------------------------------------------+
| DS           | Power Gating       | Deep Sleep Mode Control Input. This pin turns off the periphery power  |
|              | feature            | supply while retaining the memory contents. The outputs of the memory  |
|              |                    | are pulled low.                                                        |
+--------------+--------------------+------------------------------------------------------------------------+
| SD           | Power Gating       | Shut Down Mode Contorl Input. This pin turns off the power supply to   |
|              | feature            | the periphery and memory core, and does not retain the memory data.    |
+--------------+--------------------+------------------------------------------------------------------------+

Table: Input Pin Description






+-----------+----------------------+----------------------------------------------------------------------+
| Signal    | Enabled              | Description                                                          |
+===========+======================+======================================================================+
| Q [n-1:0] | always               | Data Output bus.                                                     |
+-----------+----------------------+----------------------------------------------------------------------+
| FRSOUT    | Redundancy feature   | Faulty Repair Register Scan Output. It is used to output the Faulty  |
|           |                      | Repair Register Scan bit. When the Power Gating feature mode is      |
|           |                      | selected, its content will be lost if the power supply of the        |
|           |                      | periphery is turned off.                                             |
+-----------+----------------------+----------------------------------------------------------------------+
| PUR       | Power Gating feature | “Power Up Ready” pin is used to reduce the peak power during wake-up |
|           |                      | from DS and SD modes when instances are cascaded. When memory is in  |
|           |                      | operation, this flag pin must be high.                               |
+-----------+----------------------+----------------------------------------------------------------------+

Table: Output Pin Description




> Note: In the table above, `m` represents the maximum number of addresses supported by the compiler, and `n` represents the maximum number of bits supported by the compiler.



#### Compiler Range Information







+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| Column\   | Bank   | Word\   |   Word\ |   Word\ |   Bit\ |   Bit\ |   Bit\ | Maximum\   |
| Mux       |        | Step    |     Min |     Max |   Step |    Min |    Max | Density    |
+===========+========+=========+=========+=========+========+========+========+============+
| 4         | 1      | 16      |      32 |    1024 |      1 |      8 |    320 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 4         | 2      | 16      |      64 |    2048 |      1 |      8 |    320 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 4         | 4      | 16      |     128 |    4096 |      1 |      8 |    320 | 1280Kb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 8         | 1      | 32      |      64 |    2048 |      1 |      8 |    160 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 8         | 2      | 32      |     128 |    4096 |      1 |      8 |    160 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 8         | 4      | 32      |     256 |    8192 |      1 |      8 |    160 | 1280Kb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 1      | 64      |     128 |    4096 |      1 |      8 |     80 | 320Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 2      | 64      |     256 |    8192 |      1 |      8 |     80 | 640Kb      |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+
| 16        | 4      | 64      |     512 |   16384 |      1 |      8 |     80 | 1280Kb     |
+-----------+--------+---------+---------+---------+--------+--------+--------+------------+

Table: Compiler Range








#### Logic Truth Tables

##### Memory Function Truth Table

> Note: In the above truth table, the state of test signals is `T_ICLKBYP=L`.\
>      Before starting normal memory operation (read/write), a `Negedge(1->0)` must be performed on `FRSRST` first.\
>       `NCM`: Memory bit-cell contents remain unchanged.\
>       `Q-1`: Maintains the state of the previous cycle.\
>       `Q`: Output without `CLK` latency.

The following table shows the memory function truth table for this compiler.



+------------+-------+-------+-------+--------+---------+-----+------------+
| Function   | CLK   | CEN   | WEN   | BWEN   | D       | Q   | Memory\    |
|            |       |       |       |        |         |     | Contents   |
+============+=======+=======+=======+========+=========+=====+============+
| Idle       | L     | X     | X     | X      | X       | Q-1 | NCM        |
+------------+-------+-------+-------+--------+---------+-----+------------+
| Disabled   | H     | H     | X     | X      | X       | Q-1 | NCM        |
+------------+-------+-------+-------+--------+---------+-----+------------+
| Read       | H     | L     | H     | X      | X       | Q   | NCM        |
+------------+-------+-------+-------+--------+---------+-----+------------+
| Write      | H     | L     | L     | L      | Data-in | Q-1 | Data-in    |
+------------+-------+-------+-------+--------+---------+-----+------------+
| Write Mask | H     | L     | L     | H      | X       | Q-1 | NCM        |
+------------+-------+-------+-------+--------+---------+-----+------------+

Table: Memory Function Truth Table


##### Power Mode Truth Table

The following table shows the truth table for Power mode.

> Note: This function is valid when the `Power Gating feature` is selected.\
>       In Periphery Off modes, the Periphery supply `VDD` is allowed to be powered down.\
>       `Q-1` = Memory output maintains the state of the previous cycle.



+-------------+-------+------+------+------+-------+-----+----------------------+
| Mode        | CEN   | LS   | DS   | SD   |   PUR | Q   | Comments             |
+=============+=======+======+======+======+=======+=====+======================+
| Normal      | 0/1   | 0    | 0    | 0    |     1 | Q-1 | Normal mode          |
+-------------+-------+------+------+------+-------+-----+----------------------+
| Light Sleep | 0/1   | 1    | 0    | 0    |     1 | Q-1 | Xdec power gate,\    |
|             |       |      |      |      |       |     | Bitline Discharge    |
+-------------+-------+------+------+------+-------+-----+----------------------+
| Deep Sleep\ | X     | X    | 0->1 | 0    |     0 | 0   | Periphery shutdown   |
|  enable     |       |      |      |      |       |     |                      |
+-------------+-------+------+------+------+-------+-----+----------------------+
| Deep Sleep\ | X     | X    | 1->0 | 0    |     1 | X   | Periphery wakeup     |
|  disable    |       |      |      |      |       |     |                      |
+-------------+-------+------+------+------+-------+-----+----------------------+
| Shut Down\  | X     | X    | X    | 0->1 |     0 | 0   | Periphery shutdown,\ |
|  enable     |       |      |      |      |       |     | array shutdown       |
+-------------+-------+------+------+------+-------+-----+----------------------+
| Shut Down\  | X     | X    | X    | 1->0 |     1 | X   | Periphery wakeup,\   |
|  disable    |       |      |      |      |       |     | array wakeup         |
+-------------+-------+------+------+------+-------+-----+----------------------+

Table: Power Mode Truth Table



##### Redundancy Scan Mode Truth Table

The following table shows the truth table for Redundancy Scan mode.

> Note: When `FRSCLK` is not running, please keep it at `H` or `L`.




+------------+----------+--------+-----------+-------+----------+----------+
| Function   | FRSCLK   | FRSE   | FRSIN     | CEN   | FRSRST   | FRSOUT   |
+============+==========+========+===========+=======+==========+==========+
| Disable    | X        | X      | X         | H     | L        | X        |
+------------+----------+--------+-----------+-------+----------+----------+
| Normal     | X        | L      | X         | L     | L        | X        |
+------------+----------+--------+-----------+-------+----------+----------+
| Scan       | L->H     | H      | Fuse_Data | X     | L        | X        |
+------------+----------+--------+-----------+-------+----------+----------+
| Reset      | X        | X      | X         | X     | H        | L        |
+------------+----------+--------+-----------+-------+----------+----------+

Table: Redundancy Scan Mode Truth Table



#### Waveform Diagrams

This section presents various timing waveforms.



>Note: If `CEN` is Low, it must be ensured that each signal meets the timing specification relative to the clock.\
>      If `CEN` is High, there is no need to meet the timing specification for each signal.\
>      This note also applies to Power Management pins such as `LS`.\
>      When `CEN=1`, `LS` can be asynchronously asserted and de-asserted.


The figure below shows the conventions used in the waveform diagrams.



![Waveform Conventions](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\waveform_conventions.png)



![Read Cycle Timing Diagram](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\read_cycle_timing_diagram.png)




![Write Cycle Timing Diagram](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\write_cycle_timing_diagram.png)



![Light Sleep Mode Work Function Diagram](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\light_sleep_mode_work_function_diagram.png)






![Deep Sleep Mode Work Function Diagram](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\deep_sleep_mode_work_function_diagram.png)




![Shut Down Mode Work Function Diagram](../Template/SC/V02/Figure\High Speed Single Port SRAM Compiler\shut_down_mode_work_function_diagram.png)




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





