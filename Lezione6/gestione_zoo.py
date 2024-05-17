#Leonardo Marianella
class Zoo:
    def __init__(self) -> None:     
        self.fences : list = []
        self.zoo_keepers : list = []

    def add_fence(self, fence) -> None:
        
        self.fences.append(fence)
    
    def add_zookeeper(self, zookeeper) -> None:
        
        self.zoo_keepers.append(zookeeper)


    def clean(self):
        total_cleaning_time = 0.0
        for fence in self.fences:

            if fence.animal:
                
                cleaning_time = fence.areafence / (fence.areafence - (fence.areafence - sum(animal.height * animal.width for animal in fence.animal)))
                total_cleaning_time += cleaning_time

            else:
                
                cleaning_time = fence.areafence
                total_cleaning_time += cleaning_time
        
        return total_cleaning_time
    
    def describe_zoo(self) -> str:

        print("Guardiani: ")

        for Zookeeper in self.zoo_keepers:
            print(f"Guardiano (nome={Zookeeper.name}, cognome={Zookeeper.surname}, id={Zookeeper.id})")

        print("\nRecinti: ")

        for fence in self.fences:
            
            print(f"Recinto(area={fence.area}, temperatura={fence.temperature}, habitat={fence.habitat})")
            print("Con all'interno: ")
            
            for animal in fence.animal:
                print(f"Animali(nome={animal.name}, specie={animal.species}, età={animal.age})")
        
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
            animalarea += animal.height * animal.width
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

