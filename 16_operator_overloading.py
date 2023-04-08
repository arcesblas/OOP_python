# Your task is to:
"""
Explain the relationship between rich comparison methods and operator overloading.

Define a class with all the rich comparison methods implemented and show how you 
can compare the instances of this class. Please include the output. 
You can choose which class to define and how it should be implemented. 
For example, you could define a Bubble class and choose how to compare the bubble instances.
"""

# Explain the relationship between rich comparison methods and operator overloading.
"""
Operator overloading occurs when an operator has different implementations depending on the data type of the operands.

This means that the same operator can have different functionality based on the data type of the operands.

Rich comparison methods are special methods that allow us to customize the "behavior" of the comparison operators ( < <= > >= == !=) when these operators act on instances of the class.

This customization of the behavior is a form of operator overloading because we are providing a different functionality for the same operator depending on the data type of the operands.
"""

# Submit your class with the rich comparison methods implemented.

class House:
	
	def __init__(self, size, color, price):
		self.size = size
		self.color = color
		
	def __lt__(self, other):
		return self.size < other.size
	
	def __le__(self, other):
		return self.size <= other.size
	
	def __eq__(self, other):
		return self.size == other.size
	
	def __ne__(self, other):
		return self.size != other.size
	
	def __gt__(self, other):
		return self.size > other.size
	
	def __ge__(self, other):
		return self.size >= other.size

	
house1 = House(60, "Blue", 67000)
house2 = House(90, "Red", 34000)
house1 < house2
# True
house1 <= house2
# True
house1 == house2
# False
house1 != house2
# True
house1 > house2
# False
house1 >= house2
# False