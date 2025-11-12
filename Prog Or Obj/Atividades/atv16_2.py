from atv16_1 import Employee, FulltimeEmployee, HourlyEmployee

def run_tests():
    print("-- Resultados --")
    print("-" * 40)

    fulltime_employee_1 = FulltimeEmployee("Ana", "Costa", 3500.00)

    print(f"Consultas do funcionário: {fulltime_employee_1.full_name()}")
    print(f"    Primeiro Nome: {fulltime_employee_1.get_first_name()}")
    print(f"    Nome Completo: {fulltime_employee_1.full_name()}")
    print(f"    Salário Base: R${fulltime_employee_1.get_base_salary():.2f}")
    print(f"    Salário Total: R${fulltime_employee_1.compute_salary():.2f}")

    fulltime_employee_1.set_base_salary(4000.00)
    print(f"    Novo Salário Base: R${fulltime_employee_1.get_base_salary():.2f}")
    print(f"    Novo Salário Total: R${fulltime_employee_1.compute_salary():.2f}")

    print("-" * 40)

    fulltime_employee_2 = FulltimeEmployee("Carlos", "Martins") 
        
    print(f"    Funcionário: {fulltime_employee_2.full_name()}")
    print(f"    Salário Base: R${fulltime_employee_2.get_base_salary():.2f}")
    print(f"    Salário Total: R${fulltime_employee_2.compute_salary():.2f} (+ 200.00)")
    
    print("qt."{Employee.get_count_employees()})

if __name__ == "__main__":
    run_tests()