from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, idCode) -> None:
        super().__init__(first_name, last_name)
        self.__idCode = idCode
    
    def setIdCode(self, idCode):
        self.__idCode = idCode
    
    def getIdCode(self):
        return self.__idCode
    
    def patientInfo(self):
        print(f"Paziente: {self.__first_name} {self.__last_name}\n ID: {self.__idCode}")