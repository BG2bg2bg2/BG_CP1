# BG 1st pseudocode to code

import random as r

# Data
room = ["Earth", "LA", "UA", "Quip", "LASS", "IPLA", "BLAT", "Uit", "HIPOS"]

# Display all rooms
def rooms():
    for i, room_name in enumerate(room, start=1):
        print(f'{i}: {room_name}')

help = """
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

# Room data
def roomers():
    return [
        {"room": "Earth\n", "stuff": ["plasma gun\n"], "enemy": 'scout\n', 'description': 'You see an object that had a blue scaner scanning you then showed in a 3D like object of you getting sucked into a spaceship but on your way up you got knocked out.\nAll at once the room went BLACK\n'},
        {"room": "LA\n", "stuff": ["jetpack\n"], "enemy": 'scout\n', 'description': 'You see a video of ships filled with people being transorted,\nbut you just know there must be a way for you to save them.\n'},
        {"room": "UA", "stuff": [], "enemy": "scout", 'description': "You press buttons until you pressed the '$' button then trouble happens...\nYou might have a chance to beat the BOSS now"},
        {"room": "Quip", "stuff": [], "enemy": 'friends', 'description': 'You should avoid the next room... The words hung in the air then was mealted into the floor'},
        {"room": "LASS", "stuff": ["drone"], "enemy": 'GLARB', 'description': "Run from me while you still can for I will kill you if you try to flee from the BOSS or kill the univers!"},
        {"room": "IPLA", "stuff": [], "enemy": "scout", "description": "Your not far from home just a few more light years at the speed of light and your home but you also need to avoid the BOSS"},
        {"room": "BLAT", "stuff": ['book'], "enemy": 'scout', "description": "You see ships with TVs on them with protests of banners thinking they are on strie but they are not instead they are protraying death to the BOSS"},
        {"room": "Uit", "stuff": ['ball_o_shield'], "enemy": "scout","enemy": "scout", 'description': 'A patrol scout sees you and you kill them but now the alarm sounded.\nYour introuble'},
        {"room": "HIPOS", "stuff": ["space_shoose"],"enemy": "scout", "enemy": 'BOSS'}
    ]

# User stats
def user_stats():
    user_name = input("Enter a name for your character: ")
    return {
        "name": user_name,
        "health": 50,
        "speed": 2,
        "defence": 5,
        "strength": 10,
        "items": []
    }

# Item boosts
item_effects = {
    'space_shoose': {'speed': 30, 'health': 10, 'strength': 40, 'defence': 10},
    "drone": {"speed": 12, "defence": 20, "strength": 25},
    "plasma gun": {"strength": r.randint(3, 9)},
    "jetpack": {"speed": r.randint(5, 9)},
    "book": {"strength": r.randint(4, 9), "defence": r.randint(5, 10)},
    "ball_o_shield": {"defence": r.randint(4, 9)}
}

# Boost stats from items
def boost_stats(player, item):
    if item in item_effects:
        boosts = item_effects[item]
        for stat, val in boosts.items():
            player[stat] += val
        print(f"{item} boosts your stats: {boosts}")

# Boost stats from defeating enemies
enemy_boosts = {
    "scout": {"strength": r.randint(1, 10), "speed": r.randint(0, 2)},
    "friends": {"health": r.randint(1,20), "speed": r.randint(1,20),
                "defence": r.randint(1,20), "strength": r.randint(1,20)},
    "GLARB": {"health": r.randint(200,2000), "speed": r.randint(1000,2000),
              "defence": r.randint(1000,2000), "strength": r.randint(1000,2000)},
    "BOSS": {"health": r.randint(10,20), "speed": r.randint(10,20),
             "defence": r.randint(10,20), "strength": r.randint(10,20)}
}

def boost_from_enemy(player, enemy_name):
    if enemy_name in enemy_boosts:
        boosts = enemy_boosts[enemy_name]
        for stat, val in boosts.items():
            player[stat] += val
        print(f"Defeating {enemy_name} boosts your stats: {boosts}")

# Enemy stats
def enemy_stats(enemy):
    if enemy == "scout": return {"health": 30, "speed": 1, "defence": 1, "strength": 5}
    if enemy == "friends": return {"health": 10, "speed": 10, "defence": 10, "strength": 10}
    if enemy == "GLARB": return {"health": 100, "speed": 300, "defence": 0, "strength": 34543}
    if enemy == "BOSS": return {"health": 90, "speed": 3, "defence": 2, "strength": 30}

# Combat
def do_combat(player, enemy_name):
    enemy = enemy_stats(enemy_name)
    print(f"Combat begins against {enemy_name}!")

    while player["health"] > 0 and enemy["health"] > 0:
        player_hit = r.randint(1, player["strength"] + player["speed"] * 2)
        enemy["health"] -= player_hit
        print(f"You hit {enemy_name} for {player_hit} damage.")

        if enemy["health"] <= 0:
            print(f"You defeated {enemy_name}!")
            if enemy_name == 'BOSS':
                print("You won the game")
                player['health'] = 0
            else:
                boost_from_enemy(player, enemy_name)
            return

        enemy_hit = r.randint(1, enemy["strength"])
        block = r.randint(1, max(player["defence"] - player["speed"] + enemy["speed"] * 2, 3))
        damage = max(enemy_hit - block, 0)
        player["health"] -= damage
        print(f"{enemy_name} hits you for {damage} damage. Your health: {player['health']}")

        if player["health"] <= 0:
            print("You died!")
            return

# Visit room
def visit_room(player, room_number, game_rooms):
    chosen = game_rooms[room_number - 1]
    print(f"\nYou enter {chosen['room']}.")
    for a in {chosen['room']}:
        print("description")

    if chosen["stuff"]:
        for item in chosen["stuff"][:]:
            print(f"You found {item} with boost: {item_effects.get(item, {})}")
            pick = input(f"Do you want to pick up {item}? (y/n): ")
            if pick.lower() == "y":
                player["items"].append(item)
                boost_stats(player, item)
                chosen["stuff"].remove(item)

    if chosen["enemy"]:
        print(f"You encounter an enemy: {chosen['enemy']}")
        fight_or_run = input("Fight or run? (f/r): ")
        if fight_or_run.lower() == "r":
            print("You run away!")
            return player
        do_combat(player, chosen["enemy"])
        chosen["enemy"] = None

    return player

# Main loop
playing = True
while playing:
    print(help)
    player = user_stats()
    user_health = player["health"]
    game_rooms = roomers()

    while user_health > 0:
        rooms()
        choose = input("Enter 'a' to list all rooms, 'b' to list your stats, 'c' for help, or a number to enter a room: ")

        if choose.lower() == "a":
            for a in game_rooms:
                print(a)

        elif choose == 'b':
            print(player)

        elif choose == 'c':
            print(help)

        elif choose.isdigit():
            room_choice = int(choose)
            if 1 <= room_choice <= 9:
                player = visit_room(player, room_choice, game_rooms)
                user_health = player["health"]
            else:
                print("Invalid room number.")



        else:
            print("Enter a valid number.")

    again = input("Continue? (yes, y / no, n): ").lower()
    if again not in ["yes", "y"]:
        playing = False

print("\nGame Over.")
