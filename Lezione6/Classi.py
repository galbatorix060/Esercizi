class Person:
    
    def __init__(self, name:str,surname:str,ssn:str) -> None:

        """

        """
        self._name : str = name
        self._surname : str = surname
        self._ssn : str = ssn

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

        raise Exception("You cannot modify the name!")



person1: Person = Person(name="Leonardo", surname="Marianella", ssn="MRNLRD04U20H501Y")
print(person1.get_name())

person1.set_name(name = "Francesco")
print(person1.get_name())