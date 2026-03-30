from abc import ABC, abstractmethod
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any


# 1. Classe Base (Pai)
class Employee(ABC):
    def __init__(self, emp_id: int, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Método abstrato: obriga as classes filhas a implementarem sua própria versão
    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary,
            "bonus": self.calculate_bonus(),  # Aqui acontece a mágica do polimorfismo!
            "role": self.__class__.__name__,
        }


# 2. Classe Filha 1: Developer (Herança)
class Developer(Employee):
    def __init__(
        self, emp_id: int, name: str, salary: float, programming_language: str
    ):
        super().__init__(emp_id, name, salary)  # Reaproveita o construtor do pai
        self.programming_language = programming_language

    # Polimorfismo: O bônus do dev é 10% do salário
    def calculate_bonus(self) -> float:
        return self.salary * 0.10

    def to_dict(self):
        data = super().to_dict()
        data["programming_language"] = self.programming_language
        return data


# 3. Classe Filha 2: Manager (Herança)
class Manager(Employee):
    def __init__(self, emp_id: int, name: str, salary: float, team_size: int):
        super().__init__(emp_id, name, salary)  # Reaproveita o construtor do pai
        self.team_size = team_size

    # Polimorfismo: O bônus do gerente é 20% + 100 por pessoa na equipe
    def calculate_bonus(self) -> float:
        return (self.salary * 0.20) + (self.team_size * 100)

    def to_dict(self):
        data = super().to_dict()
        data["team_size"] = self.team_size
        return data


# ==========================================
# SCHEMAS DO FASTAPI (Como a API recebe os dados)
# ==========================================
class DeveloperCreate(BaseModel):
    id: int
    name: str
    salary: float
    programming_language: str


class ManagerCreate(BaseModel):
    id: int
    name: str
    salary: float
    team_size: int


# ==========================================
# ROTAS DA API (Endpoints)
# ==========================================
app = FastAPI(title="Employee API com POO")

# Simulação de um banco de dados em memória (um dicionário simples)
db: Dict[int, Employee] = {}


@app.post("/employees/developer", status_code=201)
def create_developer(dev: DeveloperCreate):
    if dev.id in db:
        raise HTTPException(status_code=400, detail="ID já existe")

    # Instanciando o objeto da nossa classe Developer
    new_dev = Developer(dev.id, dev.name, dev.salary, dev.programming_language)
    db[dev.id] = new_dev  # Salvando no nosso "banco"

    return {"message": "Desenvolvedor criado!", "data": new_dev.to_dict()}


@app.post("/employees/manager", status_code=201)
def create_manager(mgr: ManagerCreate):
    if mgr.id in db:
        raise HTTPException(status_code=400, detail="ID já existe")

    # Instanciando o objeto da nossa classe Manager
    new_mgr = Manager(mgr.id, mgr.name, mgr.salary, mgr.team_size)
    db[mgr.id] = new_mgr  # Salvando no nosso "banco"

    return {"message": "Gerente criado!", "data": new_mgr.to_dict()}


@app.get("/employees")
def list_employees():
    # Retorna todos os funcionários. O método to_dict() vai acionar o polimorfismo
    # e calcular o bônus correto dependendo se é Dev ou Manager!
    return [emp.to_dict() for emp in db.values()]
