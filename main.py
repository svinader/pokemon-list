
import csv

pokemons = []
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. izdrukat pirmus 10")
    print("7. izdrukat pedejus 10") 
    print("8. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        index = int(input("What pokemons numbers you want to show?\n"))
        print(pokemons[index])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        newlist = []
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        let = input("What you want to show?\n")
        for x in pokemons:
            if let in x:
                newlist.append(x) 

        print(newlist)
        pass
    elif choice == '5':
        newlist = []
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        lenght = int(input("What you want to show?\n"))
        for pokemon in pokemons:
            if len(pokemon) == lenght:
                newlist.append(pokemon)

        print(newlist)
        pass
    elif choice == '6':
        print(pokemons[:10])
        pass
    elif choice == '7':
        print(pokemons[-10:-1])
        pass
    elif choice == '8':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
