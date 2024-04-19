#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
print("ESERCZIO 6-1\n\n\n")
Soggetto: dict = {"first_name" : "Daniele","last_name" : "Fioravanti","age" : "20","City" : "Roma"}
print(Soggetto["first_name"], Soggetto["last_name"], Soggetto["age"], Soggetto["City"])



#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.



print("ESERCIZIO 6-2\n\n\n")
Numeri: dict = {"Valerio" : 1, "leonardo" : 2, "Daneile" : 3, "Edoardo" : 5, "Emanuele" : 6}
for persona, numero in Numeri.items():
    print(f"{persona} Equivale a {numero}")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.



print("ESERCIZIO 6-3\n\n\n")
glossary: dict = {"append" : "aggiungi un valore alla fine della lista", "pop" : "rimiuovi un valore all'interno di una lista", "remove" : "rimuovi un valore senza restituzioni di un valore", "nosuffix" : "rimuove l'estensione di un file(bisogna specificare che parte levare)"}
for parola, significato in glossary.items():
    print(parola)
    print(significato)
    print("\n\n\n")


#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.



print("ESERCIZIO 6-7\n\n\n")
Persona1: dict = {"first_name" : "Valerio", "last_name" : "Gamba", "age" : "20", "citta" : "Roma"}
Persona2: dict = {"first_name" : "Lorenzo", "last_name" : "Marianella", "age" : "23", "citta" : "Roma"}
people: list = [Soggetto, Persona1, Persona2]
for persona in people:
    for dato, informazione in persona.items():
        print("\n", dato, ':', informazione)
print("\n\n\n")
#a : list = index for index in a



#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 



print("ESERCIZIO 6-8\n\n\n")
cane : dict = {"Tipo" : "cane", "owner" : "daniele"}
gatto : dict = {"Tipo" : "gatto", "owner" : "leonardo"}
criceto : dict = {"Tipo" : "criceto", "owner" : "valerio"}
animali: list = [cane,gatto,criceto]
for animale in animali:
    for tipo,proprietario in animale.items():
        print("\n",tipo, ':', proprietario)
print("\n\n\n")



#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.



print("ESERCIZIO 6-9\n\n\n")



favourite_places: dict = {"valerio" : ["Malaga","New York","Amsterdam"], "daniele" : ["Ibiza", "Roma", "Madrid"], "leonardo" : ["Mikonos", "Rotterdam", "Anzio"]}
for k,v in favourite_places.items():
    print(f"{k}:")
    for element in v:
        print(f"\t{element}")
print("\n\n\n")



#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.



print("ESERCIZIO 6-10\n\n\n")



Numeri: dict = {"Valerio" : [1,2,3], "leonardo" : [4,5,6], "Daneile" : [7,8,9], "Edoardo" : [23,54,67], "Emanuele" : [21,12,34]}
for persona, numero in Numeri.items():
    print(f"{persona} ha come numeri fortunati: {numero}")


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.



print("ESERCIZIO 6-11\n\n\n")



roma: dict = {"county" : "italy", "population" : "3.8M", "quote" : "The best art in the world"}
milano: dict = {"county" : "italy", "population" : "2.7M", "quote" : "the best style in the world"}
berlino: dict = {"county" : "germany", "population" : "4M", "quote" : "the best public transport in the world"}
cities: list = [milano,roma,berlino]

for ss in cities:
    for k,v in ss.items():
        print(ss,k,v,"\n")