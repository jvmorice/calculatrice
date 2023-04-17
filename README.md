# calculatrice
Just another calculator in Python

### Auto-remplacements to avoid SyntaxError

**Entering an opening bracket**  
If an opening bracket is entered after a digit, the multiplication sign 
is placed before the bracket.  
If an opening bracket is entered after the dot, the dot is deleted and
the multiplication sign is placed between the digit and the bracket.  
If an opening bracket is entered after a closing one, a multiplication
sign ist inserted between them.  

**Entering an closing bracket**  
If a closing bracket is entered after a dot, the dot is deleted.  
Entering of a closing bracket after an opening one or after
an operation sign is blocked.  
A closing bracket can be entered only if the number of opening brackets
does not exceed the number of closing brackets, including the
entered one.  

**Entering a number or a dot**  
The initial zero is replaced by the entered digit.  
The initial zero is saved, if the second character is a dot.  
Entering a dot after a dot is blocked.  
If a dot is entered after an operation character or an opening bracket,
a zero is inserted before it: '5*.2' -> '5*0.2'.  
If a dot is entered after a closing bracket, a multiplication sign and
a zero are inserted between the bracket and the dot: ').1' -> ')*0.1'.  
If a digit is entered after a closing bracket, a multiplication sign
is inserted between them: ')4' -> ')*4'  

**Entering an operation sign**  
The initial zero is replaced by '-'. Entering other operation signs
after the initial minus is blocked.  
The others operation signs don't replace the initial zero.  
Entering multiple operation signs in a row is blocked.  
Entering an operation sign after the dot replace the dot.  
Entering +, *, / after an opening bracket is blocked.  

**Calculation**  
A calculation is possible only if the last character of the expression is 
a digit or a closing bracket.  
If the result of the calculation is a float with a zero after the dot, it is 
converted to integer, for example '2.0' is converted to '2'.  
If a NameError, a SyntaxError or a ZeroDivisionError occurs, a message is 
displayed in the entry field.  