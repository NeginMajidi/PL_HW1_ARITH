# PL_HW1_ARITH

An interpreter for the ARITH language, using Python

I used the code in the following link as a reference:
https://ruslanspivak.com/lsbasi-part7/

You only need to run "make". By doing so, the Makefile makes a file called arith with
a command written in it. This file, when executed as "./arith", runs the HW1.py file 
which reads an expression from input, parses it to an AST, evaluates the resulting 
AST, and writes the result to stdout.

New testcases are placed in the "tests" directory. To the best of my knowledge, these 
testcases covers all of the features needed. It also tests the new feature added to 
the language which is subtraction.