# Explain why the @property syntax is preferred in Python over getters, setters, and property().

"""
The standard attribute access is the normal, Pythonic way of accessing attributes. 
The advantage of properties is that they are syntactically identical to attribute access, so you can change from one to another.
"""

# Submit the two versions of the modified class. Remember to perform some validations in the setters.

# First
class BouncyBall:
 
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand
 
    def get_price(self):
        return self._price
 
    def set_price(self, new_price):
        if isinstance(new_price, float) and new_price > 0:
            self._price = new_price
        else:
            print("Please enter a valid price.")
 
    price = property(get_price, set_price)
 
    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("Please introduce a valid size.")
    
    size = property(get_size, set_size)
 
    def get_brand(self):
        return self._brand
    
    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print("Please introduce a valid new brand.")
        
    brand = property(get_brand, set_brand)

# Second
class BouncyBall:
 
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand
 
    @property
    def price(self):
        return self._price
    
    @property
    def size(self):
        return self._size
 
    @property
    def brand(self):
        return self._brand
 
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and new_price > 0:
            self._price = new_price
        else:
            print("Please enter a valid price.")
    
    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("Please introduce a valid size.")
 
    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print("Please introduce a valid new brand.")