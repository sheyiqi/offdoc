#### Timing Library Model

[Company Name] memory compiler timing library models contain:

- Memory characterization data in a specific format
- Path delays with transition values for corresponding to slew rates and output loads
- Timing values for input pin constraints such as `setup/hold`, `period`, `width`, and `recovery`

Use the timing model files to generate `SDF` data and back-annotate the `SDF` data into the Verilog models and verify timing arcs consistency.

The following section describes the timing analysis tools that [Company Name] memory compiler supports:

##### Using .lib Models

[Company Name] `<instance_name>.lib` model contains:

- `Delay model`: Provides table lookup information for delay calculations
- `Environment conditions`: Provides various operating conditions and `k-factors` for circuit timing evaluation.
- `Lookup table`: Describes timing information for:
-   ❑ Describing delays
-   ❑ Specifying constraints

[Company Name] `.lib` model:

- Provides library information including cell timing function, physical, power, test data for optimized tools performance while meeting the technology requirements.
- Makes the library development process faster through simplified data entry.
- Provides low cost library maintenance by using a single library source while minimizing library generation and verification costs.
- Offers comprehensive modeling capabilities for design flows.
- Develops high quality library that produces better designs.
- Offers a reliable, and low-cost, library development solution that is available and ready to use today.