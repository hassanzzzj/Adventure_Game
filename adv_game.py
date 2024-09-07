import random

def start_game():
    print("Welcome to 'The Lost Treasure'!")
    print("You find yourself in a dark, mysterious forest.")
    first_choice()

def first_choice():
    print("\nWhat do you want to do?")
    print("1. Walk down the path")
    print("2. Explore the forest")
    print("3. Turn back")

    choice = input("> ")

    if choice == "1":
        path_choice()
    elif choice == "2":
        explore_forest()
    elif choice == "3":
        print("You turned back and returned home. Game Over.")
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def path_choice():
    print("\nYou follow the winding path deeper into the forest.")
    print("You come across a fork in the road. Which way do you go?")
    print("1. Left")
    print("2. Right")
    print("3. Turn back")

    choice = input("> ")

    if choice == "1":
        print("You went left and fell into a pit. Game Over.")
    elif choice == "2":
        right_path()
    elif choice == "3":
        first_choice()
    else:
        print("Invalid choice. Please try again.")
        path_choice()

def right_path():
    print("\nYou take the path to the right. The forest grows darker.")
    print("You hear a strange sound in the distance. What do you do?")
    print("1. Investigate the sound")
    print("2. Continue down the path")
    print("3. Turn back")

    choice = input("> ")

    if choice == "1":
        investigate_sound()
    elif choice == "2":
        print("You walked into a dense thicket and got lost. Game Over.")
    elif choice == "3":
        path_choice()
    else:
        print("Invalid choice. Please try again.")
        right_path()

def investigate_sound():
    print("\nYou cautiously make your way towards the sound.")
    print("You realize it's a group of bandits gathered around a campfire.")
    print("They haven't noticed you yet. What do you do?")
    print("1. Attack the bandits")
    print("2. Sneak past them")
    print("3. Turn back")

    choice = input("> ")

    if choice == "1":
        attack_bandits()
    elif choice == "2":
        sneak_past()
    elif choice == "3":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        investigate_sound()

def attack_bandits():
    print("\nYou bravely attack the bandits!")
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        print("You defeated the bandits and found a treasure map! You can now continue your adventure.")
        treasure_map()
    else:
        print("The bandits overpower you. Game Over.")

def sneak_past():
    print("\nYou sneak past the bandits and continue down the path.")
    print("You reach a clearing with a glowing treasure chest in the center.")
    print("What do you do?")
    print("1. Open the chest")
    print("2. Leave it alone")

    choice = input("> ")

    if choice == "1":
        open_chest()
    elif choice == "2":
        print("You decided to leave the chest alone and continue your adventure. Game Over.")
    else:
        print("Invalid choice. Please try again.")
        sneak_past()

def open_chest():
    print("\nYou open the chest and find a magical amulet!")
    print("What do you want to do with the amulet?")
    print("1. Wear it")
    print("2. Keep it in your bag")
    print("3. Throw it away")

    choice = input("> ")

    if choice == "1":
        print("The amulet grants you the power of invisibility! You can now safely explore the forest.")
        explore_forest()
    elif choice == "2":
        print("You keep the amulet in your bag. It might come in handy later.")
        explore_forest()
    elif choice == "3":
        print("You threw away the amulet. You might regret that decision later.")
        explore_forest()
    else:
        print("Invalid choice. Please try again.")
        open_chest()

def treasure_map():
    print("\nYou study the treasure map and realize it leads to a hidden cave.")
    print("Do you want to follow the map?")
    print("1. Yes")
    print("2. No, continue exploring the forest")

    choice = input("> ")

    if choice == "1":
        print("You follow the map and discover the hidden cave filled with treasure! You win!")
    elif choice == "2":
        explore_forest()
    else:
        print("Invalid choice. Please try again.")
        treasure_map()

def explore_forest():
    print("\nYou wander deeper into the forest.")
    print("You come across a mysterious old man who offers you a riddle.")
    print("If you solve it, he will grant you a special item.")
    print("Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    
    answer = input("> ").strip().lower()

    if answer == "echo":
        print("Correct! The old man gives you a magical sword to aid you on your journey.")
        print("You can now choose to go back to the treasure chest or continue exploring.")
        print("1. Go back to the chest")
        print("2. Continue exploring")

        choice = input("> ")

        if choice == "1":
            sneak_past()
        elif choice == "2":
            print("You continue exploring and find a beautiful waterfall. You win!")
        else:
            print("Invalid choice. Please try again.")
            explore_forest()
    else:
        print("Incorrect! The old man disappears, leaving you alone in the forest.")
        print("You can either go back to the path or continue exploring.")
        print("1. Go back to the path")
        print("2. Continue exploring")

        choice = input("> ")

        if choice == "1":
            path_choice()
        elif choice == "2":
            print("You wander aimlessly and get lost. Game Over.")
        else:
            print("Invalid choice. Please try again.")
            explore_forest()

# Start the game
start_game()