# Explain how objects are stored in memory. Mention the role of the id of an object.

"""
Objects are stored in Python in a particular way, in Python, objects are stored as references. 
This will sound weird to some people, but isn’t it, by this way we can save a lot of memory and CPU power 
because some objects that have the same value as str or int(-5,256) are the same references. 
Lists and objects made up by the user don’t follow this rule. 
The function of id() is relevant because it leads to a specific and unique label of an object.
"""

# Explain the purpose of the is operator. How is it related to the id of an object?

"""
The “is” operator works with de “id” of the objects, 
if we have two variables that have the same value, 
the "is" operator will look at the references of these two objects and not the value.
"""