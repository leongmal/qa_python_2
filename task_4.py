class EmployeeSalary:

    hourly_payment = 400

def __init__(self,name, hours=None, rest_days = 2, email=None):
    self.name = name
    self.hours = hours
    self.rest_days = rest_days
    self.email = email

@classmethod
def get_hours(cls,name,hours,rest_days,email):
    if hours is None:
        hours = (7 - rest_days) * 8
        return cls(name,hours,rest_days,email)
   

if __name__ == "__main__":
    # # Создание объекта с полными данными
    # employee_full = EmployeeSalary('Иван', 40, 2, 'lel@gmail.com')
    # print(employee_full)

    # Создание объекта с неполными данными (расчет часов и генерация email)
    employee_partial = EmployeeSalary.get_hours('Анна', rest_days=3)
    print(employee_partial)