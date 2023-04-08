# Now you will practice how to implement inheritance in Python.
class ElectronicDevice():
    def __init__(self, id, brand, price) -> None:
        self.id = id
        self.brand= brand
        self.price = price
    
    def turn_on(self, turn_on_device=False):
        if turn_on_device == True:
            print("\n========= I'm On =========")
        elif turn_on_device == False:
            print("\n========= I'm Off =========")
        
class Computer(ElectronicDevice):
    def __init__(self, id, brand, price, ram, cpu, sdd) -> None:
        super().__init__(id, brand, price)
        self.ram = ram
        self.cpu = cpu
        self.sdd = sdd
        
    def sum(self, a:int, b:int):
        c = a + b
        print(c)
        
class Tv(ElectronicDevice):
    def __init__(self, id, brand, price, resolution, size) -> None:
        super().__init__(id, brand, price)
        self.resolution = resolution
        self.size = size
        
class Desktop(Computer):
    def __init__(self, id, brand, price, ram, cpu, sdd, usb_ports=5) -> None:
        super().__init__(id, brand, price, ram, cpu, sdd)
        self.usb_ports = usb_ports
        
class Laptop(Computer):
    def __init__(self, id, brand, price, ram, cpu, sdd, size) -> None:
        super().__init__(id, brand, price, ram, cpu, sdd)
        self.size = size
        

my_dekstop = Desktop(123, "Lg", 500, 16, 5, 1000, 6)

my_dekstop.turn_on()
my_dekstop.turn_on(True)
my_dekstop.sum(3, 4)