class Empleado:
    def __init__(self,id,  name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.__salary = salary
    
    def getSalary(self):
        return self.__salary

    def setSalary(self, newSalary):
        self.__salary = newSalary
    
    def isValid(self):
        return self.__salary >= 0
    
    def showEmploye(self):
        print(f" ID : {self.id}, Nombre: {self.name}, Edad: {self.age} años, Salario: {self.getSalary()}€")

class Gerente(Empleado):
    def __init__(self, id, name, age, salary, department):
        super().__init__(id, name, age, salary)
        self.department = department
    
    def showEmploye(self):
        print(f"ID : {self.id}, Nombre: {self.name}, Edad: {self.age} años, Salario: {self.getSalary()}€, Departamento : {self.department}")


class Empresa:
    def __init__(self):
        self.employes = []
        self.employesDict = {}
    
    def addEmploye(self, employe):
        if not isinstance(employe, Empleado) :
            print("Error , Objeto no es un empleado.")
            return
        
        if not employe.isValid():
            print(f"Error: Salario inválido para {employe.name}")
            return
        
        self.employes.append(employe)
        self.employesDict[employe.id] = employe
    
    def showEmployess(self):
        if not self.employes:
            print("La lista esta vacia.")
            return
        
        print("Lista de empleados : ")
        for i, emp in enumerate(self.employes, 1):
            print(f"{i}. ", end="")
            emp.showEmploye()
    
    def orderBySalary(self):
        return sorted(self.employes, key=lambda x: x.getSalary())
    
    def getEmployeID(self, id):
        return self.employesDict.get(id, "ID no encontrado")

empresa = Empresa()

emp1 = Empleado(1, "Fernando Rojas", 45, 66000)
g1 = Gerente(2, "Avril Albbert", 22, 80000, "Tesoreria y Finanzas")
emp2 = Empleado(3, "Joan Rodriguez", 30, 30000)

empresa.addEmploye(emp1)
empresa.addEmploye(g1)
empresa.addEmploye(emp2)
print("Lista de empleados")
empresa.showEmployess()
print()
print("Lista de empleados ordenados por salario")
endressats = empresa.orderBySalary()
for emp in endressats:
    emp.showEmploye()
print()
print("Busqueda por ID")
print("Buscando ID 2 : ", end="")
print()
print("Buscando ID 33 : ", empresa.getEmployeID(99))
resultat = empresa.getEmployeID(2)
if isinstance(resultat, Empleado):
    resultat.showEmploye()
else :
    print(resultat)
