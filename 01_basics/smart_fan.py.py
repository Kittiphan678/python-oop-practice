class SmartFan:
    def __init__ (self,brand):
        self.brand = brand
        self.__speed = 0

    def turn_on(self):
        self.__speed = 1
        print(f"พัดลม {self.brand} เปิดทำงานแล้ว (ระดับ {self.__speed})")

    def change_speed(self,level):
        if self.__speed == 0 :
            print ("กรุณาเปิดพัดลมก่อนใช้งาน")
        elif level >= 1 and level <= 3:
            self.__speed = level
            print (f"ปรับความแรงลมเป็นระดับ : {level}")
        else :
            print ("ระดับความแรงไม่ถูกต้อง (เลือกได้เฉพาะ 1-3)")
    def turn_off(self):
        self.__speed = 0
        print ("ปิดพัดลมแล้ว")
fan = SmartFan("Hatari")
fan.change_speed(2)
fan.turn_on()
fan.change_speed(5)
fan.change_speed(3)
fan.turn_off()