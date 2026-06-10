#### Extra Margin Control

[Company Name] memory compilers provide the Extra Margin Control feature.

The read and write operation time of SRAM is controlled by Extra Margin.
The read operation process of single-end SRAM is as follows:

- The word line transitions to a high voltage level, and the read bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down or keep the corresponding bit line through the transmission gate, then read bit line will pulled down to logic 0 or keep logic 1.
- The single end sense amplifier is activated to drive read bit line`s voltage to output data.

The write operation process of differential SRAM is as follows:
- The word line is activated, and the input data is driven to the bit line pair, maintaining logic 0 and 1 respectively.
- The bit line of logic 0 pulls down the memory storage node of the bitcell through the transmission gate.
- The storage node changes logic 1 to logic 0 through the cross-couple structure

Both read and write operations in SRAM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of SRAM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, SRAM bitcell exhibits varying variability, leading to distinct characteristics in its read and write capabilities. This variability can be mitigated by extending the duration of read and write operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed

The [Company Name] memory compiler controls the operating frequency of the compiler and the robustness of SRAM read and write operations through 'Extra Margin Control'.

Table: Timing Mode Settings

[Company Name] memory compiler provides the enable signal through the `EMCEA/EMCEB` pin. The `EMCEA/EMCEB` pin allows for the selection between internal default margin control and external margin control. When `EMCEA/EMCEB` is low, the instance uses the default self-timing control.

There are `Extra Margin Control` bus pins available in the memory compiler. `EMCA/EMCB` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `EMCA/EMCB` pins, including `EMCEA/EMCEB`, is provided for debug and yield analysis purposes. 

When `EMCEA/EMCEB` is high, instance margin could be adjusted by the extra input pins. 
The margin sequentially increases as `EMCA/EMCB` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Extra Margin Control` settings are user-adjustable. The user-side `EMCA/EMCB` interface is uniformly encoded, ensuring that all compilers have the same default `EMCA/EMCB` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

Table: Default EMC Bus Settings

> Note: For additional characterization data of EMC settings, users can contact the [Company Name] Support Team.








