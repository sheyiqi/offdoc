#### Interface Dual Rail

[Company Name] memory compilers support the Interface Dual Rail feature.

Users can enable independent voltage rails for the `input/output interface logic` and the `internal periphery logic + array` at the instance level. Level shifters are used in the `input interface logic`. This option is controlled by setting the `Interface Dual Rail feature`. For more information, see “Standard Operating Characterization Conditions” in Chapter 2. This option allows the array to remain within the safe operating voltage range of VDD nom +/- 10%.

When the `Interface Dual Rail feature` is selected, Light Sleep mode is also supported. After the dual-rail option is enabled, Deep Sleep and Shut Down modes can be enabled independently when the `Power Gating feature` is selected. When the `Periphery Off feature` is further selected, periphery power shutoff can be enabled. For more information, see “Periphery Off” in this chapter.

