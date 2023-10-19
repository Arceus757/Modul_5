# # Skapa em lista med namn

# mylist = ["apple", "banana", "kiwi", "cherry"]


# # Ändra det första namnet
# mylist[0] = "grape"

# # Lägg till ett nytt namn
# new_fruits = "pear"
# mylist.append(new_fruits)

# # Skriv ut den uppdaterade listan
# print(mylist)

# antal_frukter = len(mylist)
# print(f"Antal frukter i listan: {antal_frukter}")

# # Ta bort en frukt  med pop()
# borttaget_frukt = mylist.pop(1)  # Tar bort den andra frukten
# print(f"Borttaget namn: {borttaget_frukt}")

# Skriv ut den uppdaterade listan

mina_frukter = ["apple", "banana", "cherry"]

while True:
    print(f"Aktuella frukter: {mina_frukter}")
    print("1. Lägg till en frukt")
    print("2. Ta bort en frukt")
    print("3. Avsluta")
    val = input("Vad vill du göra? |1|2|3| : ")

    if val == "1":
        ny_frukt= input("Skriv in en ny frukt: ")
        mina_frukter.append(ny_frukt)
    elif val == "2":
        if len(mina_frukter) > 0:
            print(f"Aktuella frukter: {mina_frukter}")
            index = int(input("Ange index för frukten du vill ta bort: "))
            if index >= 0 and index < len(mina_frukter):
                borttaget_frukt = mina_frukter.pop(index)
                print(f"{borttaget_frukt} har tagits bort.")
            else:
                print("Ogiltigt index.")
        else:
            print("Det finns inga frukter att ta bort.")
    elif val == "3":
        break
    else:
        print("Ogiltigt val. Försök igen.")

print(f"Slutgiltiga frukter: {mina_frukter}")

# my_fav_car = {"Weight" : "5-7t", "lenght" : "3.8m", "number_of_seats" : "4"}
# print(my_fav_car["number_of_seats"])