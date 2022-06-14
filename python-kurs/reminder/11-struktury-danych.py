# Lista

# names_list = []
# names_list.append("Kamil")
# names_list.append("Mariusz")

# print(names_list)

# names_list = ["Kamil", "Mariusz", "Adam", "Kamil"]

# names_list.clear() # usówa z listy wszystkie elementy

# names_list.remove("Kamil") # usówa pierwsze wystąpienie danego elementu
# print(names_list)

# print(names_list)
# print()
# print(names_list.pop(0)) # zwraca elemen z listy i go usówa z listy
# print()
# print(names_list)

# names_list.reverse() # odwraca listę
# names_list.sort() # sortuje listę

# for name in names_list:
#     print(name)

# print(names_list[0]) # konkretny element listy

# print(names_list.count("Rafał")) # liczy ile razy dany element występuję w liście
# print(len(names_list)) # pokazuje długość listy

# mnaes_list2 = ["Dominik"]

# names_list3 = names_list + names_list2
# print(names_list3)

# names_list.sort(reverse=True) # posortowane odwrotnie
# print(names_list)

# Kropka - struktura niemutowalna

# person = ("Jakub","Samul", "29")

# print(person)

# Set - nie wyświetla duplikatów, nie są upożądkowane, muszą być niemutowalne,

# names_set = {"Kamil","Mariusz","Kamil"}

names_set = set()

# names_list = []
# names_tuple = ()

names_set.add("Kamil")  # dodaje element
names_set.add("Mariusz")  # dodaje element
# names_set.add(names_list) # nie można
# names_set.add(names_tuple)

# names_set.remove("Kamil") # usówa element
# names_set.discard("Mariusz") # usówa element


# print(names_set)
names_set2 = {"Mariusz", "Tytus"}

# names_set3 = names_set + names_set2 # błąd nie można setów łączyć za pomocą +

# names_set3 = names_set.union(names_set2) # union twoży nowy set

names_set.update(names_set2) # updejtuje już istniejący set 

for name in names_set:
    print(name)
