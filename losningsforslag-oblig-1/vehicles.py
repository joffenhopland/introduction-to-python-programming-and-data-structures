class Vehicles:
    def __init__(self, make, year, milage, price):
        self.make = str(make)
        self.year = int(year)
        self.milage = int(milage)
        self.price = int(price)

    def __str__(self):
        return f"Make:  {self.make}  Model:  {self.year}  Milage:  {self.milage}  Price:  {self.price}"

    def get_make(self):
        return self.make
    def get_year(self):
        return self.year
    def get_milage(self):
        return self.milage
    def get_price(self):
        return self.price

    def set_make(self, make):
        self.make = make
    def set_year(self, year):
        self.year = year
    def set_milage(self, milage):
        self.milage = milage
    def set_price(self, price):
        self.price = price
        
class Car(Vehicles):
    def __init__(self, make, year, milage, price, doors):
        self.doors = int(doors)
        super().__init__(make, year, milage, price)
        
    def __str__(self):
        return f"{super().__str__()} Doors: {self.doors}"
        
    def get_doors(self):
        return self.doors
    
    def set_doors(self, doors):
        self.doors = doors
        
class Truck(Vehicles):
    def __init__(self, make, year, milage, price, drive_type):
        super().__init__(make, year, milage, price)
        self.drive_type = str(drive_type)
        
    def __str__(self):
        return f"{super().__str__()} Drivetype: {self.drive_type}"
    
    def get_drive_type(self):
        return self.drive_type
    
    def set_drive_type(self, drive_type):
        self.drive_type = drive_type
        
class SUV(Vehicles):
    def __init__(self, make, year, milage, price, pass_cap):
        super().__init__(make, year, milage, price)
        self.pass_cap = int(pass_cap)
        
    def __str__(self):
        return f"{super().__str__()} Number of passengers: {self.pass_cap}"
    
    def get_pass_cap(self):
        return self.pass_cap
    
    def set_pass_cap(self, pass_cap):
        self.pass_cap = pass_cap