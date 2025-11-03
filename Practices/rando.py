def start():
    print("You wake up in a small village. Do you:")
    print("1. Go outside")
    print("2. Go back to sleep")
    choice = input("> ")
    if choice == "1":
        outside()
    elif choice == "2":
        sleep()
    else:
        print("Invalid choice.")
        start()

def outside():
    print("You walk outside and see two paths. Do you:")
    print("1. Take the left path")
    print("2. Take the right path")
    choice = input("> ")
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice.")
        outside()

def sleep():
    print("You go back to sleep and never wake up.")
    ending1()

def left_path():
    print("You see a river. Do you:")
    print("1. Try to swim across")
    print("2. Walk along the river")
    choice = input("> ")
    if choice == "1":
        swim()
    elif choice == "2":
        walk_river()
    else:
        print("Invalid choice.")
        left_path()

def right_path():
    print("You find a cave. Do you:")
    print("1. Go inside")
    print("2. Keep walking past it")
    choice = input("> ")
    if choice == "1":
        cave()
    elif choice == "2":
        walk_past()
    else:
        print("Invalid choice.")
        right_path()

def swim():
    print("The current is too strong. You drown.")
    ending2()

def walk_river():
    print("You find a bridge and cross safely.")
    bridge()

def cave():
    print("You enter the cave and see a chest. Do you:")
    print("1. Open it")
    print("2. Ignore it")
    choice = input("> ")
    if choice == "1":
        chest()
    elif choice == "2":
        ignore_chest()
    else:
        print("Invalid choice.")
        cave()

def walk_past():
    print("You keep walking and find an old man. Do you:")
    print("1. Talk to him")
    print("2. Ignore him")
    choice = input("> ")
    if choice == "1":
        old_man()
    elif choice == "2":
        ignore_old_man()
    else:
        print("Invalid choice.")
        walk_past()

def chest():
    print("The chest was trapped! You die.")
    ending3()

def ignore_chest():
    print("You walk deeper and find treasure on the ground.")
    treasure()

def old_man():
    print("He gives you a map to a castle.")
    castle()

def ignore_old_man():
    print("You walk into the woods and get lost.")
    ending4()

def bridge():
    print("You see a farm nearby. Do you:")
    print("1. Visit the farm")
    print("2. Keep walking")
    choice = input("> ")
    if choice == "1":
        farm()
    elif choice == "2":
        keep_walking()
    else:
        print("Invalid choice.")
        bridge()

def farm():
    print("The farmer gives you food and a place to rest.")
    ending5()

def keep_walking():
    print("You walk for hours and find a small town.")
    town()

def treasure():
    print("You pick up the treasure and exit the cave safely.")
    ending6()

def castle():
    print("You reach the castle gate. Do you:")
    print("1. Knock on the door")
    print("2. Sneak in through a window")
    choice = input("> ")
    if choice == "1":
        knock()
    elif choice == "2":
        sneak()
    else:
        print("Invalid choice.")
        castle()

def knock():
    print("The guards welcome you in. You become a knight.")
    ending7()

def sneak():
    print("You are caught sneaking in and thrown in jail.")
    ending8()

def town():
    print("You visit the market and find a horse for sale. Do you:")
    print("1. Buy the horse")
    print("2. Walk away")
    choice = input("> ")
    if choice == "1":
        buy_horse()
    elif choice == "2":
        walk_away()
    else:
        print("Invalid choice.")
        town()

def buy_horse():
    print("You ride the horse to a mountain and live there peacefully.")
    ending9()

def walk_away():
    print("You wander too far and never find your way back.")
    ending10()

def ending1():
    print("Ending 1: You slept forever.")

def ending2():
    print("Ending 2: You drowned in the river.")

def ending3():
    print("Ending 3: You died from a trap.")

def ending4():
    print("Ending 4: You got lost in the woods.")

def ending5():
    print("Ending 5: You lived a peaceful farm life.")

def ending6():
    print("Ending 6: You became rich with treasure.")

def ending7():
    print("Ending 7: You became a knight.")

def ending8():
    print("Ending 8: You were thrown in jail.")

def ending9():
    print("Ending 9: You lived on a mountain.")

def ending10(): 
    print("Ending 10: You disappeared forever.")

start()






