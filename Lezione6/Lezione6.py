print("ESERCIZIO 2\n\n\n")


class Student:
    def __init__(self, name:str,studyProgram:str, age:str, gender:str) -> None:
        self._name:str = name
        self._studyProgram:str = studyProgram
        self._age: str = age
        self._gender: str = gender
    
    def printInfo(self) -> str:

        return self._name, self._studyProgram, self._age, self._gender

student1 : Student = Student(name="Leonardo", studyProgram="computer science", age="19", gender="Male")
student2 : Student = Student(name="Valerio", studyProgram="science", age="19", gender="Male")
student3 : Student = Student(name="Daniele", studyProgram="history", age="19", gender="Male")

print(student1.printInfo())
print(student2.printInfo())
print(student3.printInfo(),"\n\n\n")

"""
print("ESERCIZIO 3\n\n\n")


class Animal:
    def __init__(self, name:str, gender:str, color:str) -> None:
        self._name: str = name
        self._gender:str = gender
        self._color:str = color
   
    def setLegs(self) -> int:
        self._legs = int(input(f"inserire numero di gambe per {self._name}: "))
        return self._legs

    def getLegs(self) -> int:
        
        print(self._legs)

    def printInfo(self) -> str:
        print(self._name, self._gender, self._color,self._legs)

animal1: Animal = Animal(name="dog", gender="Female", color="black")
animal2: Animal = Animal(name="cat", gender="male", color="white")

print(animal1._name, animal2._name)
animal1.setLegs()
animal1.getLegs()
animal2.setLegs()
animal2.getLegs()
animal1.printInfo()
animal2.printInfo()
"""

print("\n\n\nESERCIZIO 4\n\n\n")


class Food:
    def __init__(self, name, price, description) -> None:
        self._name: str = name
        self._price: int = price
        self._description: str = description


class Menu:
    def __init__(self, menu: list = []) -> None:
        self._menu = menu
    
    def addFood(self, food: Food) -> list:
        self._menu.append(food)
        return self._menu
    
    def removeFood(self, food : Food) -> list:
        self._menu.remove(food)
        return self._menu
    
    def printPrices(self) -> str:
        for i in self._menu:
            print(i._price, i._name)
    
    def getAveregePrice(self) -> float:
        prezzo = 0
        for i in self._menu:
            prezzo += i._price
        media = prezzo / len(self._menu)
        return media
        
        

food1: Food = Food(name="banana", price=1, description="fruit")
food2: Food = Food(name="manzo", price=12, description="meet")
food3: Food = Food(name="orata", price=20, description="fish")
food4: Food = Food(name="lasagna", price=7, description="pasta")
lista: list = [food1,food2,food3]
menu: Menu = Menu(lista)
menu.addFood(food4)
menu.removeFood(food2)
menu.printPrices()
print(menu.getAveregePrice())
