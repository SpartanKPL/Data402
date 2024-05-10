<img height="150" src="Python-logo.png" width="150"/>

# Python Fundamentals
***

## Data Types: 
***
### Numeric
`x = 1`  [Integers](#int1) _(int)_ is a whole number.
<br>

`x = 1.5`  [Floating points](#float1) _(float)_ is a number with a decimal point.  
* `x = 1e10` Floats can be scientific numbers by using 'e'.
<br>

`x = 1j` [Complex numbers](#complex1) _(complex)_ a number followed by j is a complex number.  
<BR>

### Text

`x = "one"` [Strings](#string1) _(str)_ can be used to display characters and are defined by using either single ' ' or double " " quotes.  
<BR>
### Boolean  

[Booleans](#boolean1) are a datatype that represent either **True** or **False**.
<br><br>
`x = True` Variables can be assigned **True** or **False** (with no quotes).

`x = 5 < 4` They can also be assigned an equation or comparison that is true or false. In this instance x is **False**. 
<BR>

### Sequences  

`x = ["apple", "banana", "cherry"]`  [Lists](#list1) are defined with square brackets and store multiple values in a single variable and are mutable.
<BR>

`x = ("apple", "banana", "cherry")` [Tuples](#tuple1) are defined by parentheses and are similar to lists but are immutable.
<BR>

### Mapping  

`x = {"name" : "John", "age" : 36}` [Dictionaries](#dictionary1) are combinations of keys and value pairs, they are mutable but do not allow duplicate keys.
<br>
<BR>

## Variables: 
***
[Variables](#variable1) work as empty containers that can store data assigned to them. 
They are <ins>case-sensitive</ins>. _X_ is **not** the same variable as _x_. They are created when they are assigned a value. 
    
`x = 1` Numbers  without speech marks  
`y = "one"` Strings in speech marks  
`z = True` Booleans without speech marks  
<br>
You can find out what datatype a variable is by using `type(x)`  
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

## Maths Operators: 
***
You can use maths operators to work out equations in python.  
<br>
`+` Addition - Basic addition of numbers `1 + 1` would return `2`  
`-` Subtraction - Basic subtraction of numbers `1 - 1` would return `0`  
`/` Division - Basic division of numbers `10 / 2` would return `5`  
`*` Multiplication - Basic addition of numbers `5 * 2` would return `10`  
`%` Modulo - Returns the remainder after dividing `10 % 3` would return `1`  
`**` Exponentiation - Raises one number to the power of another `5 ** 2` would return `25`  
`//` Floor Division - Returns the result of division **rounded down** to the nearest whole number  `21 // 2` would return `10` while `21 / 2` would return `10.5`  


## Comparison Operators:
***
Comparison operators are used to compare values in variables and return True or False based on the result.  
<br>
 
* `==` - Equal to
  + `1 == 1` would return `True`, `1 == 2` would return `False`  
<br>
* `!=` - Not equal to 
  *  `2 != 3` would return `True`, `2 != 2` would return `False`  
<br>
* `>` - Greater than
  *  `4 > 3` would return `True`, `4 > 4` would return `False`  
<br>
* `<` - Less than  
  * `5 < 6` would return `True`, `5 < 5` would return `False`  
  <br>

* `>=` - Greater than or equal to  
  * `4 >= 4` would return `True`, `3 >= 4` would return `False`  
<br>

* `<=` - Less than or equal to  
  * `5 <= 5` would return `True`, `6 <= 5` would return `False`  

## Strings: 
***

### String Indexing
You can print the letters based on their position in a string through indexing.  
<br>
_! Indexing in Python and many programming languages start from 0 not 1_
```python
text = "Hello World"

print(text[1])
>>> e 

print(text[0])
>>> H 

print(text[-1])
>>> d # Reverse indexing allows you to work from the end of a string

print(text[-0])
>>> H # There is no difference between 0 and -0 so it this still returns 0
```
### Concatenation
You can join strings together through concatenation by using `+`

```python
Text1 = "Testing"
Text2 = "testing"
Text3 = 123

print(Text1 + Text2)
>>> Testingtesting
```
You can easily add blankspaces that are not already present any of the variables as well.
```python
print(Text1 + " " + Text2)
>>> Testing testing
```
You can concatenate strings. It would result in an error if there was an attempt to combine a string and integer for example. 
This can be fixed by [casting](#casting1) the integer as a string.
```python
print(Text1 + Text2 + str(Text3))
>>> Testingtesting123
```
### String Methods

### Escape Characters

## Control Flow

### If & Else statement 
If statements are used to check a condition, they are often used alongside elif and else, but it can be used as a standalone statement.

```python
if 5 > 6 or 6 < 10:
  print("Correct")

```
Considering each of these conditions are true `Correct` will be printed out; however, if conditions that are not true were to be in the if statement there is no code stating what is supposed to happen. An Else statement can be used to produce a result if the condition in the if statement cannot be met.

```python
if 5 == 10:
  print("Correct")
else:
  print("Incorrect")
```
As 5 is not equal to 10, `Incorrect` will be printed out in this instance
### Elif Statement
The elif statement is a combination of both an if and else statement. This is used when you want to have a result when the if statement isn't met but you have more conditions that might give a result outside of an else statement.

```python
if 5 == 10:
  print("Correct")
elif 5 > 4:
  print("Correct")
else:
  print("Incorrect")
```
In this instance, `Correct` would be printed out. While 5 is not equal to 10, it is greater than 4 so the code following the elif statement is run and as the else statement cannot be reached. 

## Loops


## Glossary
<a name="int1"></a>Integer:  
<a name="float1"></a>Float:  
<a name="complex1"></a>Complex:  
<a name="string1"></a>String:  
<a name="boolean1"></a>Boolean:  
<a name="list1"></a>List:  
<a name="tuple1"></a>Tuple:  
<a name="dictionary1"></a>Dictionary:  
<a name="variable1"></a>Variable:  
<a name="casting1"></a>Casting:  
