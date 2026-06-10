#### Timing Margin Control

Memory compilers provide the Timing Margin Control feature.

The read operation time of ROM is controlled by Timing Margin.The read operation process of single-end ROM is as follows:

- The read bit line be precharged to logic 1.
- The word line transitions to a high voltage level, and the read bit line precharge signal is disabled.
- The internal signal of the bitcell pulls down or keep the corresponding bit line through the transmission gate, then read bit line will pulled down to logic 0 or keep logic 1.
- The single end sense amplifier is activated to drive read bit line`s voltage to output data.


Read operations in ROM require a certain amount of time to ensure their completion. In fact, there is a negative correlation between the capacity and yield of ROM, meaning that a larger capacity often indicates a lower yield.

As the capacity increases, ROM bitcell exhibits varying variability, leading to distinct characteristics in its read  capabilities. This variability can be mitigated by extending the duration of read  operations. This underscores the trade-off between memory speed and yield/reliability: a longer delay enhances read robustness but slows down the operational speed

Memory compiler controls the operating frequency of the compiler and the robustness of ROM read operations through `Timing Margin Control`.

Table: Timing Mode Settings

Memory compiler provides the enable signal through the `TMEH/TMEL` pin. The `TMEH/TMEL` pin allows for the selection between internal default margin control and external margin control. When `TMEH/TMEL` is low, the instance uses the default self-timing control.

There are `Timing Margin Control` bus pins available in the memory compiler. `TMH/TML` are used to trade-off between speed and robustness (`yield`). It is required that external access to all `TMH/TML` pins, including `TMEH/TMEL`, is provided for debug and yield analysis purposes. 

When `TMEH/TMEL` is high, instance margin could be adjusted by the Timing input pins. 
The margin sequentially increases as `TMH/TML` sequentially decrease from All 1 to All 0, but the access time and cycle time will be sequentially enlarged as the pins driven from All 1 to All 0.

The `Timing Margin Control` settings are user-adjustable. The user-side `TMH/TML` interface is uniformly encoded, ensuring that all compilers have the same default `TMH/TML` value. Users can configure the settings from the options shown in the table below according to their application requirements.    

Table: Default TM Bus Settings

> Note: For additional characterization data of TM settings, users can contact the Support Team.








