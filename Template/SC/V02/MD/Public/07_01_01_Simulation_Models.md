#### Simulation Models

The following sections describe the simulation models that [Company Name] supports:


##### Verilog Behavioral Model

`<instance_name>.v` describes the logic in different modes with every possible transition of every pin along with X handling and full timing. Full timing modeling includes all path delays and input pin constraints like `setup`, `hold`, `recovery`, `width`, and `period`.


Verilog Compiler Directives: The Verilog model `<instance_name>.v` supports following compiler directives to provide flexibility and
extra features to the customers.

- `POWER_PINS`: Declares the power pins (`VDD`, `VDDC`, `VSS`).
- `verifault`: Enables `suppress_faults` and `enable_portfaults`, so that faults are injected only at ports.
- `PreSim`: Adds a 0.001 ns delay after the rising edge of the clock during read and write operations to prevent simulation errors caused by multiple signals switching on the same edge in certain cases.
- `NO_WARNING`: Suppresses warning and error messages.
- `INITIALIZE_MEM`: Initializes the values of the internal memory.
- `MEMFAULTNJ`: Enables repair fault injection. This option must be enabled for fault-injection testing.
- `TIMING_ANNOTATE`: Enables timing values in the `SPECIFY` module to simulate timing back-annotation in post-layout simulation.

> Note: For detailed information about Verilog simulation, contact the [Company Name] Support Team.

##### Fast Functional Verilog Model

This is a Verilog model with limited functionality to speed up the simulation time. This model supports limited functionality only and does not contain any timing information.

