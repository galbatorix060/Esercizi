from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization, parcel) -> None:
        super().__init__(first_name, last_name)

        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            self.specialization = None

        if isinstance(parcel, float):
            self.parcel = parcel
        else:
            self.parcel = None
            print("La parcella inserita non p un float!")
        
    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            print("la specializzazione inserita non è una stringa!")
        
    def setParcel(self, parcel):
        if isinstance(parcel, float):
            self.parcel = parcel
        else:
            print("la parcella inserita non è un float!")
    
    def getSpecializazion(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self):
        if self.age >= 30:
            print(f"Doctor {self.getName()} {self.getLastName()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastName()} is not valid!")
            return False
    
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.specialization}")