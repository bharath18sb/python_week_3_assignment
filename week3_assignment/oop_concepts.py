class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

if __name__ == "__main__":
    emp1 = FullTimeEmployee("Alice", 1, 50000)
    emp2 = PartTimeEmployee("Bob", 2, 50, 100)

    for emp in [emp1, emp2]:
        print(f"Employee {emp.name} (ID: {emp.id}) salary: ₹{emp.calculate_salary():.2f}")
