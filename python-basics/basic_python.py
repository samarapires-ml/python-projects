# This file has basic python codr for learning and practice 

# Downloading python
""" Downloading python : python can be downloaded from python.org. 
     We download it and then we get the python virtual machine.
     
     python virtual machine --> coverts code to byte code """

# IDE - Integrated Development Environment 
""" IDE stands for Integrated Development Environment and it is used 
    by the virtual machine to run python code. 
    Eg: VSCode, Pycharm etc """

# Hello world program in python 
# print statement is used to give output 
# text should be in " "
print("Hello World!")

# Comments in python 
""" As we already know there are 2 ways to comment in python 
1. # - single comments 
2. """ """  - this is a doc string as multiline comments are not available 
              in python we can use doc string for multiline comments 
"""

# Variables in Python
""" Variables are used in python to strore 'so called things - could be nos, text etc'
    We can choose our own variable names but its best to name it according to what it does in the code 

    Do not use these while naming variables:
    1. You cannot use numbers at the start of variables 
    2. You cannot use spaces in variables 
    3. You should not use special characters in variables
"""

# Variable naming conventions 
""" 
     3 ways to write variables in python '
     1. Camel case - samaraPires (First word starts with small letter but every new word starts with capital letter)
     2. Pascal case - SamaraPires (Every word including the first starts with capital letter)
     3. Snake case - samara_pires (no capital letters but _ between every word)
"""

# Data Types 

""" Data is stored in variables and every bit of data belongs to a specific data type
    Python has built in data types for different kinds of data

    In Numbers we have: 
    1. Integers: All the numbers excluding decimal places and fractions 
    2. Float: All decimal numbers and fraction values are Float 
    3. Complex: Numbers with real and imaginary parts are complex 
"""
# Creating a complex number in python 
z = 3 + 4j
print(z)          # (3+4j)

# Accessing real and imaginary parts
print(z.real)     # 3.0
print(z.imag)     # 4.0
print(type(z))

#Integer 
x = 2
print(x)
print(type(x))

#Float 
y = 3/7
a = 3.6
print(y)
print(a)
print(type(y))
print(type(a))

# Data types cont ..........
"""
    Strings - used to store anything in python literally anything that is possible from ur keyboard. 
    Have to use " " and what yo ustore should come within it for it to be considered as a string 
    You can use " " or ' ' and both work the same. 

    Boolean - This is the data type that always gives the value as either TRUE or FALSE. 
"""

# String example
name = "Alice"  # String (text in quotes)
print(name)     # Output: Alice
print(type(name))  # <class 'str'>

#Boolean example 
is_valid = True     # Boolean (True or False - T & F should be capital)
is_even = (4 % 2 == 0)  # Evaluates to True
print(is_valid)     # Output: True
print(type(is_even)) # <class 'bool'>

#Type checking 
"""
Type checking in Python verifies an object's data type at runtime or statically, 
helping prevent errors from mismatched types.

Main Methods
type(): Returns the exact class of an object.
isinstance(): Checks if an object is of a specific type (or subclass), more flexible than type().
"""
#Example 
b = 3 + 4j
name = "Alice"
is_valid = True

print(type(b))            # <class 'complex'>
print(isinstance(b, complex))  # True

print(type(name))         # <class 'str'>
print(isinstance(name, str))   # True

print(type(is_valid))     # <class 'bool'>

#  Understanding How Strings Work 
