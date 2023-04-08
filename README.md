# Object Oriented Programming (OOP) in Python

## Basic Concepts and Advantages of OOP

*  What is OOP?   
Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.
[Source](https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP)

* Name the four basic principles of Object-Oriented Programming.   
Abstraction, inheritance, encapsulation, and polymorphism.
[Source](https://khalilstemmler.com/articles/object-oriented/programming/4-principles/#:~:text=Abstraction%2C%20encapsulation%2C%20inheritance%2C%20and%20polymorphism%20are%20four%20of%20the,principles%20of%20object%2Doriented%20programming.)

* Why does OOP contribute to the modularity of a program?   
The software enables modularity by allowing developers to break down a complex problem into self-contained units to make specific designs.
[Source](https://emeritus.org/blog/coding-what-is-object-oriented-programming/#:~:text=Modularity,units%20to%20make%20specific%20designs.)

## Classes 
* What is a class?   
In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
[Source](https://brilliant.org/wiki/classes-oop/)

* What type of word is typically used as the name of a class?  
A noun

*  Explain the syntax used to define a class in Python.
```python
Class Dog():
  
  def __init__(self, atributes):
      self.atributes = atributes
```

## Instances and Instance Attributes
*  What is an instance?   
An instance is simply defined as a case or occurrence of anything.
[Source](https://www.techopedia.com/definition/16325/instance)

* How are classes related to instances?   
An instance of a class is an object.
[Source](https://www.techtarget.com/whatis/definition/instance#:~:text=An%20instance%20of%20a%20class,they%20are%20called%20instance%20variables.)

*  What is an instance attribute?   
Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.
[Source](https://www.tutorialsteacher.com/articles/class-attributes-vs-instance-attributes-in-python)

* What is the role of init () in the creation and initialization of instance
attributes?   
 The __init__  function is called every time an object is created from a class. The __init__ method lets the class initialize the object’s attributes and serves no other purpose.
 [Source](https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html#:~:text=The%20__init__%20method%20lets%20the%20class%20initialize%20the,and%20serves%20no%20other%20purpose.)
 
 * What is the role of the keyword ’self’ in a Python class?   
This handy keyword allows you to access variables, attributes, and methods of a defined class in Python.
 [Source](https://blog.hubspot.com/website/python-self#:~:text=Let's%20get%20started.-,What%20is%20SELF%20in%20Python%3F,it%20by%20any%20other%20name.)
 
 * How to Define Nonpublic Methods in a Python Class?   
 Strictly speaking, everything defined in a Python class is public.
 [Source](https://towardsdatascience.com/how-to-define-nonpublic-methods-in-a-python-class-f477a1ddf3c0)
 
 * Explain public, protected and private members   
 **Public Members:** Public members (generally methods declared in a class) are accessible from outside the class. The object of the same class is required to invoke a public method.All members in a Python class are public by default.    
 **Protected Members:** Protected members of a class are accessible from within the class and are also available to its sub-classes. No other environment is permitted access to it. This enables specific resources of the parent class to be inherited by the child class.    
 **Private Members:** Python doesn't have any mechanism that effectively restricts access to any instance variable or method. Python prescribes a convention of prefixing the name of the variable/method with a single or double underscore to emulate the behavior of protected and private access specifiers.
 [Source](https://www.tutorialsteacher.com/python/public-private-protected-modifiers)
 
 ## Class Attributes
*  What is a class attribute?    
A class attribute is a Python variable that belongs to a class rather than a particular object.
[Source](https://builtin.com/software-engineering-perspectives/python-attributes#:~:text=A%20class%20attribute%20is%20a,.)

* Describe the differences between class attributes and instance attributes   
Class attributes are the variables defined directly in the class that are shared by all objects of the class. Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.
[Source](https://www.tutorialsteacher.com/articles/class-attributes-vs-instance-attributes-in-python#:~:text=Class%20attributes%20are%20the%20variables,are%20defined%20in%20the%20constructor.&text=Defined%20directly%20inside%20a%20class.)

## Encapsulation and Abstraction
*  Describe the principle of Encapsulation and its importance in Object Oriented Programming.    
Encapsulation is a way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object.
 [Source](https://www.sumologic.com/glossary/encapsulation/#:~:text=Encapsulation%20is%20a%20way%20to,an%20instantiated%20class%20or%20object.)

* Describe the principle of Abstraction and its importance in Object-Oriented Programming.  
 Through the process of abstraction, a programmer hides all but the relevant data about an object in order to reduce complexity and increase efficiency.
 [Source](https://www.techtarget.com/whatis/definition/abstraction#:~:text=In%20object%2Doriented%20programming%2C%20abstraction,reduce%20complexity%20and%20increase%20efficiency.)
  
 * Describe what happens during the process of Name Mangling and its main purpose.  
 In name mangling process any identifier with two leading underscore and one trailing underscore is textually replaced with _classname__identifier where classname is the name of the current class.
   [Source](https://www.geeksforgeeks.org/name-mangling-in-python/)
   
 ## Properties, Getters, and Setters
