
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

def total(pokemons):
    return int(pokemons["total"])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        pokemon_index = int(input("Choose your pokemon: "))
        print(pokemons[pokemon_index])
        pass
    elif choice == '2':
        pokemons.sort(key = total, reverse = True)
        print(pokemons[0:10])
        pass
    elif choice == '3':
        def total(pokemons):
            return int(pokemons["total"])
        pokemons.sort(key = total, reverse = False)
        print(pokemons[0:10])
        pass
    elif choice == '4':
        print("---POKEMON BATTLE---")
        player = int(input("Choose your pokemon for the battle: "))
        print(pokemons[player])
        print("...")
        print("Computer are choosing the pokemon")
        random_pokemons = random.sample(pokemons, 1)
        print("Computer chose ", random_pokemons)

        while player_health > 0 and enemy_health:
            print("")
            enemy_damage = pokemons[enemy].get("attack") - pokemons[player].get("defense") + random.randit(5, 20)
            player_health = pokemons[player].get("HP") - enemy_damage
            

        
        
        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")

