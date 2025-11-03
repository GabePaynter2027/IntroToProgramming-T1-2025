def game_intro():
    print("         WELCOME TO THE LOST CAVE       ")
    print("You are about to embark on a mysterious journey full of danger, treasure, and discovery.")
    print("Your choices will decide your fate. There are many endings — can you find them all?")
    print("Type numbers to make choices. Choose wisely!\n")
    input("Press Enter to begin your adventure... ")
    start()


def start():
    print("\nYou wake up at the edge of a dark cave. A cold wind blows from within.")
    print("1. Enter the cave")
    print("2. Walk away into the forest")
    choice = input("> ")

    if choice == "1":
        cave_entrance()
    elif choice == "2":
        forest_path()
    else:
        print("Invalid choice. Try again.")
        start()


# 1
def cave_entrance():
    print("\nYou step into the cave. It's dark and damp. You see two tunnels.")
    print("1. Go left toward a faint light")
    print("2. Go right into the darkness")
    choice = input("> ")

    if choice == "1":
        glowing_room()
    elif choice == "2":
        dark_tunnel()
    else:
        print("Invalid choice. Try again.")
        cave_entrance()


# 2
def glowing_room():
    print("\nYou enter a glowing chamber filled with crystals.")
    print("1. Take a glowing crystal")
    print("2. Ignore them and move on")
    print("3. Look around for hidden objects")
    choice = input("> ")

    if choice == "1":
        print("You take a crystal. It might come in handy.")
        dark_bridge(True)
    elif choice == "2":
        dark_bridge(False)
    elif choice == "3":
        mysterious_statue()
    else:
        print("Invalid choice.")
        glowing_room()


# 3
def dark_tunnel():
    print("\nYou walk into total darkness and trip over a rock.")
    print("1. Get up and continue")
    print("2. Go back to the entrance")
    choice = input("> ")

    if choice == "1":
        underground_lake()
    elif choice == "2":
        cave_entrance()
    else:
        print("Invalid choice.")
        dark_tunnel()


# 4
def dark_bridge(has_crystal):
    print("\nYou reach a shaky wooden bridge over a deep pit.")
    print("1. Cross carefully")
    print("2. Shout to test how deep it is")

    choice = input("> ")
    if choice == "1":
        if has_crystal:
            print("The crystal lights your way — you cross safely.")
            treasure_chamber()
        else:
            print("You slip in the darkness and fall.")
            ending_fall()
    elif choice == "2":
        echo_monster()
    else:
        print("Invalid choice.")
        dark_bridge(has_crystal)


# 5
def forest_path():
    print("\nYou walk away from the cave and into the woods.")
    print("You see smoke rising in the distance.")
    print("1. Investigate the smoke")
    print("2. Keep walking the other way")
    choice = input("> ")

    if choice == "1":
        campfire_scene()
    elif choice == "2":
        lost_in_forest()
    else:
        print("Invalid choice.")
        forest_path()


# 6
def underground_lake():
    print("\nYou find an underground lake glowing faintly.")
    print("1. Swim across")
    print("2. Walk around the edge")
    print("3. Sit and rest for a moment")
    choice = input("> ")

    if choice == "1":
        water_monster()
    elif choice == "2":
        secret_tunnel()
    elif choice == "3":
        hidden_library()
    else:
        print("Invalid choice.")
        underground_lake()


# 7
def echo_monster():
    print("\nYour echo wakes something in the darkness...")
    print("A huge bat swoops down!")
    print("1. Run away")
    print("2. Fight it with a stick")
    choice = input("> ")

    if choice == "1":
        cave_entrance()
    elif choice == "2":
        ending_eaten()
    else:
        print("Invalid choice.")
        echo_monster()


# 8
def treasure_chamber():
    print("\nYou find a massive golden chest!")
    print("1. Open the chest")
    print("2. Leave it alone")
    print("3. Look around the room first")
    choice = input("> ")

    if choice == "1":
        trapped_room()
    elif choice == "2":
        peaceful_exit()
    elif choice == "3":
        crystal_guardian()
    else:
        print("Invalid choice.")
        treasure_chamber()


# 9
def trapped_room():
    print("\nThe chest was a trap! The walls begin closing in.")
    print("1. Try to escape")
    print("2. Accept your fate")
    choice = input("> ")

    if choice == "1":
        escape_tunnel()
    elif choice == "2":
        ending_crushed()
    else:
        print("Invalid choice.")
        trapped_room()


# 10
def peaceful_exit():
    print("\nYou leave the treasure untouched and find a gentle slope upward.")
    print("You emerge safely into sunlight.")
    ending_peaceful()


# 11
def escape_tunnel():
    print("\nYou crawl through a narrow escape tunnel and see light ahead.")
    print("1. Go toward the light")
    print("2. Turn around")
    choice = input("> ")

    if choice == "1":
        ending_hero()
    elif choice == "2":
        ending_lost()
    else:
        print("Invalid choice.")
        escape_tunnel()


# 12
def campfire_scene():
    print("\nYou find a group of travelers by a campfire.")
    print("1. Talk to them")
    print("2. Steal their food and run")
    choice = input("> ")

    if choice == "1":
        travelers_help()
    elif choice == "2":
        ending_caught()
    else:
        print("Invalid choice.")
        campfire_scene()


# 13
def travelers_help():
    print("\nThe travelers share food and tell you about a nearby village.")
    print("1. Go to the village")
    print("2. Stay and rest with them")
    choice = input("> ")

    if choice == "1":
        village_gate()
    elif choice == "2":
        peaceful_ending_travelers()
    else:
        print("Invalid choice.")
        travelers_help()


# 14
def village_gate():
    print("\nYou reach the village gate. Guards stop you.")
    print("1. Ask for shelter")
    print("2. Attack them")
    choice = input("> ")

    if choice == "1":
        ending_safe_village()
    elif choice == "2":
        ending_prison()
    else:
        print("Invalid choice.")
        village_gate()


# 15
def lost_in_forest():
    print("\nYou wander aimlessly in the forest until night falls.")
    ending_lost()


# 16
def secret_tunnel():
    print("\nYou find a secret tunnel behind the lake!")
    print("1. Enter the tunnel")
    print("2. Go back")
    choice = input("> ")

    if choice == "1":
        treasure_chamber()
    elif choice == "2":
        dark_tunnel()
    else:
        print("Invalid choice.")
        secret_tunnel()


# 17
def water_monster():
    print("\nSomething grabs your leg under the water!")
    print("1. Kick and fight")
    print("2. Let it pull you down")
    choice = input("> ")

    if choice == "1":
        ending_freedom()
    elif choice == "2":
        ending_drowned()
    else:
        print("Invalid choice.")
        water_monster()


# 18
def mysterious_statue():
    print("\nYou find an ancient statue with glowing eyes.")
    print("1. Touch the statue")
    print("2. Bow to it respectfully")
    print("3. Smash it with a rock")
    choice = input("> ")

    if choice == "1":
        hidden_library()
    elif choice == "2":
        treasure_chamber()
    elif choice == "3":
        ending_cursed()
    else:
        print("Invalid choice.")
        mysterious_statue()


# 19 
def hidden_library():
    print("\nYou stumble into an ancient underground library full of scrolls.")
    print("1. Read a scroll")
    print("2. Search for a secret exit")
    choice = input("> ")

    if choice == "1":
        ending_wisdom()
    elif choice == "2":
        hidden_exit()
    else:
        print("Invalid choice.")
        hidden_library()


# 20 
def crystal_guardian():
    print("\nA giant guardian made of crystal rises from the floor!")
    print("1. Show it your glowing crystal")
    print("2. Run away")
    print("3. Attack it")
    choice = input("> ")

    if choice == "1":
        ending_guardian_peace()
    elif choice == "2":
        dark_tunnel()
    elif choice == "3":
        ending_guardian_anger()
    else:
        print("Invalid choice.")
        crystal_guardian()


def hidden_exit():
    print("\nBehind a pile of books, you find a narrow tunnel leading upward.")
    print("You crawl for what feels like hours and finally see daylight.")
    ending_escape()


def ending_fall():
    print("\nYou fall into the pit and never climb out. THE END.")
    restart_option()


def ending_crushed():
    print("\nThe walls crush you in the trapped room. THE END.")
    restart_option()


def ending_eaten():
    print("\nThe bat tears you apart. THE END.")
    restart_option()


def ending_peaceful():
    print("\nYou walk away peacefully, wiser for your choices. THE END.")
    restart_option()


def ending_hero():
    print("\nYou escape the cave and become a local hero! THE END.")
    restart_option()


def ending_lost():
    print("\nYou wander forever, lost in darkness. THE END.")
    restart_option()


def ending_caught():
    print("\nThe travelers catch you stealing and tie you up. THE END.")
    restart_option()


def ending_safe_village():
    print("\nThe guards welcome you. You live happily in the village. THE END.")
    restart_option()


def ending_prison():
    print("\nThe guards overpower you and throw you in prison. THE END.")
    restart_option()


def ending_freedom():
    print("\nYou defeat the monster and swim to safety. THE END.")
    restart_option()


def ending_drowned():
    print("\nThe creature drags you under, and you drown. THE END.")
    restart_option()


def peaceful_ending_travelers():
    print("\nYou live a quiet, peaceful life with the travelers. THE END.")
    restart_option()


def ending_cursed():
    print("\nThe statue curses you. You slowly turn to stone. THE END.")
    restart_option()


def ending_wisdom():
    print("\nYou gain ancient knowledge that changes your mind forever. THE END.")
    restart_option()


def ending_guardian_peace():
    print("\nThe guardian bows and lets you pass to the treasure beyond. You are rich! THE END.")
    restart_option()


def ending_guardian_anger():
    print("\nThe guardian smashes you with one mighty blow. THE END.")
    restart_option()


def ending_escape():
    print("\nYou escape through the hidden tunnel and breathe fresh air again. THE END.")
    restart_option()


def restart_option():
    print("\nWould you like to play again?")
    print("1. Yes")
    print("2. No")
    choice = input("> ")

    if choice == "1":
        start()
    elif choice == "2":
        print("\nThanks for playing The Lost Cave! Goodbye!")
    else:
        print("Invalid choice.")
        restart_option()


game_intro()