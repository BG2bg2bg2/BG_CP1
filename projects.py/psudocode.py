#BG 1st pseudocode to code with persistent room state and enemy boosts

import random as r

# Data
room = ["Earth", "LA", "UA", "Quip", "LASS", "IPLA", "BLAT", "Uit", "HIPOS"]

# Display all rooms
def rooms():
    for i, room_name in enumerate(room, start=1):
        print(f'{i}: {room_name}')

# Room data
def roomers():
    return [
        {"room": "Earth", "stuff": ["plasma gun"], "enemy": None},
        {"room": "LA", "stuff": ["jetpack"], "enemy": None},
        {"room": "UA", "stuff": [], "enemy": "scout"},
        {"room": "Quip", "stuff": [], "enemy": 'friends'},
        {"room": "LASS", "stuff": ["drone"], "enemy": 'GLARB'},
        {"room": "IPLA", "stuff": [], "enemy": "scout"},
        {"room": "BLAT", "stuff": ['book'], "enemy": None},
        {"room": "Uit", "stuff": ['ball_o_shield'], "enemy": None},
        {"room": "HIPOS", "stuff": ["portal"], "enemy": 'BOSS'}
    ]

# User stats
def user_stats():
    user_name = input("Enter a name for your character: ")
    return {
        "name": user_name,
        "health": 90,
        "speed": 2,
        "defence": 5,
        "strength": 10,
        "items": []
    }

# Item boosts


item_effects = {
    'portal': {'speed': 30, 'health': 10, 'strength': 40, 'defence': 10},
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
    "friends": {"health": r.randint(1,20), "speed": r.randint(1,20),"defence": r.randint(1,20) ,"strength": r.randint(1,20)},
    "GLARB": {"health": r.randint(200,2000), "speed": r.randint(1000,2000),"defence": r.randint(1000,2000) ,"strength": r.randint(1000,2000)},
    "BOSS": {"health": r.randint(10,20) * 6, "speed": r.randint(10,20) * 6,"defence": r.randint(10,20) * 6 ,"strength": r.randint(10,20) * 6}
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
    if enemy == "BOSS": return {"health": 70, "speed": 3, "defence": 2, "strength": 30}

# Combat
def do_combat(player, enemy_name):
    enemy = enemy_stats(enemy_name)
    print(f"Combat begins against {enemy_name}!")
    while player["health"] > 0 and enemy["health"] > 0:
        # player attack
        player_hit = r.randint(1, player["strength"] + player["speed"] * 2)
        enemy["health"] -= player_hit
        print(f"You hit {enemy_name} for {player_hit} damage.")
        if enemy["health"] <= 0:
            print(f"You defeated {enemy_name}!")
            if enemy_name == 'BOSS':
                    print("You won the game")
                    return
            else:
                boost_from_enemy(player, enemy_name)  # Boost stats on enemy defeat
                return

        # enemy attack
        enemy_hit = r.randint(1, enemy["strength"])
        print(f"Enemy hit: {enemy_hit}")
        block = r.randint(1, max(player["defence"] - player["speed"] + enemy["speed"] * 2, 0 + 3))
        print(f"block: {block}")
        damage = max(enemy_hit - block, 0)
        player["health"] -= damage
        print(f"{enemy_name} hits you for {damage} damage. Your health: {player['health']}\n")
        if player["health"] <= 0:
            print("You died!")
            return

# Visit room
def visit_room(player, room_number, game_rooms):
    chosen = game_rooms[room_number - 1]
    print(f"\nYou enter {chosen['room']}.")

    # Items
    if chosen["stuff"]:
        for item in chosen["stuff"][:]:
            print(f"You found {item} with boost: {item_effects.get(item, {})}")
            pick = input(f"Do you want to pick up {item}? (y/n): ")
            if pick.lower() == "y":
                player["items"].append(item)
                boost_stats(player, item)
                chosen["stuff"].remove(item)  # Remove item after pickup
            else:
                print(f"You leave the {item}.")

    # Enemy
    if chosen["enemy"]:
        print(f"You encounter an enemy: {chosen['enemy']}")
        fight_or_run = input("Fight or run? (f/r): ")
        if fight_or_run.lower() == "r":
            print("You run away!")
            return player
        do_combat(player, chosen["enemy"])
        chosen["enemy"] = None  
        # Remove enemy after defeat

    return player

# Main loop
playing = True
while playing:
    player = user_stats()
    user_health = player["health"]
    game_rooms = roomers()

    while user_health > 0:
        rooms()
        choose = input("Enter 'a' to list all rooms, 'b' to list your stats, or a number to enter a room: ")
        if choose.lower() == "a":
            for a in game_rooms:
                print(a)
        if choose == 'b':
            user_stats()
        else:
            if choose.isdigit():
                room_choice = int(choose)
                if 1 <= room_choice <= 9:
                    player = visit_room(player, room_choice, game_rooms)
                    user_health = player["health"]
                else:
                    print("Invalid room number.")
            else:
                print("Enter a valid number.")

    # Play again?
    if "BOSS"["health"] <= 0:
        print("You win!!!!!")
        

    while user_health <= 0:
        again = input("Continue? (yes, y / no, n): ").lower()
        if again in ["no", "n"]:
            playing = False
            break
        elif again in ["yes", "y"]:
            print("\nRestarting game...\n")
            break  
        else:
            print("Must enter a valid answer.")
            continue

print("\nGame Over.")
hi