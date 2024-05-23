print("ESERCIZIO 9-1\n\n\n")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self) -> str:
        print("nome ristorante: ",self.restaurant_name, "tipo cucina: ", self.cuisine_type)

    def open_restaurant(self) -> str:
        print("the restaurant is open!")
    
    def set_number_served(self, number_served) -> int:
        self.number_served = number_served
    
    def get_number_served(self):
        print("il numero di coperti e: ", self.number_served)
    
    def increment_number_served(self):
        n = int(input("inserire nuovi coperti: "))
        self.number_served += n

restaurant: Restaurant = Restaurant("fracco", "Romana")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n\n\nESERCIZIO 9-2\n\n\n")

restaurant1 : Restaurant = Restaurant("oryza", "orientale")
restaurant2 : Restaurant = Restaurant("Layelana", "persiana")
restaurant3 : Restaurant = Restaurant("McDonald's", "fast food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print("\n\n\nESERCIZIO 9-3\n\n\n")

class User:
    def __init__(self, first_name, last_name, age, email, login_attempts = 0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = login_attempts
    
    def describe_user(self) -> str:
        print(f"name: {self.first_name}, last name: {self.last_name}, age: {self.age}, user email: {self.email}")
    
    def greet_user(self) -> str:
        print(f"welcome back {self.first_name}!!")
    
    def increment_login_attempts(self) -> int:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

user : User = User("Leonardo", "Marianella", 20, "leo.mari@gmail.com")

user.describe_user()
user.greet_user()

print("\n\n\nESERCIZIO 9-4\n\n\n")

restaurant.set_number_served(10)
restaurant.get_number_served()
restaurant.increment_number_served()
restaurant.get_number_served()

print("\n\n\nESERCIZIO 9-5\n\n\n")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

print("\n\n\nESERCIZIO 9-6\n\n\n")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = [], number_served=0) -> None:
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def set_flavors(self, flavors):
        self.flavors = flavors
    
    def get_flavors(self):
        for i in self.flavors:
            print(i)
    
ice2000 : IceCreamStand = IceCreamStand("ice2000", "gelateria")

ice2000.set_flavors(["pistacchio", "nocciola", "zabbaione", "Crema"])
ice2000.get_flavors()

print("\n\n\nESERCIZIO 9-7\n\n\n")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, login_attempts=0) -> None:
        super().__init__(first_name, last_name, age, email, login_attempts)
        privileges = []
        self.privileges = privileges
    
    def set_privileges(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print(i)

admin : Admin = Admin("admin", "", 20, "")

admin.describe_user()
admin.set_privileges(["can add post", "can delete post", "can ban user"])
admin.show_privileges()

print("\n\n\nESERCIZIO 9-8\n\n\n")

class Privileges:
    def __init__(self, privileges) -> None:
        self.privileges = privileges
    
    def show_privileges(self):
        for i in self.privileges:
            print(i)

privilegi : Privileges = Privileges(["can add post", "can delete post", "can ban user"])
\
privilegi.show_privileges()

class Admin2(User):
    def __init__(self, first_name, last_name, age, email, privileges, login_attempts=0) -> None:
        super().__init__(first_name, last_name, age, email, login_attempts)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()

admin2 : Admin2 = Admin2("admin2", "", 21, "", ["can add post", "can delete post", "can ban user", "can delete account"])

admin2.show_privileges()

print("\n\n\nESERCIZIO 9-9\n\n\n")

class ElectrictCar():
    def __init__(self, brand, model, year, battery) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.battery = battery

    def get_range(self):
        print(f"capienza batteria: {self.battery}")

    def upgrade_battery(self):
        if self.battery != 65:
            self.battery = 65
    
tesla : ElectrictCar = ElectrictCar("tesla", "model x", "2019", 40)
tesla.get_range()
tesla.upgrade_battery()
tesla.get_range()

print("\n\n\nESERCIZIO 9-10\n\n\n")

