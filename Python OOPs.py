# %% [markdown]
# #OOPs :-

# %% [markdown]
# #TQ1:-  What is Object-Oriented Programming (OOP)?
#       - Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects, which are instances of classes. It focuses on encapsulating data and behavior together, promoting modularity, code reuse, and scalability.
# 
# Key principles of OOP include:
# 
# 1-Encapsulation – hiding internal details and showing only relevant features.
# 
# 2-Abstraction – exposing only essential functionalities.
# 
# 3-Inheritance – deriving new classes from existing ones.
# 
# 4-Polymorphism – using a common interface to operate on different data types or classes.
# 
# Python supports OOP and allows developers to create reusable, maintainable, and scalable code using classes and objects.

# %% [markdown]
# #TQ2:- What is a class in OOP?
#       - A class in Object-Oriented Programming is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that the objects created from the class will have.
# 
# In Python, a class is defined using the class keyword:

# %%
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")


# %% [markdown]
# #TQ3:- What is an object in OOP?
#       - An object is an instance of a class in Object-Oriented Programming. It represents a real-world entity with state (attributes) and behavior (methods).
# 
# Once a class is defined, you can create objects from it. Each object has its own unique values for the attributes defined in the class.
# 
# Example:
#      

# %%
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.drive()   # Output: The Toyota Corolla is driving.
car2.drive()   # Output: The Honda Civic is driving.


# %% [markdown]
# #tq4:- What is the difference between abstraction and encapsulation?
#        - Feature	Abstraction	Encapsulation
# Definition	Hiding implementation details and showing only essential features.	Wrapping data and methods into a single unit (class) and restricting direct access.
# Focus	Focuses on what an object does.	Focuses on how to protect the data.
# Purpose	Simplifies complexity by hiding unnecessary details.	Safeguards internal object state from unintended modification.
# How achieved	Using abstract classes or interfaces.	Using private/public modifiers and methods (getters/setters).
# Example	Abstract method area() in base class Shape.	Private attribute __balance in BankAccount class.

# %% [markdown]
# #TQ5:- What are dunder methods in Python?
#       - Dunder methods (short for “double underscore methods”) are special methods in Python that have double underscores at the beginning and end of their names, like __init__, __str__, __len__, etc. They are also called magic methods.
# 
# These methods allow you to define how objects of your class behave with built-in Python operations, such as object creation, string representation, arithmetic operations, etc.
# 
# Common examples:
# 
# __init__(self, ...) → Constructor (initializes object)
# 
# __str__(self) → String representation using print()
# 
# __len__(self) → Returns the length when len(obj) is called
# 
# __add__(self, other) → Defines behavior of + operator
# 
# __eq__(self, other) → Defines behavior of == operator

# %%
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python OOP")
print(b)  # Output: Book: Python OOP


# %% [markdown]
# #TQ6:- Explain the concept of inheritance in OOP.
#       - Inheritance is an important feature of Object-Oriented Programming that allows a class (child/derived class) to inherit properties and behaviors (methods and attributes) from another class (parent/base class).
# 
# It promotes code reusability, reduces redundancy, and allows the creation of hierarchical class relationships.
# 
# Types of Inheritance in Python:
# Single inheritance – One child inherits from one parent.
# 
# Multiple inheritance – Child class inherits from multiple parents.
# 
# Multilevel inheritance – A class inherits from a child class which itself inherits from another class.
# 
# Hierarchical inheritance – Multiple child classes inherit from a single parent.

# %%
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog


# %% [markdown]
# #TQ7: What is polymorphism in OOP?
#      - Polymorphism in Object-Oriented Programming means "many forms". It allows the same method or operation to behave differently depending on the context or the object on which it is called.
# 
# In Python, polymorphism is commonly achieved through:
# 
# Method Overriding – Subclass provides a specific implementation of a method defined in the parent class.
# 
# Duck Typing – Python allows any object that has the required method to be used, regardless of its actual class.

# %%
#Example 1: Polymorphism through method overriding
class Bird:
    def fly(self):
        print("Some birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high.")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly.")

for bird in [Sparrow(), Penguin()]:
    bird.fly()

#Example 2: Duck Typing
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())



# %% [markdown]
# #TQ8:- How is encapsulation achieved in Python?
#       -Encapsulation is the concept of hiding internal object details and exposing only necessary parts through methods. It helps in protecting data from direct modification and maintaining control over how it's accessed or changed.
# 
# In Python, encapsulation is achieved using:
# 
# Public Members – Accessible from anywhere.
# → No underscore (e.g., self.name)
# 
# Protected Members – Meant for internal use, accessible in subclasses.
# → Single underscore prefix (e.g., _balance)
# 
# Private Members – Not directly accessible from outside the class.
# → Double underscore prefix (e.g., __password)
# 
# 

# %%
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # Public
        self._balance = balance       # Protected
        self.__password = "1234"      # Private

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Aditya", 1000)
print(account.get_balance())  # ✅ OK
print(account._balance)       # ⚠️ Not recommended
# print(account.__password)   # ❌ Error: private attribute


# %% [markdown]
# #TQ9:- What is a constructor in Python?
#       -A constructor in Python is a special method used to initialize objects when they are created from a class. It is defined using the __init__() method.
# 
# This method is automatically called whenever a new object is created, and it allows you to set initial values for the object’s attributes.
#  syntax:- class ClassName:
#     def __init__(self, parameters):
#         initialization code
# 

# %%
#Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Aditya", 22)
print(p1.name)  # Output: Aditya
print(p1.age)   # Output: 22


# %% [markdown]
# #TQ10:- What are class and static methods in Python?
#       - Python provides two types of methods that are not tied to object instances:
# 
# 1. Class Method (@classmethod)
# Works with the class itself, not an object.
# 
# Takes cls as the first argument (not self).
# 
# Used to access or modify class-level data.
# 2. Static Method (@staticmethod)
# Does not take self or cls.
# 
# Acts like a regular function placed inside a class.
# 
# Used when method logic doesn't need access to class or instance data.
# 
# | Method Type     | Decorator       | First Parameter | Accesses Class/Instance Data? |
# | --------------- | --------------- | --------------- | ----------------------------- |
# | Instance Method | None            | `self`          | Yes                           |
# | Class Method    | `@classmethod`  | `cls`           | Yes (class data)              |
# | Static Method   | `@staticmethod` | None            | No                            |
# 

# %%
#Example-1
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Person.get_count())  # Output: 0
p1 = Person("Amit")
print(Person.get_count())  # Output: 1

#Example-2
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 5))  # Output: 8


# %% [markdown]
# #TQ11: What is method overloading in Python?
#        -Method Overloading is the ability to define multiple methods with the same name but different parameters (number or type). While many languages support true method overloading, Python does not support it directly.
# 
# Instead, Python handles overloading by using default arguments or variable-length arguments (*args, **kwargs) in a single method definition.**bold text**

# %%
#Simulating Method Overloading in Python:
class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return "Insufficient arguments"

calc = Calculator()
print(calc.add(2, 3))        # Output: 5
print(calc.add(1, 2, 3))     # Output: 6



# %% [markdown]
# #TQ12:- What is method overriding in OOP?
#        - Method Overriding is an OOP concept where a child (derived) class provides a specific implementation of a method that is already defined in its parent (base) class.
# 
# It is used to modify or extend the behavior of an inherited method.
# 
# 🔹 Key Points:
# Method name and parameters must be the same as in the parent class.
# 
# The child class's version overrides the parent's version.
# 
# Enables runtime polymorphism.

# %%
# Example:
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks


# %% [markdown]
# #TQ13:- What is a property decorator in Python?
#        -The @property decorator in Python is used to define a method as a property, so it can be accessed like an attribute. It allows you to encapsulate instance variables and provide controlled access to them.
# 
# 🔹 Why use @property?
# To make a method look like an attribute.
# 
# To add logic when getting, setting, or deleting an attribute.
# 
# To use getter, setter, and deleter functionalities cleanly.**bold text**

# %%
#Example
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        self._name = value

s = Student("Aditya")
print(s.name)      # Access like an attribute → "Getting name..." → "Aditya"
s.name = "Rahul"   # Set like an attribute → "Setting name..."


# %% [markdown]
# #TQ14:- Why is polymorphism important in OOP?
#        Polymorphism is important in Object-Oriented Programming because it allows objects of different classes to be treated as objects of a common base class, enabling flexibility, code reusability, and scalability.
# 
# 🔹 Key Benefits of Polymorphism:
# Code Reusability
# 
# Same interface can be used for different underlying forms (data types or classes).
# 
# No need to write duplicate code for each subclass.
# 
# Flexibility & Extensibility
# 
# You can change or extend the behavior of methods in subclasses without modifying the base class.
# 
# Cleaner Code
# 
# Simplifies function logic using a common method name, even if implementation differs across classes.
# 
# Supports Dynamic Method Binding (Runtime Polymorphism)
# 
# The method that gets called is determined at runtime based on the object’s type.

# %%
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()

make_sound(Dog())  # Output: Dog barks
make_sound(Cat())  # Output: Cat meows


# %% [markdown]
# #TQ15:- What is an abstract class in Python?
#       - An abstract class in Python is a class that cannot be instantiated directly and is meant to be inherited by other classes. It can contain abstract methods, which are methods without implementation, forcing subclasses to provide their own versions.
# 
# Python provides abstract class support through the abc module (abc stands for Abstract Base Classes).
# 
# 🔹 Key Features:
# Defined using the ABC class from the abc module.
# 
# Abstract methods are marked with the @abstractmethod decorator.
# 
# Cannot create objects of an abstract class.
# 
# Ensures that derived classes implement certain methods.**bold text**
# 
# 

# %%
#Example
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

# shape = Shape()  ❌ Error: can't instantiate abstract class
circle = Circle()
print(circle.area())  # Output: 78.5


# %% [markdown]
# #TQ16:- What are the advantages of OOP?
#       - Object-Oriented Programming (OOP) offers several advantages that make it a powerful and widely used programming paradigm.
#        Key Advantages of OOP:
# Modularity
# 
# Code is organized into separate classes, making it easier to manage and understand.
# 
# Reusability
# 
# Existing classes can be reused via inheritance without rewriting code.
# 
# Encapsulation
# 
# Data and methods are bundled together, protecting the internal state of objects and allowing controlled access.
# 
# Polymorphism
# 
# Same method name can be used for different types of objects, making code more flexible and general.
# 
# Inheritance
# 
# Enables creating hierarchies of classes and building on top of existing code.
# 
# Scalability & Maintainability
# 
# Large codebases become easier to extend and maintain by updating only relevant classes.
# 
# Improved Collaboration
# 
# OOP supports a clear structure that helps teams work collaboratively, focusing on different classes or modules.
# 
# Real-World Modeling
# 
# OOP allows you to model real-world entities more naturally using objects and classes.
# 
# 

# %% [markdown]
# #TQ17:- What is the difference between a class variable and an instance variable?
#       - | Feature            | **Class Variable**                                | **Instance Variable**                             |
# | ------------------ | ------------------------------------------------- | ------------------------------------------------- |
# | **Scope**          | Shared across **all instances** of the class      | Unique to **each object (instance)**              |
# | **Defined**        | Inside the class, **outside any method**          | Inside a method (usually `__init__`) using `self` |
# | **Accessed using** | `ClassName.variable_name` or `self.variable_name` | Only through `self.variable_name`                 |
# | **Purpose**        | To store common data for all objects              | To store data unique to each object               |
# 

# %%
class Student:
    school_name = "ABC School"  # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable

s1 = Student("Aditya")
s2 = Student("Rahul")

print(s1.school_name)   # Output: ABC School (shared)
print(s2.name)          # Output: Rahul (unique)


# %% [markdown]
# #TQ18: What is multiple inheritance in Python?
#       - Multiple Inheritance is a feature in Python where a child class inherits from more than one parent class. This allows the child class to access attributes and methods of all its parent classes.bold text

# %%
#Example
class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Programming")

c = Child()
c.skills()


# %% [markdown]
# #TQ19:- Explain the purpose of __str__ and __repr__ methods in Python.
#        -The __str__ and __repr__ methods in Python are special (dunder) methods used to define string representations of an object.
# 
# 🔹 __str__ Method:
# Called by the built-in str() function or print().
# 
# Used to return a user-friendly, readable string.
# 
# 🔹 __repr__ Method:
# Called by the built-in repr() function or in interactive mode.
# 
# Used to return an unambiguous, developer-focused string that ideally can be used to recreate the object.
# - summary: | Method     | Purpose                         | Called by             |
# | ---------- | ------------------------------- | --------------------- |
# | `__str__`  | User-friendly output            | `print()`, `str()`    |
# | `__repr__` | Developer-friendly, unambiguous | `repr()`, interpreter |
# 
#      

# %%
#Example
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

b = Book("Python 101", "Aditya")
print(str(b))    # Output: Python 101 by Aditya
print(repr(b))   # Output: Book('Python 101', 'Aditya')


# %% [markdown]
# #TQ20:- What is the significance of the super() function in Python?
#        - The super() function in Python is used to call methods of a parent (or superclass) from within a child (or subclass). It is especially useful in inheritance, particularly in method overriding and multiple inheritance scenarios.
# 
# 🔹 Why use super()?
# To reuse code from the parent class without hardcoding the class name.
# 
# To ensure method resolution order (MRO) is respected in multiple inheritance.
# 
# To avoid duplicating code in subclasses.
# 
# 

# %%
#Example: Single Inheritance
class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        super().show()       # calls Parent's show()
        print("This is the child class.")

c = Child()
c.show()

#Example: Calling __init__ of Parent Class
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)   # initializes 'name' in Person
        self.grade = grade



# %% [markdown]
# #TQ21:- What is the significance of the __del__ method in Python?
#        -The __del__() method in Python is a special (dunder) method known as the destructor. It is automatically called when an object is about to be destroyed or garbage collected.
# 
# 🔹 Purpose of __del__:
# To release resources, like closing files or network connections.
# 
# To clean up memory or perform final actions before object deletion.
# 
# 

# %%
#Example
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print("File opened.")

    def __del__(self):
        self.file.close()
        print("File closed.")

f = FileHandler("test.txt")
del f  # Triggers __del__()


# %% [markdown]
# #TQ22:- What is the difference between @staticmethod and @classmethod in Python?
#        - Both @staticmethod and @classmethod are decorators used to define methods that don’t behave like regular instance methods, but they differ in how they interact with the class and its objects.
# 
# 🔹 @staticmethod:
# Does not take self or cls as the first parameter.
# 
# Behaves like a normal function placed inside a class.
# 
# Cannot access or modify class or instance data.
# 
# Used when the method logic is related to the class but independent of class/object state.
#  @classmethod:
# Takes cls as the first parameter.
# 
# Can access and modify class variables.
# 
# Used when you want to work with the class itself, not individual instances.

# %%
#Example
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # Output: 8

#Example
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Student.get_count())  # Output: 0 (before object creation)
s1 = Student("Aditya")
print(Student.get_count())  # Output: 1


# %% [markdown]
# #TQ23:- How does polymorphism work in Python with inheritance?
#        -In Python, polymorphism with inheritance means that a subclass can override methods of a parent class, and objects of different subclasses can be used interchangeably through a common interface (usually the parent class).
# 
# This is a core part of runtime polymorphism, where the method that gets executed depends on the actual object type, not the reference type.
# 
# 🔹 Key Concepts:
# Subclasses override methods from their superclass.
# 
# A base class reference can point to any subclass object.
# 
# Method calls are resolved dynamically at runtime.
# 
# .
# 
# 🔹 Benefits:
# Simplifies code: Write functions that handle a variety of types.
# 
# Extensibility: Add new subclasses without changing existing code.
# 
# Flexibility: Behavior adapts based on object type at runtime.
# 
# 

# %%
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Polymorphic behavior
def animal_sound(animal):
    animal.make_sound()

# Different subclass objects
animal_sound(Dog())   # Output: Bark
animal_sound(Cat())   # Output: Meow


# %% [markdown]
# #TQ24:- What is method chaining in Python OOP?
#        - Method chaining is a programming technique where multiple methods are called on the same object in a single line, one after another. In Python OOP, it is achieved by making each method return self, so that the next method can be called on the same object.
#  Syntax Pattern:
# object.method1().method2().method3()
# Each method must return the object itself (self) to enable chaining.
# 
# 
# 

# %%
class Person:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.city = None

    def set_age(self, age):
        self.age = age
        return self  # Enables chaining

    def set_city(self, city):
        self.city = city
        return self  # Enables chaining

    def show(self):
        print(f"{self.name}, {self.age}, {self.city}")
        return self  # Optional chaining

# Using method chaining
p = Person("Aditya").set_age(22).set_city("Delhi").show()


# %% [markdown]
# #TQ25:-What is the purpose of the __call__ method in Python?
#       - The __call__() method in Python is a special (dunder) method that allows an object to be called like a function. When you write obj(), Python automatically calls obj.__call__().
# 
# 🔹 Purpose:
# To make an instance behave like a function.
# 
# Useful in scenarios like function wrappers, decorators, or stateful functions.

# %%
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, {self.name}!")

g = Greeter("Aditya")
g()  # Equivalent to g.__call__()


# %% [markdown]
# #OOPs Practicle Question:-

# %% [markdown]
# #PQ1:- Create a parent class Animal with a method speak() that prints a generic message.
#      
# 
# 

# %%
# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print("Bark!")

# Testing both classes
generic_animal = Animal()
dog = Dog()

# Calling the speak method
generic_animal.speak()  # Output: This animal makes a sound.
dog.speak()             # Output: Bark!


# %% [markdown]
# #PQ2:-  Write a program to create an abstract class Shape with a method area().
# Derive classes Circle and Rectangle from it and implement the area() method in both.

# %%
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Must be overridden

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Testing
c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", round(c.area(), 2))      # Output: Circle Area: 78.54
print("Rectangle Area:", r.area())             # Output: Rectangle Area: 24


# %% [markdown]
# #PQ3:-Implement a multi-level inheritance scenario where:
# 
# Class Vehicle has an attribute type.
# 
# Class Car is derived from Vehicle.
# 
# Class ElectricCar is further derived from Car and adds a battery attribute.

# %%
# Base class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def show_type(self):
        print(f"Vehicle Type: {self.vehicle_type}")

# First-level derived class
class Car(Vehicle):
    def __init__(self, vehicle_type, brand):
        super().__init__(vehicle_type)
        self.brand = brand

    def show_brand(self):
        print(f"Car Brand: {self.brand}")

# Second-level derived class
class ElectricCar(Car):
    def __init__(self, vehicle_type, brand, battery_capacity):
        super().__init__(vehicle_type, brand)
        self.battery_capacity = battery_capacity

    def show_details(self):
        self.show_type()
        self.show_brand()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Testing
e_car = ElectricCar("4-wheeler", "Tesla", 75)
e_car.show_details()


# %% [markdown]
# #PQ4:-  Demonstrate polymorphism by creating a base class Bird with a method fly().
# Create two derived classes Sparrow and Penguin that override the fly() method.
# 
# 

# %%
# Base class
class Bird:
    def fly(self):
        print("Birds can fly in general.")

# Derived class 1
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high in the sky.")

# Derived class 2
class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly but can swim very well.")

# Polymorphism in action
def test_flying(bird_obj):
    bird_obj.fly()

# Testing with different bird objects
bird1 = Sparrow()
bird2 = Penguin()

test_flying(bird1)  # Output: Sparrow flies high in the sky.
test_flying(bird2)  # Output: Penguins can't fly but can swim very well.


# %% [markdown]
# #PQ5:-Write a program to demonstrate encapsulation by creating a class BankAccount
# with private attributes balance and methods to deposit, withdraw, and check balance.

# %%
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

# Testing
acc = BankAccount("Aditya", 1000)
acc.deposit(500)             # ₹500 deposited.
acc.withdraw(300)            # ₹300 withdrawn.
print("Current Balance:", acc.get_balance())  # Output: 1200

# Trying to access private variable directly (will raise error)
# print(acc.__balance)  ❌ AttributeError


# %% [markdown]
# #PQ6:- Demonstrate runtime polymorphism using a method play() in a base class Instrument.
# Derive classes Guitar and Piano that implement their own version of play().

# %%
# Base class
class Instrument:
    def play(self):
        print("An instrument is being played.")

# Derived class 1
class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar strings.")

# Derived class 2
class Piano(Instrument):
    def play(self):
        print("Pressing piano keys gracefully.")

# Function demonstrating runtime polymorphism
def perform(instrument_obj):
    instrument_obj.play()

# Testing
g = Guitar()
p = Piano()

perform(g)  # Output: Strumming the guitar strings.
perform(p)  # Output: Pressing piano keys gracefully.


# %% [markdown]
# #PQ7:-  Create a class MathOperations with:
# 
# A class method add_numbers() to add two numbers.
# 
# A static method subtract_numbers() to subtract two numbers.
# 
# 

# %%
class MathOperations:
    @classmethod
    def add_numbers(cls, a, b):
        result = a + b
        print(f"Sum: {result}")
        return result

    @staticmethod
    def subtract_numbers(a, b):
        result = a - b
        print(f"Difference: {result}")
        return result

# Testing the methods
MathOperations.add_numbers(10, 5)        # Output: Sum: 15
MathOperations.subtract_numbers(10, 5)   # Output: Difference: 5


# %% [markdown]
# #PQ8:-  Implement a class Person with a class method to count the total number of persons created.
# 
# 

# %%
class Person:
    count = 0  # Class variable to keep track of instances

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Increment count whenever a new object is created

    @classmethod
    def get_total_persons(cls):
        return cls.count

# Creating Person objects
p1 = Person("Aditya")
p2 = Person("Riya")
p3 = Person("Aman")

# Checking total persons created
print("Total Persons:", Person.get_total_persons())  # Output: Total Persons: 3


# %% [markdown]
# #PQ9:-  Write a class Fraction with attributes numerator and denominator.
# Override the __str__ method to display the fraction as "numerator/denominator".

# %%
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Testing
f1 = Fraction(3, 4)
f2 = Fraction(7, 2)

print(f1)  # Output: 3/4
print(f2)  # Output: 7/2


# %% [markdown]
# #PQ10:- Demonstrate operator overloading by creating a class Vector and overriding the + operator to add two vectors.

# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Add corresponding x and y values
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Testing
v1 = Vector(2, 3)
v2 = Vector(4, 1)
result = v1 + v2

print("Resultant Vector:", result)  # Output: (6, 4)


# %% [markdown]
# #PQ11:- Create a class Person with attributes name and age.
# Add a method greet() that prints:
# "Hello, my name is {name} and I am {age} years old."
# 
# 

# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Testing
p1 = Person("Aditya", 22)
p1.greet()


# %% [markdown]
# #PQ12:- Implement a class Student with attributes name and grades.
# Create a method average_grade() to compute the average of the grades.

# %%
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # Expected to be a list of numbers

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Testing
s1 = Student("Aditya", [85, 90, 78, 92])
s2 = Student("Riya", [70, 80])

print(f"{s1.name}'s Average Grade:", round(s1.average_grade(), 2))  # Output: ~86.25
print(f"{s2.name}'s Average Grade:", round(s2.average_grade(), 2))  # Output: 75.0


# %% [markdown]
# #PQ13:- Create a class Rectangle with methods:
# 
# set_dimensions() to set the length and width
# 
# area() to calculate and return the area
# 
# 

# %%
class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def set_dimensions(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Testing
rect = Rectangle()
rect.set_dimensions(5, 4)
print("Area of Rectangle:", rect.area())  # Output: 20


# %% [markdown]
# #PQ14:-  Create a class Employee with a method calculate_salary() that computes the salary based on hours worked and hourly rate.
# Create a derived class Manager that adds a bonus to the salary.

# %%
# Base class
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

# Derived class
class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + self.bonus

# Testing
emp = Employee("Ravi", 40, 200)
mgr = Manager("Aditya", 45, 300, 5000)

print(f"{emp.name}'s Salary:", emp.calculate_salary())   # Output: 8000
print(f"{mgr.name}'s Salary:", mgr.calculate_salary())   # Output: 18500


# %% [markdown]
# #PQ15:-Create a class Product with attributes name, price, and quantity.
# Implement a method total_price() that calculates the total price of the product.

# %%
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price       # Price per unit
        self.quantity = quantity # Total units

    def total_price(self):
        return self.price * self.quantity

# Testing
p1 = Product("Notebook", 40, 5)
p2 = Product("Pen", 10, 12)

print(f"Total for {p1.name}: ₹{p1.total_price()}")  # Output: ₹200
print(f"Total for {p2.name}: ₹{p2.total_price()}")  # Output: ₹120


# %% [markdown]
# #PQ16:- Create a class Animal with an abstract method sound().
# Create two derived classes Cow and Sheep that implement the sound() method.

# %%
from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Must be implemented by child classes

# Derived class 1
class Cow(Animal):
    def sound(self):
        print("Cow says Moo")

# Derived class 2
class Sheep(Animal):
    def sound(self):
        print("Sheep says Baa")

# Testing
animals = [Cow(), Sheep()]
for a in animals:
    a.sound()


# %% [markdown]
# #PQ17:- Create a class Book with attributes title, author, and year_published.
# Add a method get_book_info() that returns a formatted string with the book’s details.

# %%
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_book_info(self):
        return f"'{self.title}' by {self.author} ({self.year_published})"

# Testing
b1 = Book("Python Basics", "Aditya Sen", 2025)
b2 = Book("OOP in Depth", "Riya Verma", 2023)

print(b1.get_book_info())  # Output: 'Python Basics' by Aditya Sen (2025)
print(b2.get_book_info())  # Output: 'OOP in Depth' by Riya Verma (2023)


# %% [markdown]
# #PQ18:-  Create a class House with attributes address and price.
# Create a derived class Mansion that adds an attribute number_of_rooms.

# %%
# Base class
class House:
    def __init__(self, address, price):
        self.address = address
        self.price = price

    def show_info(self):
        print(f"Address: {self.address}")
        print(f"Price: ₹{self.price}")

# Derived class
class Mansion(House):
    def __init__(self, address, price, number_of_rooms):
        super().__init__(address, price)
        self.number_of_rooms = number_of_rooms

    def show_info(self):
        super().show_info()
        print(f"Number of Rooms: {self.number_of_rooms}")

# Testing
m1 = Mansion("Beverly Hills, LA", 50000000, 12)
m1.show_info()



