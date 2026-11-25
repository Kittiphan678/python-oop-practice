class Rectangle:
    def __init__ (self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 *(self.width + self.height))

c1 = Rectangle(5,10)
print(f"พื้นที่ :", c1.area())
print(f"เส้นรอบรูป :", c1.perimeter())