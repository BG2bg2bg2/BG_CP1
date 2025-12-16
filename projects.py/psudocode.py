import random as r

# Data
room = ["Earth", "LA", "UA", "Quip", "LASS", "IPLA", "BLAT", "Uit", "HIPOS"]

# Display all rooms
def rooms():
    for i, room_name in enumerate(room, start=1):
        print(f'{i}: {room_name}')

HELP = """
You have to choose a letter 
when you are asked to collect an item
y for collect it
n for leave it
when you are asked to attack
f for fight
r for run
'a' to show the 'map' of the place
'b' to list your stats of how much damage and health you have
'c' to come back this
'1' to Enter room 1
'2' to enter room 2
'3' to enter room 3
'4' to enter room 4
'5' to enter room 5
'6' to enter room 6
'7' to enter room 7
'8' to enter room 8
'9' to enter room 9
"""

def roomers():
    # Return fresh copy of rooms (resets items and enemies)
    return [
        {"room": "Earth", "stuff": ["plasma gun"], "enemy": "scout",
         "description": "You see an object that had a blue scaner scanning you then showed in a 3D like object of you getting sucked into a spaceship but on your way up you got knocked out.\nAll at once the room went BLACK\n"},
        {"room": "LA", "stuff": ["jetpack"], "enemy": "scout",
         "description": "You see a video of ships filled with people being transorted,\nbut you just know there must be a way for you to save them.\n"},
        {"room": "UA", "stuff": [], "enemy": "scout",
         "description": "You press buttons until you pressed the '$' button then trouble happens...\nYou might have a chance to beat the BOSS now"},
        {"room": "Quip", "stuff": [], "enemy": "friends",
         "description": "You should avoid the next room... The words hung in the air then was mealted into the floor"},
        {"room": "LASS", "stuff": ["drone"], "enemy": "GLARB",
         "description": "Run from me while you still can for I will kill you if you try to flee from the BOSS or kill the univers!"},
        {"room": "IPLA", "stuff": [], "enemy": "scout",
         "description": "Your not far from home just a few more light years at the speed of light and your home but you also need to avoid the BOSS"},
        {"room": "BLAT", "stuff": ["book"], "enemy": "scout",
         "description": "You see ships with TVs on them with protests of banners thinking they are on strie but they are not instead they are protraying death to the BOSS"},
        {"room": "Uit", "stuff": ["ball_o_shield"], "enemy": "scout",
         "description": "A patrol scout sees you and you kill them but now the alarm sounded.\nYour introuble"},
        {"room": "HIPOS", "stuff": ["space_shoose"], "enemy": "BOSS",
         "description": "The final chamber hums with power. The BOSS stands before you."}
    ]

def user_stats():
    user_name = input("Enter a name for your character: ")
    return {"name": user_name, "health": 50, "speed": 2, "defence": 5, "strength": 10, "items": []}

item_effects = {
    "space_shoose": {"speed": 30, "health": 10, "strength": 40, "defence": 10},
    "drone": {"speed": 12, "defence": 20, "strength": 25},
    "plasma gun": {"strength": r.randint(3, 9)},
    "jetpack": {"speed": r.randint(5, 9)},
    "book": {"strength": r.randint(4, 9), "defence": r.randint(5, 10)},
    "ball_o_shield": {"defence": r.randint(4, 9)}
}

def boost_stats(player, item):
    if item in item_effects:
        for stat, val in item_effects[item].items():
            player[stat] += val
        print(f"{item} boosts your stats: {item_effects[item]}")

def enemy_stats(enemy):
    if enemy == "scout":
        return {"health": 30, "speed": 1, "defence": 1, "strength": 5}
    if enemy == "friends":
        return {"health": 10, "speed": 10, "defence": 10, "strength": 10}
    if enemy == "GLARB":
        return {"health": 100, "speed": 300, "defence": 0, "strength": 34543}
    if enemy == "BOSS":
        return {"health": 100, "speed": 3, "defence": 2, "strength": 30}

def do_combat(player, enemy_name):
    enemy = enemy_stats(enemy_name)
    print(f"Combat begins against {enemy_name}!")

    while player["health"] > 0 and enemy["health"] > 0:
        player_hit = r.randint(1, player["strength"] + player["speed"] * 2)
        enemy["health"] -= player_hit
        print(f"You hit {enemy_name} for {player_hit} damage.")

        if enemy["health"] <= 0:
            print(f"You defeated {enemy_name}!")
            if enemy_name == "BOSS":
                print("You won the game!")
                player["health"] = 0
            if enemy_name == "GLARB":
                print("You get extra points for killing GLARB")
                player["health"] = 100
            return

        enemy_hit = r.randint(1, enemy["strength"])
        block = r.randint(1, max(player["defence"] - player["speed"] + enemy["speed"] * 2, 3))
        damage = max(enemy_hit - block, 0)
        player["health"] -= damage
        print(f"{enemy_name} hits you for {damage} damage. Your health: {player['health']}")

        if player["health"] <= 0:
            print("You died!")
            return

def visit_room(player, room_number, game_rooms):
    chosen = game_rooms[room_number - 1]
    print(f"\nYou enter {chosen['room']}.")
    print(chosen["description"])

    if chosen["stuff"]:
        for item in chosen["stuff"][:]:
            print(f"You found {item}")
            pick = input(f"Do you want to pick up {item}? (y/n): ").lower()
            if pick == "y":
                player["items"].append(item)
                boost_stats(player, item)
                chosen["stuff"].remove(item)
        for item in chosen["stuff"][:]:
            item.list(["stuff"])[:]

    if chosen["enemy"]:
        print(f"You encounter an enemy: {chosen['enemy']}")
        fight_or_run = input("Fight or run? (f/r): ").lower()
        if fight_or_run == "f":
            do_combat(player, chosen["enemy"])
        elif fight_or_run == "r":
            print("You run away safely!")
        chosen["enemy"] = None

    return player

while True:
    # Outer loop for restarting
    player = user_stats()
    game_rooms = roomers()  
    # Reset rooms for a fresh game

    while player["health"] > 0:
        print(HELP)
        rooms()
        choose = input("Enter 'a' to list all rooms, 'b' to list your stats, 'c' for help, or a number to enter a room: ").lower()

        if choose == "a":
            for rdata in game_rooms:
                print(rdata['room'])

        elif choose == "b":
            print(player)

        elif choose == "c":
            print(HELP)

        elif choose.isdigit():
            room_choice = int(choose)
            if 1 <= room_choice <= 9:
                player = visit_room(player, room_choice, game_rooms)
            else:
                print("Invalid room number.")

        else:
            print("Enter a valid option.")

    # Game over
    print("\nGame Over.")

    # Ask to restart
    restart = input("Do you want to restart the game? (yes/y or no/n): ").lower()
    if restart not in ["yes", "y"]:
        print("Thanks for playing!")
        break