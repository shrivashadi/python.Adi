# %% [markdown]
# # Python Basic

# %% [markdown]
# ##TQ-1:- What is Python, and why is it popular?
#          -Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.
# 
# Python is popular because:
# 
# It has a simple and easy-to-understand syntax.
# 
# It supports multiple programming paradigms like procedural, object-oriented, and functional programming.
# 
# It has a large standard library and a strong community.
# 
# It is used in many fields like web development, data science, artificial intelligence, automation, and more.
# 
# It is beginner-friendly, making it a great choice for new programmers.**bold text**

# %% [markdown]
# ##TQ2-: 2. What is an interpreter in Python?
#         -  An interpreter in Python is a program that reads and executes Python code line by line. Instead of converting the entire code into machine language at once (like a compiler), the interpreter processes each line one at a time.
#         Python uses an interpreter to run programs, which makes debugging easier and allows faster testing during development.

# %% [markdown]
# # TQ3:- What are pre-defined keywords in Python?
#         -Pre-defined keywords in Python are reserved words that have special meaning in the language. These keywords are part of the Python syntax and cannot be used as variable names, function names, or identifiers.
# 
# They are used to define the structure and flow of a Python program.
# 
# Examples of Python keywords:-if, else, elif, for, while, break, continue, def, return, import, class, True, False, None
# 
#       
#      

# %% [markdown]
# # TQ4:-Can keywords be used as variable names?
#        -No, keywords cannot be used as variable names in Python.
# 
# This is because keywords have special meanings in the language and are used to define the syntax and structure of Python code. Using them as variable names will cause a syntax error.
# 
# Example (Invalid):- number = 5  # ✅ "number" is a valid variable name
# 

# %% [markdown]
# # TQ5:- What are identifiers in Python?
#         - Identifiers are the names used to identify variables, functions, classes, modules, and other objects in Python.
# 
# They are created by the programmer and must follow certain rules:
# 
# Must start with a letter (A–Z or a–z) or an underscore _
# 
# Can be followed by letters, digits (0–9), or underscores
# 
# Cannot use Python keywords as identifiers
# 
# Are case-sensitive (Name, name, and NAME are different)
# 
# Examples of valid identifiers:- name, _age, student1, total_marks
# 
# Examples of invalid identifiers:- 1name     # starts with a digit
# class     # keyword
# total-marks  # contains a hyphen
# 

# %% [markdown]
# # TQ6:- Why are lists mutable, but tuples are immutable?
#       - Lists are mutable because they are designed to allow modification after creation. You can:
# 
# Add elements (append, extend)
# 
# Remove elements (remove, pop)
# 
# Change elements (list[0] = new_value)
# 
# Tuples are immutable because they are meant to be fixed collections of items. Once created:
# 
# You cannot change, add, or remove elements.
# 
# This makes them faster and safer (used in keys for dictionaries, etc.)

# %%
#Example:
my_list = [1, 2, 3]
my_list[0] = 100      # ✅ This works (mutable)

my_tuple = (1, 2, 3)
# my_tuple[0] = 100    ❌ This gives error (immutable)


# %% [markdown]
# #TQ7:-  What is the difference between == and is operators in Python?
#         ➤ == Operator:
# 
# Compares values of two objects.
# 
# Returns True if the data inside the objects is the same, even if they are different objects in memory.
# 
# ➤ is Operator:
# 
# Compares the identity (memory location) of two objects.
# 
# Returns True only if both variables refer to the exact same object in memory.
# 
# 

# %%
#Example
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # ✅ True → values are the same
print(a is b)  # ❌ False → different objects in memory


# %% [markdown]
# # TQ8:- What are logical operators in Python?
#        Logical operators are used to combine multiple conditions or boolean expressions. They return True or False based on logic.
# 
#    Python has 3 main logical operators:
#    | Operator | Meaning                          | Example                      |
# | -------- | -------------------------------- | ---------------------------- |
# | `and`    | True if **both** are true        | `(5 > 2 and 3 < 4)` → `True` |
# | `or`     | True if **at least one** is true | `(5 > 10 or 3 < 4)` → `True` |
# | `not`    | Reverses the condition           | `not (5 > 2)` → `False`      |
# 
#     

# %%
#Example
a = 10
b = 5

print(a > 5 and b < 10)   # True (both conditions are true)
print(a < 5 or b < 10)    # True (second condition is true)
print(not (a > b))        # False (because a > b is True, not makes it False)


# %% [markdown]
# #TQ9:- What is type casting in Python?
#        - Type casting means converting one data type into another.
# Python provides built-in functions to perform type conversions.
# 
# 🔹 Types of Type Casting:
# 1-Implicit Type Casting (automatic by Python)
# 
# 1-Explicit Type Casting (manual by the programmer)

# %%
#ample of Explicit Type Casting:
a = "123"
b = int(a)      # '123' (string) → 123 (integer)
print(b + 1)    # Output: 124

#Example of Implicit Type Casting:
x = 10
y = 2.5
z = x + y       # x (int) is automatically converted to float
print(z)        # Output: 12.5


# %% [markdown]
# #TQ10:- What is the difference between implicit and explicit type casting?
#         - Implicit Type Casting:
# Automatically done by Python interpreter.
# 
# Happens when combining different data types.
# 
# No data loss or programmer control needed
# 
#  Explicit Type Casting:-
# Done manually by the programmer.
# 
# Converts one type to another using built-in functions.
# 
# Can lead to data loss (e.g., float to int).
#        

# %%
#Example
a = "100"
b = int(a)    # string to int
print(b + 1)  # Output: 101


# %% [markdown]
# #TQ11:- What is the purpose of conditional statements in Python?
#        - Conditional statements are used to make decisions in a Python program.
# They allow the program to execute certain blocks of code only when specific conditions are met.
# 
#  Main Conditional Statements:
# if – checks a condition and executes the block if it is True.
# 
# elif – checks other conditions if the previous if was False.
# 
# else – runs when none of the above conditions are True.

# %%
#Example
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible.")


# %% [markdown]
# # TQ12:-  How does the elif statement work?
#           - It is used when you want to check multiple conditions one after another.
# 
#  Working of elif:
# Python checks conditions from top to bottom.
# 
# The first condition that is True is executed.
# 
# Once a condition is matched, the rest are skipped.

# %%
#Example
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")


# %% [markdown]
# # TQ13:- What is the difference between for and while loops?
#         - for Loop:
# Used when you know in advance how many times you want to repeat a block.
# 
# Works well with sequences like lists, strings, ranges, etc.
# 
# Example:

# %%
#Example
for i in range(5):
    print(i)


# %% [markdown]
# #TQ14:- Describe a scenario where a while loop is more suitable than a for loop?
#       - cenario: Taking input until user enters a specific value
# Imagine you want to keep asking a user for a password until they type the correct one.
# You don't know how many times the user will try — so a while loop is perfect.
# 
# Why not for loop?
# Because you don't know how many attempts the user will take — it depends on the condition, not a fixed count.
#  Real-World Use Cases of while Loop:
# Login systems
# 
# Game loops
# 
# Waiting for sensor/device signal
# 
# Repeating until valid input is given
# 

# %%
#Example
password = ""

while password != "open123":
    password = input("Enter password: ")

print("Access granted.")


# %% [markdown]
# # Python Basics Practical-

# %% [markdown]
# # PQ1:- Write a Python program to print “Hello, World!”

# %%
# PQ1: Print "Hello, World!"
print("Hello, World!")


# %% [markdown]
# #PQ2:- Write a Python program that displays your name and age.

# %%
# PQ2: Display your name and age
name = "Aditya Sen"
age = 22

print("Name:", name)
print("Age:", age)


# %% [markdown]
# #PQ3:- rite code to print all the pre-defined keywords in Python using the keyword library.

# %%
# PQ3: Print all pre-defined keywords in Python
import keyword

print("Python Keywords:")
print(keyword.kwlist)


# %% [markdown]
# #PQ4:- Write a program that checks if a given word is a Python keyword.

# %%
# PQ4: Check if a word is a Python keyword
import keyword

word = input("Enter a word to check: ")

if keyword.iskeyword(word):
    print(f"'{word}' is a Python keyword.")
else:
    print(f"'{word}' is NOT a Python keyword.")


# %% [markdown]
# #PQ5:- Create a list and tuple in Python, and demonstrate how attempting to change an element works differently for each.
# 
# 

# %%
# PQ5: List (mutable) and Tuple (immutable) example

# Creating a list and a tuple
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

# Modifying the list
print("Original list:", my_list)
my_list[0] = 100
print("Modified list:", my_list)

# Attempting to modify the tuple
print("Original tuple:", my_tuple)
try:
    my_tuple[0] = 100  # This will raise an error
except TypeError as e:
    print("Error:", e)


# %% [markdown]
# #PQ6:- Write a function to demonstrate the behavior of mutable and immutable arguments.

# %%
# PQ6: Mutable vs Immutable function behavior

# Function to modify mutable (list)
def modify_list(mylist):
    mylist.append(100)
    print("Inside function (list):", mylist)

# Function to modify immutable (integer)
def modify_integer(num):
    num += 10
    print("Inside function (int):", num)

# Main program
my_list = [1, 2, 3]
my_num = 5

modify_list(my_list)
print("Outside function (list):", my_list)   # List is modified

modify_integer(my_num)
print("Outside function (int):", my_num)     # Integer remains same


# %% [markdown]
# #PQ7:- Write a program that performs basic arithmetic operations on two user-input numbers.

# %%
# PQ7: Basic arithmetic operations

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Handling division by zero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")


# %% [markdown]
# #PQ8:- Write a program to demonstrate the use of logical operators.

# %%
# PQ8: Logical operators demo

# Taking two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Logical operations
print("Both numbers are greater than 0:", a > 0 and b > 0)
print("At least one number is even:", a % 2 == 0 or b % 2 == 0)
print("First number is NOT negative:", not (a < 0))


# %% [markdown]
# #PQ9:-  Write a Python program to convert user input into string, integer, float, and boolean types.

# %%
# PQ9: Type conversion of user input

user_input = input("Enter a value: ")

# Type conversions
as_string = str(user_input)
as_integer = int(float(user_input))  # Handles numeric strings safely
as_float = float(user_input)
as_boolean = bool(user_input)

# Display results
print("As String:", as_string)
print("As Integer:", as_integer)
print("As Float:", as_float)
print("As Boolean:", as_boolean)


# %% [markdown]
# #PQ10:- Write a program that demonstrates type casting with examples.

# %%
# PQ10: Type casting demonstration

# Original values
int_val = 10
float_val = 5.6
str_val = "123"

# Casting int to float
print("int to float:", float(int_val))

# Casting float to int
print("float to int:", int(float_val))

# Casting string to int
print("string to int:", int(str_val))

# Casting int to string
print("int to string:", str(int_val))

# Casting non-empty string to boolean
print("non-empty string to bool:", bool(str_val))

# Casting 0 to boolean
print("0 to bool:", bool(0))


# %% [markdown]
# #PQ11:- Write a Python program that uses conditional statements.

# %%
# PQ11: Conditional statement example

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
elif age > 0:
    print("You are not eligible to vote.")
else:
    print("Invalid age entered.")


# %% [markdown]
# #PQ12:- rite a loop to print numbers from 1 to 10.
# 
# 

# %%
# PQ12: Print numbers from 1 to 10 using a loop

for i in range(1, 11):
    print(i)


# %% [markdown]
# #PQ13:- Write a Python program to find the sum of all even numbers between 1 and 50.

# %%
# PQ13: Sum of even numbers from 1 to 50

even_sum = 0

for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i

print("Sum of even numbers from 1 to 50 is:", even_sum)


# %% [markdown]
# #PQ14:- Write a Python program to calculate the factorial of a number provided by the user using a while loop.

# %%
# PQ14: Factorial using while loop

num = int(input("Enter a number: "))
factorial = 1
i = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is: {factorial}")



