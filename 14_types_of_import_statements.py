"""
Your task is to:

Explain the types import statements 
that you can use to import a module in Python.

For each one of them, explain how you can use 
or call the imported elements. Please include examples.
"""

# Importing the whole module object
"""
using the syntax import module_name
>>>> import math
>>>> math.sqrt(25)
5.0
"""

# Importing specific things from a module
"""
use the from syntax for importing
>>>> from math import pi
>>>> pi
3.141592653589793
"""

# Importing a module under a different name
"""
use the as syntax when importing a whole module
>>>> import math as m
>>>> m.pi
3.141592653589793
>>>> m.sqrt(25)
5.0
"""

# Import specific things from the module and rename them as you're importing
"""
>>>> from os.path import join as join_path
"""