#JSON
import json                        

def read_pokemon():   
    try:
        with open('pokemon_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return initial_pokemon
    
initial_pokemon = [             
    {
        "name": {
            "english": "Pikachu"
        },
        "type": [
            "Electric"
        ],
        "base": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "Sp. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90
        }
    },
    {
        "name": {
            "english": "Charmander"
        },
        "type": [
            "Fire"
        ],
        "base": {
            "HP": 39,
            "Attack": 52,
            "Defense": 43,
            "Sp. Attack": 60,
            "Sp. Defense": 50,
            "Speed": 65
        }
    },
    {
        "name": {
            "english": "Squirtle"
        },
        "type": [
            "Water"
        ],
        "base": {
            "HP": 44,
            "Attack": 48,
            "Defense": 65,
            "Sp. Attack": 50,
            "Sp. Defense": 64,
            "Speed": 43
        }
    }
]


def menu():          
    while True:
        print("----- Pokémon Menu -----")
        print("1. Add a new Pokémon")
        print("2.        Exit        ")
        try: 
            choice = input("Please select an option (1 or 2): ")
            if choice == '1':
                add_pokemon()                                   
            elif choice == '2':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ex:   
            print(f"You did not enter a number: {ex}")
            print("Please try again.") 


def save_pokemon(python_object):                     
    with open('pokemon_data.json', 'w') as file:               
        json.dump(python_object, file, indent=4) 

        
def add_pokemon():    
    initial_pokemon=read_pokemon()
    english_name = input("Please enter the English name of the new Pokemon: ")           
    types_input = input("Please enter the types of the new Pokémon, separated by commas: ")
    hp = int(input("Enter the HP of the new Pokémon: "))
    attack = int(input("Enter the Attack of the new Pokémon: "))
    defense = int(input("Enter the Defense of the new Pokémon: "))
    sp_attack = int(input("Enter the Special Attack of the new Pokémon: "))
    sp_defense = int(input("Enter the Special Defense of the new Pokémon: "))
    speed = int(input("Enter the Speed of the new Pokémon: "))
    new_pokemon = {                                           
        "name": {
            "english": english_name
        },
        "type": types_input,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    initial_pokemon.append(new_pokemon) 
    save_pokemon(initial_pokemon)  


menu()