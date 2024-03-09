class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model  = model
        self.year   = year
    def display_infor(self):
        print(f"{self.year} {self.make} {self.model}")
class Car(Vehicle):
    def __init__(self, make, model, year,num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    def display_infor(self):
        print(f"Car: {self.year} {self.model} {self.make}, Doors: {self.num_doors}")

class Truck(Vehicle):
    def __init__(self, make, model, year,bed_length):
        super().__init__(make, model, year )
        self.bed_length = bed_length
    def display_infor(self):
            print(f"Truck: {self.year} {self.make} {self.model}, Bed Length: {self.bed_length} ")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year ,engine_size):
        super().__init__(make, model, year)
        self.engine_size= engine_size
    def display_infor(self):
        print(f"Motocycle: {self.year} {self.model} {self.make}, Engine size: {self.engine_size}  cc")
        
my_car = Car("Toyata", "Camry", 2020 , 4)
my_truck = Truck("ford", "F-150", 2021 , 6.5)
my_motobike =  Motorcycle("Ducati","Panigale V4",2019,873)

my_car.display_infor()
my_truck.display_infor()
my_motobike.display_infor()