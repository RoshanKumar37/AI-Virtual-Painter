Arduino UNO

Programming Basics


# -----------------------------------------------------------------

1. void setup(){
	
	# It is considered as the preparation block 
	# It only runs 1 time after starting the program

}

2. void loop(){
	
	# It is considered as the execution block.
	# It runs until the program is stopped

}

3. pinMode()

# This function has two parameters
# parameter1 - pin number
# parameter2 - mode(either INPUT or OUTPUT)

"We should always use the OUTPUT mode"

4. delay()

# This function has one prameter

# Parameter - number of milliseconds

5. digitalRead() and digitalWrite()

~~digitalRead():

# Parameter1 - Pin Number
# Parameter2 - Information about the voltage

~~digitalWrite():

# Parameter1 - Pin Number
# Parameter2 - Voltage to be provided

"Voltage can be expressed as either 'HIGH(5V, 3.3V)' or 'LOW(GND, 0V)'"

# -----------------------------------------------------------------------

# Programming in Python


1. Comments # -----------------------------------------------------------

# Comments are the non-executable lines of code

# The two types of comments are:

~~1. Single Line Comment
# They start with a '#' character at the starting 

For example:
# This is a Single Line Comment

~~2. Multi Line Comment
# They are between three inverted commas ''''''

For example:
'''
This is a
multiline
comment
'''

2. Datatypes # -----------------------------------------------------------

# Datatypes are the different kinds of data that we store in a variable
# The three mostly used datatypes are:

~~1. String
# Strings are the simple statement
# They can be written in two ways either using '' or ""

For example:
"This is the first way of writing a string"
'This is the another way of writing a string'

~~2. Integers
# Integers are the combination of natural numbers, negative numbers and 0.
# They dont need any extra charaters and only need to be written as they need to be

For example:
1
10981273
0
-912386123
-6781235
etc.

~~3. Float
# Floats are the datatypes which includes decimal.
# Just like integers, they also don't need any extra characters

For example:
123.6341234
1236123.91286391263123
7891236517293.8123
-976123.1789239123

3. Variables # -----------------------------------------------------------

# Variables are the containers of the datatypes

# There syntax is:
variable = "This is a variable which has string stored as a dataType"
variable2 = 2 # This variable has integer value stored in it
variable3 = 986.5765 # This variable has float value stored in it

4. print()

# print() is one of the basic function of python which prints the stored datatype in the terminal

For example:

print("This is printed by the print function")
print(1423)

5. input()

# input() is also a function which take input from the user and stores the user input as a certain datatype in the following variable

For example:

input("Please Enter some data")

# -----------------------------------------------------------

6. Operators

# There will be 3 types of operators that we will be using for making our calculator

~~1. Arithmatic Operator

~~~~1. "+"
# we can add two types of datatypes with this arithmatic operator

For example:
var1 = "My name is "
var2 = "Roshan"
print(var1+var2)

OUTPUT:
"""
My name is Roshan
"""


For example:
num1 = 6
num2 = 10-
print(num1 + num2)

OUTPUT:
"""
16
"""

~~~~2. "-"
# This Arithmatic Operator is used to subtract two datatype

For example:
num1 = 6
num2 = 10
print(num2 - num1)

OUTPUT:
4

~~~~3. "*"
# This Arithmatic Operator is used to multiply two datatype

num1 = 12
num2 = 4
print(num2 * num1)

OUTPUT:
48

~~~~4. "/"

# This Arithmatic Operator is used to divide two datatype

num1 = 12
num2 = 4
print(num2 / num1)

OUTPUT:
3

~~2. Comparision Operator

~~~~1. == -> equal to
~~~~2. > -> greater than
~~~~3. < -> lesser than
~~~~4. >= -> greater than equal to
~~~~5. <= -> lesser that equal to
~~~~6. != -> Not equal to 

~~3. Logical Operator

~~~~1. Logical AND
# operates only if both the conditions are true

~~~~2. Logical OR
# operates when either of the conditions is true

~~~~3. Logical NOT
# operates both of the conditions are false

7. making a calculator

number1 = int(input("Enter First number"))
number2 = int(input("Enter Second number"))

operator = input("Enter the operator (+, -, *, /)")

if operator == "+" or operator == "add" or operator == "ADD":
	add, ADD = number1 + number2
	print("The sum of", number1, "and", number2, 'is: ', add, ADD)

elif operator == "-" or operator == "subtract" or operator == "SUBTRACT":
	subtract, SUBTRACT = number1 - number2
	print("The difference of", number1, "and", number2, 'is: ', subtract, SUBTRACT)

elif operator == "*" or operator == "multiply" or operator == "MULTIPLY":
	multiply, MULTIPLY= number1 + number2
	print("The product of", number1, "and", number2, 'is: ', multiply, MULTIPLY)
		
elif operator == "/" or operator == "divide" or operator == "DIVIDE":
	divide, DIVIDE = number1 + number2
	print(number1, "divided by", number2, 'is: ', divide, DIVIDE)
	

