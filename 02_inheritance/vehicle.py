class Vehicle:
    def __init__ (self,brand,model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} สตาร์ทเครื่องยนต์แล้ว")

class Motorcycle(Vehicle):
    def wheelie(self):
        print(f"{self.brand} {self.model} กำลังยกล้อ!")

moto = Motorcycle("Yamaha", "R15")
moto.start_engine()
moto.wheelie()