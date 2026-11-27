class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

class Salesperson(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name, base_salary)  # ส่งค่าให้คลาสแม่จัดการ
        self.commission = commission         # เก็บค่าคอมมิชชันเพิ่ม

    def calculate_pay(self):
        return self.base_salary + self.commission

emp1 = Employee("สมชาย", 25000)

sales1 = Salesperson("สมหญิง", 20000, 8500)

print(f"พนักงานทั่วไป: {emp1.name} | เงินเดือนสุทธิ: {emp1.calculate_pay()} บาท")
print(f"พนักงานขาย: {sales1.name} | เงินเดือนสุทธิ: {sales1.calculate_pay()} บาท")