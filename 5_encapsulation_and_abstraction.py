""" Explain why an attribute is never really private in Python. 
In your explanation, please explain the process of name mangling with an example."""

# Answer

"""
In Python we cannot set private attributes, unlike Java. 
Thats because when we use single underscore before an attribute, what we are really trying to say is something like this 
“Hey! this attribute shouldn’t be modified, you can modify, yes, but you shouldn’t, so please stay away from this. 
I know you are a really nice person and you will respect this rule, so have a nice day and keep away from this attribute.”

Name mangling: What we are doing with name mangling is adding some “extra security”, in order to avoid name clashes. Here I show you an example I found on the internet:
"""

class Vehicle:
 
    def __init__(self, horn):
        self.__horn = horn
 
 
class MyCar(Vehicle):
 
    def __init__(self, horn):
        self.__horn=horn

# So the code will show this:

"""
 >>> from vehicle import Vehicle
>>> from vehicle import Vehicle, MyCar
>>> v1 = Vehicle('doodoo')
>>> v2 = MyCar('baaam')
>>> v1.__dict__
{'_Vehicle__horn': 'doodoo'}
>>> v2.__dict__
{'_MyCar__horn': 'baaam'}
"""

# Submit your Book class with the non-public attributes.
"""
* num_pages

* publisher

* ISBN
"""

class Book:
 
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self._num_pages = num_pages
        self._ISBN = ISBN
        self._publisher = publisher