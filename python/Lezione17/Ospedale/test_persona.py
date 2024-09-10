import unittest
from dottore import Dottore
from persona import Persona
from paziente import Paziente
from fatture import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self) -> None:
        self.persona = Persona("Leonardo", "Marianella")
    
    def test_inizialization(self):
        self.assertEqual(self.persona.getName(), "Leonardo")
        self.assertEqual(self.persona.getLastName(), "Marianella")
        self.assertEqual(self.persona.getAge(), 0) 

    def test_setName(self):
        self.persona.setName("Daniele")
        self.assertEqual(self.persona.getName(), "Daniele")
        self.persona.setName(123)
        self.assertEqual(self.persona.getName(), "Daniele")
    
    def test_setLastName(self):
        self.persona.setLastName("Fioravanti")
        self.assertEqual(self.persona.getLastName(), "Fioravanti")
        self.persona.setLastName(123)
        self.assertEqual(self.persona.getLastName(), "Fioravanti")

    def test_setAge(self):
        self.persona.setAge(20)
        self.assertEqual(self.persona.getAge(), 20)
        self.persona.setAge("Mario")
        self.assertEqual(self.persona.getAge(), 20)
    
class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", "cardiologo", 15.9)
    
    def test_inizialization(self):
        self.assertEqual(self.dottore.getName(), "Mario")
        self.assertEqual(self.dottore.getLastName(), "Rossi")
        self.assertEqual(self.dottore.getSpecializazion(), "Cardiologo")
        self.assertEqual(self.dottore.getParcel(), 15.9)
    
    def test_isAValidDoctor(self):
        self.dottore.setAge(34)
        self.assertTrue(self.dottore.isAValidDoctor())
        self.dottore.setAge(24)
        self.assertTrue(self.dottore.isAValidDoctor())
    
class TestPaziente(unittest.TestCase):
    def setUp(self) -> None:
        self.paziente = Paziente("Valerio", "Gamba", "123Valey")
    
    def test_inizialization(self):
        self.assertEqual(self.paziente.getName(), "Valerio")
        self.assertEqual(self.paziente.getLastName(), "Gamba")
        self.assertEqual(self.paziente.getIdCode(), "123Valery")

class TestFattura(unittest.TestCase):
    def setUp(self) -> None:
        self.doctor = Dottore("Enzo", "Ferrari", "Urologo", 21.5)
        self.doctor.setAge(40)
        self.paziente1 = Paziente("Enrico", "Mussolini", "456MUSS")
        self.paziente2 = Paziente("Marcello", "Russo", "135MRUS")
        self.paziente3 = Paziente("Luigia", "Proietti", "246LUPR")
        self.patient = [self.paziente1, self.paziente2]
        self.fattura = Fattura(self.patient, self.doctor)

    def test_inizialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 43.0)
    
    def test_addPatient(self):
        self.fattura.addPatient(self.paziente3)
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 64.5)

    def test_removePatient(self):
        self.fattura.removePatient("246LUPR")
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 43.0)

if __name__ == "__main__":
    unittest.main()