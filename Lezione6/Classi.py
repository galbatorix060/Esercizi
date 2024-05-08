class Person:
    
    def __init__(self,name:str,surname:str,ssn:str,birth_date: str,birth_place: str,gender: str) -> None:

        """

        """
        self._name : str = name
        self._surname : str = surname
        self._birth_date: str = birth_date
        self._bith_place: str = birth_place
        self._gender: str = gender
        self.compute_ssn()

    def _lower(self):

        self._name.lower()

    def get_ssn(self) -> str:

        """
        This function returns the ssn value
        input: noneùreturn: self._ssn : str, the function reeturns ssn value

        """

        return self._ssn
    
    def set_ssn(self, ssn: str) -> str:

        """
        
        This function set the ssn
        input: ssn : str, the parameter contains the user's ssn
        return: None

        """
        raise Exception("You cannot modify the name!")

    def get_name(self):
        
        """

        This function returns a person's name
        input: none
        return: self._name : str, the function returns the person's name

        """
        return self._name
    
    def set_name(self, name : str):

        """

        This function set the attribute name
        input: name : str, the parameter contains the user's name
        return : None

        """
        self._name = name
        self._ssn = self.compute_ssn()
    
    def __str__(self) -> str:
        
        return f"name: {self._name} surname: {self._surname} ssn: {self._ssn}"
    
    def compute_ssn(self) -> bool:

        """
        
        Check the ssn's correctness

        """

        first_three_name_char = self._name[:3]
        last_three_surname_char = self._surname[-3:]

        self._ssn = first_three_name_char + last_three_surname_char


person1: Person = Person(name="Leonardo", surname="Marianella", ssn="MRNLRD04U20H501Z",birth_date="24/05/2023",birth_place="Rome",gender="male")
#person2: Person = Person(name="Gigi", surname="Alfio", ssn="GIADV849IE")
"""
queue: list[Person] = [person1, person2]

for i in queue:

    print(i.get_ssn())

"""
print(person1.get_ssn())
#person1.set_ssn(ssn="AH500Y")
print(str(person1))
print(person1.get_name())
print(person1.get_name())
print(person1.get_ssn())