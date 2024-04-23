#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.



print("ESERCIZIO 8-1")


def display_message() -> str:
    print("In this session we smoke!\n\n\n")

display_message()


#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.



print("ESERCIZIO 8-2")

"""
def favourite_book(title:str):
    title: str = input("insert title: ")
    print(f"my favourite book is {title}")
favourite_book(title="")"""

def favourite_book(title:str) -> str:
    print(f"my favourite book is {title}")
favourite_book(title="ciao")
favourite_book("ciao")
print("\n\n\n")



#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.



print("ESERCIZIO 8-3")

def make_shirt(size, message) -> str:
    print(f"the size of the shirt is {size} and the message on it is {message}")

make_shirt("S","viva l'america")
make_shirt(size = "XS", message = "viva l'america")
print("\n\n\n")


#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



print("ESERCIZIO 8-4")

def make_shirt1(size = "L", message = "I love Python") -> str:
    print(f"the size of the shirt is {size} and the message on it is {message}")

make_shirt1()
make_shirt1(size = "M")
make_shirt1(size = "XL", message = "I hate Python")
print("\n\n\n")


#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.



print("ESERCIZIO 8-5")

def describe_city(city, counrty = "Italia") -> str:
    return f"{city} {counrty}"


describe_city("roma")
describe_city("milano")
describe_city("napoli")


print("\n\n\n")


#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.



print("ESERCIZIO 8-6")

def city_counrty(city, country) -> str:
    return f"{city}, {country}"
print(city_counrty(city = "Roma", country= "Italia"))
print(city_counrty(city= "New York", country="US"))
print(city_counrty(city= "New Mexico", country= "Mexico"))
print("\n\n\n")


#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.



print("ESERCIZIO 8-7")

def make_album(name, album) -> dict:
    
print("ESERCIZIO 8-8")

print("ESERCIZIO 8-9")

print("ESERCIZIO 8-10")

print("ESERCIZIO 8-11")

print("ESERCIZIO 8-12")

print("ESERCIZIO 8-13")

print("ESERCIZIO 8-14")

print("ESERCIZIO 8-15")

print("ESERCIZIO 8-16")

print("ESERCIZIO 8-17")
