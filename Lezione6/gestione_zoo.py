class Zoo:
    def __init__(self, fences, zoo_keepers) -> None:     
        self.fences : list = fences
        self.zoo_keepers : list = zoo_keepers

class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat) -> None:
        self.name : str = name
        self.species : str = species
        self.age : int = age
        self.height : int = height
        self.width : int = width
        self.preferred_habitat : str = preferred_habitat
        self.health : float = round(100 *  (1/age), 3)

class Fence:
    def __init__(self, area, temperature, habitat) -> None:
        self.area : int = area
        self.temperature : int = temperature
        self.habitat : str = habitat
        self.animal : list[Animal] = []
    
    def animal_area(self):
        animalarea = 0
        for animal in self.animal:
            animalarea += Animal.height * Animal.width
        return animalarea
    
    def add_animal(self, animal):
        if self.area >= animal.height * animal.width:
            self.animal.append(animal)
            self.area -= animal.height * animal.width
    
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animal.remove(animal)
            self.area += animal.height * animal.width


class ZooKeeper:
    def __init__(self, name, surname, id) -> None:
        self.name = name
        self.surname = surname
        self.id = id

    def feed(self, fence: Fence, animal : Animal):
        if animal in Fence.animal:
            if fence.area >= animal.height * animal.width:
                animal.health += 1
                animal.width *= 1.02
                animal.height *= 1.02
    
    def clean(self):
