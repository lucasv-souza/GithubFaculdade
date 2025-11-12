from abc import ABC, abstractmethod

class Employee(ABC):
    count = 0
    @classmethod                    
    def count_employees(cls):
        return cls.count
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def set_first_name(self, new_first_name: str):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name: str):
        self.last_name = new_last_name

    @abstractmethod
    def compute_salary(self) -> float:
        pass

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class FulltimeEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary= 1500):
        super().__init__(first_name, last_name)
        self.base_salary = base_salary
        
    def get_base_salary(self) -> float:
        return self.base_salary

    def set_base_salary(self, new_base_salary: float):
        if new_base_salary >= 0:
            self.base_salary = new_base_salary
        else:
            raise ValueError("O salário base não pode ser negativo.")

    def compute_salary(self) -> float:
        BONUS = 200.00
        return self.base_salary + BONUS
    
class HourlyEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, hours_worked, hour_value=300.00):
        super().__init__(first_name, last_name)
        self.hours_worked = hours_worked
        self.hour_value = hour_value
        
    def get_hours_worked(self):
        return self.hours_worked
    
    def set_hours_worked(self, new_hours_worked):
        self.hours_worked = new_hours_worked

    def get_hour_value(self):
        return self.hour_value
        
    def set_hour_value(self, new_hour_value):
        self.hour_value = new_hour_value
        
    def compute_salary(self):
        return self.hours_worked * self.hour_value
    