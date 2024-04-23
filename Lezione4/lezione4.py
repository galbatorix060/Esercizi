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

def make_album(name : str, album : str) -> dict:
    Music_Album : dict = {"artist" : name, "name_album" : album}
    return Music_Album
a: dict = make_album("paky", "rozzi")
b: dict = make_album("gemitaiz", "qvc9")
c: dict = make_album("kety", "dolcevita")
print(a,"\n", b, "\n", c)

def make_album1(name : str, album : str, nsong : int = None) -> dict:
    Music_Album : dict = {"artist" : name, "name_album" : album, "number_songs" : nsong}
    return Music_Album
d: dict = make_album1("Achille", "ragazzi madre", 12)
e: dict = make_album1("rove", "ciao")
print(d,"\n", e, "\n\n\n")


#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.


print("ESERCIZIO 8-8")
"""
user : dict = {}
i = 1
while i < 100:
    i += 1
    user = make_album1(name=input("inserisci nome artista: "), album=input("inserisci nome album: "), nsong=input("inserisci numero canzoni: "))
    print("Shif + C to exit or Enter to continue")
    if input() == "C":
        break
print(user,"\n\n\n")"""


#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.



print("ESERCIZIO 8-9")

messages: list = ["ciao", "come stai", "tutto bene?", "oggi bel tempo"]
messages1: list = ["eccolo", "ollalero", "viva la lazio"]
def show_messages(l) -> str:
    for i in l:
        print(i)
    return l
show_messages(messages)
show_messages(messages1)
print("\n\n\n")


#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.



print("ESERCIZIO 8-10")

def send_messages(message) -> str:
    sent_messages: list = []
    show_messages(messages)
    for i in message:
        sent_messages.append(i)
    for i in sent_messages:
        print(f"sent message: {i}")
    return sent_messages

send_messages(messages)
print("\n\n\n")


#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.



print("ESERCIZIO 8-11")

a = send_messages(messages1)
print(a, "\n", messages1)


print("ESERCIZIO 8-12")

print("ESERCIZIO 8-13")

print("ESERCIZIO 8-14")

print("ESERCIZIO 8-15")

print("ESERCIZIO 8-16")

print("ESERCIZIO 8-17")
