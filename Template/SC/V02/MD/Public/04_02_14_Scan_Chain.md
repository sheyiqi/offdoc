#### Scan Chain

[Company Name] memory compilers provide built-in Scan Chain functionality.

In SRAM design, the scan chain is a structure used to enhance testability. Its core function is to replace key registers (such as address latches, data input/output registers, read/write enable control registers, etc.) in the SRAM peripheral circuit with flip-flops with scan functionality, and connect them in series to form several shift register chains.

In test mode, the scan chain allows test equipment to shift arbitrary test stimuli into these registers through serial input, while simultaneously shifting out the state of internal nodes for observation beat by beat. This enables the peripheral combinational logic (such as decoders, write drivers, sense amplifier paths, and interface timing logic), which is otherwise difficult to control and observe directly, to have high controllability and observability. It can effectively detect defects such as stuck-at faults and toggle delay faults introduced during the manufacturing process.

It should be noted that the [Company Name] memory compiler inserts scan chains for SRAM instances at the cost of minimal area and adapts to third-party DFT design components.

The primary function of the scan chain is to complement the peripheral logic that cannot be fully tested by MBIST. Only through the collaborative effort of the two can comprehensive fault coverage be achieved for the entire SRAM, from the storage array to the interface logic, thereby ensuring chip yield and reliability.

The Scan Chain function of [Company Name]'s memory compiler provides multiple DFF Chains:

- Input data trigger chain
- Output data trigger chain: Valid only when Mbist function is selected.
- Address/read-write enable/chip select enable flip-flop chain: If the memory is single-ported, then the memory only has one flip-flop chain. If the memory is multi-ported, then each port has one flip-flop chain.

> Note: The Scan Chain feature is only available when Bist Mux is selected by the user.



