#### GDSII Library Naming

[Company Name] memory `GDSII library names` start with a prefix of the form `XX_`. The prefix is formed by arranging Segment 1 through Segment 4 in Table 6-1 in sequence, for example, `SCT7HHS1PRF_`. It is applied to every cell in the `GDSII library` and ensures that there are no conflicts in `cellnames` when you combine instances from different compilers or different versions of a compiler into a design. The maximum length of a cell name in the compiler library is 32 characters so that they are compatible with industry-standard layout tools.

Compiler-generated block names can have a maximum length of 14 characters because if an instance name is 17 characters long, the total length of any generated cell name is a maximum of 32 characters.



