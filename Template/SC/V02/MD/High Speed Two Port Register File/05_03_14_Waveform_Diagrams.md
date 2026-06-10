#### Waveform Diagrams

This section presents various timing waveforms.



>Note: If `CEN` is Low, it must be ensured that each signal meets the timing specification relative to the clock.\
>      If `CEN` is High, there is no need to meet the timing specification for each signal.\
>      This note also applies to Power Management pins such as `LS`.\
>      When `CEN=1`, `LS` can be asynchronously asserted and de-asserted.


The figure below shows the conventions used in the waveform diagrams.



![Waveform Conventions]([Template Path]\[Compiler Name]\waveform_conventions.png)



![Read Cycle Timing Diagram]([Template Path]\[Compiler Name]\read_cycle_timing_diagram.png)




![Write Cycle Timing Diagram]([Template Path]\[Compiler Name]\write_cycle_timing_diagram.png)



![Light Sleep Mode Work Function Diagram]([Template Path]\[Compiler Name]\light_sleep_mode_work_function_diagram.png)






![Deep Sleep Mode Work Function Diagram]([Template Path]\[Compiler Name]\deep_sleep_mode_work_function_diagram.png)




![Shut Down Mode Work Function Diagram]([Template Path]\[Compiler Name]\shut_down_mode_work_function_diagram.png)



