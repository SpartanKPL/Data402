# Python Fundamentals
***

## Data Types: 
***
 **NUMERIC:**  
<br>
`x = 1`  Integers _(int)_ is a whole number
<br>

`x = 1.5`  Floating points _(float)_ is a number with a decimal point  
* `x = 1e10` Floats can be scientific numbers by using 'e'
<br>

`x = 1j` Complex numbers _(complex)_ a number followed by j is a complex number  
<BR>

 **TEXT:**
 <br><br>
`x = "one"` Strings _(str)_ can be used to display characters and are defined by using either single ' ' or double " " quotes  
<BR>
**BOOLEAN**
<br>
Booleans are a datatype that represent either **True** or **False**
<br><br>
`x = True` Variables can be assigned **True** or **False** (with no quotes)

`x = 5 < 4` They can also be assigned an equation or comparison that is true or false. In this instance x is **False**  
<BR>

**SEQUENCES**  
<BR>
`x = ["apple", "banana", "cherry"]  `  
<BR>
`x = ("apple", "banana", "cherry")`  
<BR>
`x = range(5)`

**MAPPING**  
<br>
`x = {"name" : "John", "age", : 36}  `
<br>
<BR>
**BINARY**

## Variables: 
Variables work as empty containers that can store data assigned to them. 
They are <ins>case-sensitive</ins>. _X_ is **not** the same variable as _x_. They are created when they are assigned a value. 
    
`x = 1` Numbers  without speech marks  
`y = "one"` Strings in speech marks  
`z = True` Booleans without speech marks  
<br>
You can assign multiple variables in a single line:  
`x, y, z = "One", 1, True`  
<br>
And you can assign the same value to multiple variables at once:  
 `x = y = z = "One"`

Variables created inside functions are local variables and cannot be called outside the context of that function unless the **global** keyword is used.
<br>
``` python
def example_function():
    x = 1
    global y 
    y = 5
    
example_function()
print(x)
print(y)
```
In the above example, after the function is run `print(x)` would return an error as the variable 'x' does not exist. The variable 'y' was specified to be global variable and thus can be called outside the function.

## Strings: 
