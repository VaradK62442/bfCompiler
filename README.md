# bfCompiler
A compiler for bf (BrainF**k) written in Python.

bf is an esoteric programming language that uses a theoretical infinites array of cells, all with a value of 0, and a pointer to execute code.

there are only 8 characters that it can recognize:

\> (moves the pointer forward one cell)

< (moves the pointer back one cell)

\+ (increments the cell value)

\- (decrements the cell value)

. (outputs the current cell value using ASCII)

, (takes a one character input)

\[ (starts a loop)

] (ends the loop if the pointer value is 0, otherwise goes to start of loop)


{This compiler is not 100% working correctly, will fix soon}
