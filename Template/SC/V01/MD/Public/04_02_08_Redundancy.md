#### Redundancy

[Company Name] memory compilers can generate memory instances with built-in redundancy for memory repair purposes.

When Built-In Self-Test (BIST) diagnostics determine that repair is required, the redundancy provides additional memory resources for the instance.

Redundancy is enabled via the `Redundancy feature`.

[Company Name] memory compilers include two types of redundancy: row redundancy and column redundancy. When the `Column Redundancy feature` is selected, column redundancy is enabled; when the `Row Redundancy feature` is selected, both row and column redundancy resources are provided.

The number and configuration of repair elements are determined by the compiler, as described in the table below.


Table: Repair Elements Mode


Single element of 4 columns on one side of the center block, memory compilers offer two column redundancy modes for customers to select from. For more information, please refer to "Redundancy“in this chapter.

![Column Redundancy Replace Mechanism]([Template Path]\[Compiler Name]\Column_Redundancy_replace_mechanism.png)

Figure show an example of the column redundancy replace mechanism in a 8 bits column Mux memory instance. In the case, 6th IO needs to be repaired. Once redundancy DFF chain be configured, redundancy scheme works. Q[7] receives the output of the redundant sub-array, Q[6] receives the output of Q[7], then replacement complete. The rest IO[0]~IO[5] receive the output of themselves.

One IO where defect is detected can be replaced by redundancy. All data flip-flop which used to configure redundancy logic to column redundant substitution. The redundant substitution of configure choose based on memory`s bit width of input data bus.

![Column Redundancy Waveform]([Template Path]\[Compiler Name]\1_Column_redundancy.png)

Figure shows the scan sequence of 1 column redundant substitution is followed by least significant bit of io address (0), then io address increasing until most significant bit of io address (N-2) is captured, and finally redundancy enable signal (N-1) is the last signal of scan sequence.







