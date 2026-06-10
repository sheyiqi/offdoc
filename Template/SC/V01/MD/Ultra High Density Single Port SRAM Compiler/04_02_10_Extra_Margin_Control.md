#### Extra Margin Control

[Company Name] memory compilers provide the Extra Margin Control feature.

The read and write operation time of SRAM is controlled by Extra Margin.
The read operation process of differential SRAM is as follows:

- The word line transitions to a high voltage level, and the bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down the corresponding bit line through the transmission gate, creating a small voltage difference.
- The differential sense amplifier is activated to amplify this voltage difference to the full-scale voltage difference.

The write operation process of differential SRAM is as follows:

- The word line is activated, and the input data is driven to the bit line pair, maintaining logic 0 and 1 respectively.
- The bit line of logic 0 pulls down the memory storage node of the bitcell through the transmission gate.
- The storage node changes logic 1 to logic 0 through the cross-couple structure

Both read and write operations in SRAM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of SRAM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, SRAM bitcell exhibits varying variability, leading to distinct characteristics in its read and write capabilities. This variability can be mitigated by extending the duration of read and write operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed

The [Company Name] memory compiler controls the operating frequency of the compiler and the robustness of SRAM read and write operations through `Extra Margin Control`.

Table: Timing Mode Settings

[Company Name] memory compiler provides the enable signal through the `TME` pin. The `TME` pin allows for the selection between internal default margin control and external margin control. When `TME` is low, the instance uses the default self-timing control.

There are `Extra Margin Control` bus pins available in the memory compiler. `TM` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `TM` pins, including `TME`, is provided for debug and yield analysis purposes. 

When `TME` is high, instance margin could be adjusted by the extra input pins. 
The margin sequentially increases as `TM` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Extra Margin Control` settings are user-adjustable. The user-side `TM` interface is uniformly encoded, ensuring that all compilers have the same default `TM` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

Table: Default TM Bus Settings

> Note: For additional characterization data of TM settings, users can contact the [Company Name] Support Team.








