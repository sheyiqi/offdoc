#### Redundancy

Memory compilers can generate memory instances with built-in redundancy for memory repair purposes.


Redundancy is enabled via the `Redundancy feature`.

    When the `Column Redundancy feature` is selected, column redundancy is enabled; 
    When the `Row Redundancy feature` is selected, both row and column redundancy resources are provided.



Table: Repair Elements Mode



![Column Redundancy Replace Mechanism]([Template Path]\[Compiler Name]\Column_Redundancy_replace_mechanism.png)

Figure show an example of the column redundancy replace mechanism in a 8 bits column Mux memory instance. In the case, 6th IO needs to be repaired. Once redundancy DFF chain be configured, redundancy scheme works. Q[7] receives the output of the redundant sub-array, Q[6] receives the output of Q[7], then replacement complete. The rest IO[0]~IO[5] receive the output of themselves.

One IO where defect is detected can be replaced by redundancy. All data flip-flop which used to configure redundancy logic to column redundant substitution. The redundant substitution of configure choose based on memory`s bit width of input data bus.

![Column Redundancy Waveform]([Template Path]\[Compiler Name]\1_Column_redundancy.png)

Figure shows the scan sequence of 1 column redundant substitution is followed by least significant bit of io address (0), then io address increasing until most significant bit of io address (N-2) is captured, and finally redundancy enable signal (N-1) is the last signal of scan sequence.







