from abc import ABC, abstractmethod
import os

class Zwierze(ABC):
    @abstractmethod
    def dzwiek(self):
        pass
class Pies(Zwierze):
    def dzwiek(self):
        return "pies szczeka"

zwierze = Zwierze
pies = Pies()
print(pies.dzwiek())

class Pojazd():
    def __init__(self, typ):
        self.typ = typ
    def opis(self):
        return f"{self.typ}"


class Samochod(Pojazd):
    def __init__(self, marka, model, rok):
        self.marka = marka# __marka -> zmienna prywatna
        self.model = model
        self.rok = rok

    def opis(self):
        return f"{self.marka}\t{self.model}\t{self.rok}"


samochod1 = Samochod("Toyota", "Corolla", 2024)
print (samochod1.opis())
print()

# z1
employees = []

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def dane(self):
        print(f"{self.name}, wiek: {self.age}, wynagrodzenie: {self.salary}")


class EmployeesManager(Employee):
    def addEmployee(self, employee):
        employees.append(employee)
    def showAllEmployees(self):
        i = 0
        for item in employees:
            i += 1
            print(item.dane())
    def deleteEmployeesByAge(self, ageMin, ageMax):
        for item in employees:
            if ageMin <= item.age <= ageMax:
                print(f"Usunięty element: {item}")
                employees.remove(item)
    def findEmployeeByName(self, name):
        for item in employees:
            if item.name == name:
                return item
    def updateSalary(self, newValue, name):
        for item in employees:
            if item.name == name:
                item.salary = newValue


# z2
def zPlikuOdczyt(sciezka):
    plik = open(sciezka)
    dane = plik.read()
    plik.close()
    print("Odczytano plik")
    return dane.split("\n")

def doPlikuZapis(sciezka, dane):
    plik = open('dane.txt', 'w')
    temp = []
    for i in dane: temp.append(f"{i.name}, {i.age}, {i.salary}\n")
    plik.writelines(temp)
    plik.close()
    print("Zapisano do pliku")

if os.path.exists("employees.txt"):
    temp = zPlikuOdczyt("employees.txt")
    for item in temp:
        employees.append(Employee())
else:
    temp = Employee("A", 20, 2000)
    employees.append(temp)
    temp = Employee("B", 20, 2000)
    employees.append(temp)
    temp = Employee("C", 22, 2200)
    employees.append(temp)
    temp = EmployeesManager("D", 33, 2600)
    employees.append(temp)
doPlikuZapis("employees.txt", employees)
