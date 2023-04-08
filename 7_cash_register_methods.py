"""
Your task is to: Define a CashRegister class.
Implement the methods of the CashRegister class based on the required functionality.
"""

# Requirements:
"""
Methods:
- The cash register should be able to:
- Add a product to a purchase.
- The cashier should be able to specify how many items of the same product will be purchased.
- By default, this value should be 1.
- Show the list of products in the current purchase.
- Remove a product from a purchase.
- Update the price of a product after it has been added to the purchase.
- Find the subtotal of the purchase (before taxes).
- Find the total taxes for the purchase (assume that the store will charge 5% of the total purchase in taxes).
- Find the total amount of a purchase.
x Clear the previous purchase to start a new one.
x Each one of the previous items should be implemented as a method in the class.
x Create at least three products with the format specified below.
x Call each one of these methods at least once with the appropriate arguments.
- Check if the output is correct and include it in your submission.

Attribute:
The cash register should have the name of the cashier assigned to the cash register as an instance attribute.

Products:
A product should be represented as a dictionary with two key-value pairs (a key-value pair for the name of the product and another key-value pair for its price).
For example: {"name": "Pizza", "price": 10.34}
"""

class CashRegister():
    purchase = {
        "product": [],
        "price": [],
        "cuantity": []
    }
    
    def __init__(self, cashier: str):      
      self.cashier = cashier
      
    def add_product(self, producto: str, prices: float, cuantitys=1):
        CashRegister.purchase["product"] += [producto]
        CashRegister.purchase["price"] += [prices]
        CashRegister.purchase["cuantity"] += [cuantitys]

    def del_product(self, producto: str):
        for k, v in CashRegister.purchase.items():
            if producto in CashRegister.purchase["product"]:
                x = CashRegister.purchase["product"].index(producto)
                CashRegister.purchase["product"].pop(x)
                CashRegister.purchase["price"].pop(x)
                CashRegister.purchase["cuantity"].pop(x)
                
    def show_purchase(self):
        print("\n========= Hi! These are the products that are in your shopping cart =========")
        print(CashRegister.purchase["product"])
    
    def change_price(self, producto: str, price: float):
        for v in CashRegister.purchase.values(): 
            for j in v:  
                if producto == j:
                   x = CashRegister.purchase["product"].index(producto)
                   CashRegister.purchase["price"][x] = price
                   print(f"\n========= Hi! You have updated the price of {producto} correctly, now it cost ${price} =========") 
    
    def subtotal(self):    
        self.subt = [a*b for a,b in zip(CashRegister.purchase["price"], CashRegister.purchase["cuantity"])]
        self.subt = round(sum(self.subt), 2)
        print(f"The subtotal of the purchase is ${self.subt}")
        return self.subt
    
    def tax(self):
        subt = self.subt
        self.tax = round(subt * 0.05, 2)
        print(f"The tax income si ${self.tax}")
        return self.tax
        
    def total(self):
        self.total = self.tax + self.subt
        print(f"The total price of the purchase with taxes is ${self.total}")
        
    def new_purchase(self):
        for k in CashRegister.purchase.keys():
            CashRegister.purchase[k] = []
        print("\n========= Ready for a new buy! =========") 
        
                 
       
purchase1 = CashRegister("Luis")
purchase1.add_product("Helado", 30.6, 3)  
purchase1.add_product("Crema", 10, ) 
purchase1.add_product("Cucumber", 2, 5) 

print(purchase1.purchase)      
purchase1.del_product("Crema")  
purchase1.show_purchase() 
purchase1.change_price("Cucumber", 4)
print(purchase1.purchase)
purchase1.subtotal()
purchase1.tax()
purchase1.total()
purchase1.new_purchase()
print(purchase1.purchase)