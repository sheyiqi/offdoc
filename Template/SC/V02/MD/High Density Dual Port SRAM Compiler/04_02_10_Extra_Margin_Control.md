#### Timing Margin Control

 Memory compilers provide the Timing Margin Control feature.

The read and write operation time of SRAM is controlled by Timing Margin.
The read operation process of differential SRAM is as follows:

- The word line transitions to a high voltage level, and the bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down the corresponding bit line through the transmission gate, creating a small voltage difference.
- The differential sense amplifier is activated to amplify this voltage difference to the full-scale voltage difference.

The write operation process of differential SRAM is as follows:

- The word line is activated, and the input data is driven to the bit line pair, maintaining logic 0 and 1 respectively.
- The bit line of logic 0 pulls down the memory storage node of the bitcell through the transmission gate.
- The storage node changes logic 1 to logic 0 through the cross-couple structure.

Both read and write operations in SRAM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of SRAM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, SRAM bitcell exhibits varying variability, leading to distinct characteristics in its read and write capabilities. This variability can be mitigated by extending the duration of read and write operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed.

Memory compiler controls the operating frequency of the compiler and the robustness of SRAM read and write operations through `Timing Margin Control`.

Table: Timing Mode Settings

 Memory compiler provides the enable signal through the `TMEA/TMEB` pin. The `TMEA/TMEB` pin allows for the selection between internal default margin control and external margin control. When `TMEA/TMEB` is low, the instance uses the default self-timing control.

There are `Timing Margin Control` bus pins available in the memory compiler. `TMA/TMB` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `TMA/TMB` pins, including `TMEA/TMEB`, is provided for debug and yield analysis purposes. 

When `TMEA/TMEB` is high, instance margin could be adjusted by the Timing input pins. 
The margin sequentially increases as `TMA/TMB` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Timing Margin Control` settings are user-adjustable. The user-side `TMA/TMB` interface is uniformly encoded, ensuring that all compilers have the same default `TMA/TMB` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

Table: Default TM Bus Settings

> Note: For additional characterization data of TM settings, users can contact the  Support Team.








