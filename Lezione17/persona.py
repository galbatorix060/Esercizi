class Persona:
    def __init__(self, first_name : str, last_name : str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa")
            self.__first_name = None
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa") 
            self.__last_name = None
        if self.__first_name is not None and self.__last_name is not None:
            self.age = 0
        else:
            self.age = None
    
    def setName(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("il nome inserito non è una stringa!")
    
    def setLastName(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa")

    def setAge(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            print("l'età deve essere un numero intero!")
    
    def getName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def getAge(self):
        return self.age
    
    def greet(self):
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.age} anni!")
