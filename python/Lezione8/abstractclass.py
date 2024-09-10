from abc import ABC, abstractmethod

print("ESERIZIO 1\n\n\n")
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, raggio) -> None:
        self.raggio = raggio
    
    def area(self):
        return round(3.14 * self.raggio ** 2)

    def perimeter(self):
        return round(2 * 3.14 * self.raggio)

class Rectangle(Shape):
    def __init__(self, base, altezza) -> None:
        self.altezza = altezza
        self.base = base
    
    def area(self):
        return self.altezza * self.base 

    def perimeter(self):
        return self.altezza * 2 + self.base * 2
    
cerchio1 : Circle = Circle(10)
rettangolo1 : Rectangle = Rectangle(10, 5)

print(cerchio1.area(), cerchio1.perimeter())
print(rettangolo1.area(), rettangolo1.perimeter())


print("\n\n\nESERCIZIO 2\n\n\n")

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

print(f"Somma: {MathOperations.add(10, 5)}, Moltiplicazione: {MathOperations.multiply(5, 5)}")

print("\n\n\n ESERCIZIO 3\n\n\n")

class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Titolo : {self.title}, Autore: {self.author}, ISBN: {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str):
        return cls(string = book_str)