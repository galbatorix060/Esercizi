from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patient : list, doctor : Dottore) -> None:
        self.patient = patient
        self.doctor = doctor
        if doctor.isAValidDoctor() == True:
            self.fatture = len(self.patient)
            self.salary = 0
        else:
            self.patient = [None]
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("non è possibile creare la classe fattura perche il dottore non è valido")
    
    def getSalary(self):
        self.salary = self.fatture * self.doctor.getParcel()
        return self.salary
    
    def getFatture(self):
        self.fatture = len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient : Paziente):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"alla lista del Dottor {self.doctor} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode):
        #rimuove = input("inserire codice identificativo paziente da rimuovere: ")
        self.patient.remove(idCode)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del dottor {self.doctor} è stato rimosso il paziente {rimuove}")
