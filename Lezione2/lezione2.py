# Leonardo Marianella
# 17/04/2024

print("Hello World!")

#2-3. Personal Message: Use a variable to represent a person’s name,
#and print a message to that person. Your message should be simple, 
#such as, “Hello Eric, would you like to learn some Python today?”

name: str = "Maria"
message: str = f"Ciao {name}, ti va di imparare un po di python insieme?"
print(message)


#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.


print(str.lower(name))
print(str.upper(name))
print(str.title(name))


#2-5.2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message. 



author_name: str = "Davide Pappacena"
quote: str = "\"una chiave che apre tante porte e' una buona chiave, una porta che si fa aprire da tante chiavi e' una cattiva porta\""
print (f"{author_name} una volta disse: {quote}")


#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.



filename: str = "lezioneCyber.py"
nosuffix: str = filename.removesuffix(".py")
print(nosuffix)


#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.



name10: list = ["mario","daniele","valerio"]
for i in name10:
    print(i)


#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.



msg: str = "left the chat"
name10: list = ["mario","daniele","valerio"]
for i in name10:
    print(i,msg)



#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”



MyList: list = ["Automobile","Aereo","Bicicletta","Motocicletta"]
brand: int = 0
for brand in MyList:
    print("Mi piacerebbe possedere ", brand)


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.


ListInviti: list = ["Einstein","Dante","whashington","Al Qaida"]
messaggioInvitati: str = "Egregio signore:"
messaggioInvitati1: str = "e' invitato al rave"
for invitato in ListInviti:
    print("{} {} {}".format(messaggioInvitati,invitato,messaggioInvitati1))



#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.


print("{}".format(ListInviti[2]))
ListInviti.pop(2)
ListInviti.insert(2,"Bruce Lee")
print(ListInviti)


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.


print("I found a bigger table")
ListInviti.insert(4,"Colombo")
ListInviti.insert(2,"Pablo Escobar")
ListInviti.append("Merluzzo")
messaggioInvitati: str = "Egregio signore:"
messaggioInvitati1: str = "e' invitato al rave al nuovo tavolo"
for invitato in ListInviti:
    print("{} {} {}".format(messaggioInvitati,invitato,messaggioInvitati1))



#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.



print("I'm sorry but i can only invite 2 people")
msmInvitati30: str = "I'm sorry but you can't come anymore"
nCome: int = 0

for k in range(5): #ListInviti:
    ListInviti.pop(0)
    print(msmInvitati30,ListInviti[0])


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.


WorldList: list = ["Tokyo", "New York", "Cairo","Londra","Amsterdam"]
print("originale: ",WorldList)
print("Ordine alfabetico: ",sorted(WorldList))
print("Originale: ",WorldList)
#WorldL1: list = WorldList.copy()
sorted(WorldList, reverse=True)
print("Ordine alfabetico invertito sorted: ",sorted(WorldList, reverse=True))
print("Originale: ",WorldList)
WorldList.reverse()
print(f"Ordine invertito metodo reverse: {WorldList}")
WorldList.reverse()
print(f"Ordine originale metodo reverse: {WorldList}")
WorldList.sort()
print(f"Lista con metodo sort in ordine alfabetico {WorldList}")
WorldList.sort(reverse=True)
print(f"Lista in ordine alfabetico invertito: {WorldList}")



#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.



NumeroPaesi: int = len(WorldList)
print(f"il numero di citta e': {NumeroPaesi}")



#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.



print("ESERCIZIO 3.10")
GamesList: list = ["Fallout4", "Rainbow", "Bannerloard", "Squad", "Arma3", "Horizon", "GTA5"]
print("Ordine alfabetico: ", sorted(GamesList))
print("Nuovo gioco!")
GamesList.append("RDR2")
print(GamesList)
print("Nuovo gioco nella lista!")
GamesList.insert(4, "Boarderlands4")
print(GamesList)
print("un gioco e' stato rimosso!")
GamesList.pop(7)
print("Giochi in varie forme:")
for gioco in GamesList:
    print(str.lower(gioco))
    print(str.upper(gioco))
    print(str.title(gioco))
print("lunghezza lista:", len(GamesList))
GamesList.reverse()
print(f"Ordine invertito metodo reverse: {GamesList}")
GamesList.reverse()
print(f"Ordine originale metodo reverse: {GamesList}")
GamesList.sort()
print(f"Lista con metodo sort in ordine alfabetico {GamesList}")
GamesList.sort(reverse=True)
print(f"Lista in ordine alfabetico invertito: {GamesList}")