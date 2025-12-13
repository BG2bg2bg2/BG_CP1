#BG 1st Testing lime
import random as r

# list room
room = ["Earth", "LA", "UA", "Quip", "LASS", "IPLA", "BLAT", "Uit", "HIPOS"]

# display all rooms
def rooms():
    for i, room_n in enumerate(room, start=1):
        print(f'{i}: {room_n}')



# room stuff

def roomers():

    return [
        {"room": "Earth, Where you were BORN", "stuff": ["note"], "enemy": None},
        {"room": "LA, WHERE YOU EXPLORE", "stuff": ["jetpack"], "enemy": None},
        {"room": "UA: No problem getting stuck", "stuff": [], "enemy": "scout"},
        {"room": "Quip", "stuff": ["book1"], "enemy": 'friends'},
        {"room": "LASS: Fear GLARB AT ALL COST", "stuff": [], "enemy": 'GLARB'},
        {"room": "IPLA", "stuff": [], "enemy": "scout"},
        {"room": "BLAT", "stuff": ['book2'], "enemy": None},
        {"room": "Uit", "stuff": ['ball_o_shield'], "enemy": None},
        {"room": "HIPOS", "stuff": [], "enemy": 'BOSS'}
    ]



# user stats

def user_stats():
    user = input("Enter a nickname: ")
    return {
        "name": user,
        "health": 90,
        "speed": 2,
        "defence": 5,
        "strength": 10,
        "items": []

    }


# @=a #=B $=C %=D ^=E &=F *=G (=H )=I _=J +=K -=L ==M [=N ]=O {=P }= Q ;=R '=S :=T ,=U .=V /=W ?=X <=Y >=Z
# A=1 B=2 C=3 D=4 
# item boosts

item_effects = {
    "note": "You are on your way to victory, but AVOID GLARB. and use this info\n@A  #B  $C\n%D  ^E  &F\n Find the rest\n*()_+-=[];':,./?<>",
    "gun": {"strength": r.randint(3, 9)},
    "jetpack": {"speed": r.randint(5, 9)},
    "book1": "Look at this? You see symbols that you think you have a clue...?\n\n@#$%^&*()_+-=[];':,./?<>\n\nYou flip the pages and run into\n\n- .... . / -... --- ... ... / .. ... / .- - / ..... ----- / .... . .- .-.. - .... / -.-. .- -. / -.-- --- ..- / -.. . ..-. . .- - / .... .. -- / .-- .. - .... / .--- ..- ... - / - .... . / ... - .- - ... / -.-- --- ..- / .... .- ...- . ..--.. / .--. .-.-.- ... .-.-.- / - .... . / ... -.-- -- -... --- .-.. ... / -.-. --- .-. .-. . ... .--. --- -. -.. ... / - --- / .- / .-.. . - - . .-. / .--.-. / .- ... / .-\n\n.- -...- .---- / -... -...- ..--- / -.-. -...- ...-- / -.. -...- ....- / .--- -...- .---- ----- / ..- -...- ..--- ----- / ...- -...- ..--- .---- / --.. -...- ..--- -....\n\n.- -...- ----- / -... -...- .---- / -.-. -...- ..--- / -.. -...- ...-- / -.- -...- .---- ----- / -.- .- -...- .---- .---- / -.- -.- -...- ..--- ----- / --- .-. / ..- -...- ..--- -----\n\n You emediately understood what it was saying even though you don't have google availible you still use what you have and fliped to another page and read\n\n:(^ #]'' )' @: UUK (^@-:(\n\n*-@;# @: UUUUUUU (^@-:(",
    "book2": ".- / -... / -.-. / -.. / . / ..-. / --. / .... / .. / .--- / -.- / .-.. / -- / -. / --- / .--. / --.- / .-. / ... / - / ..- / ...- / .-- / -..- / -.-- / --..\n\n 'This Looks Familiar...\n...\n... I know I need to get/read book1 too",
    "ball_o_shield": {"defence": r.randint(4, 9)}
}



# stats from items

def boost_stats(player, item):
    boosts = item_effects[item]
    if isinstance(boosts, dict):

        for stat, val in boosts.items():
            player[stat] += val
        print(f"{item} boosts your stats: {boosts}")
    else:
        print(boosts)


# boost stats from defeating enemies

enemy_boosts = {
    "scout": {"strength": r.randint(1, 10), "speed": r.randint(0, 2)},
    "friends": {"health": r.randint(1, 20), "speed": r.randint(1, 20),
                "defence": r.randint(1, 20), "strength": r.randint(1, 20)},
    "GLARB": {"health": r.randint(100, 200), "speed": r.randint(100, 200),
              "defence": r.randint(100, 200), "strength": r.randint(100, 200)},
    "BOSS": {"health": r.randint(10, 20) * 6, "speed": r.randint(10, 20) * 6,
             "defence": r.randint(10, 20) * 6, "strength": r.randint(10, 20) * 6}
}



def boost_from_enemy(player, enemy_name):
    boosts = enemy_boosts[enemy_name]
    for stat, val in boosts.items():
        player[stat] += val
    print(f"Defeating {enemy_name} boosts your stats: {boosts}")
    print(player[stat])



# enemy stats
def enemy_stats(enemy):
    if enemy == "scout": return {"health": 30, "speed": 1, "defence": 1, "strength": 5}
    if enemy == "friends": return {"health": 10, "speed": 10, "defence": 10, "strength": 10}
    if enemy == "GLARB": return {"health": 10, "speed": 300, "defence": 0, "strength": 34543}
    if enemy == "BOSS": return {"health": 70, "speed": 3, "defence": 2, "strength": 30}

# combat

def do_combat(player, enemy_name):
    enemy = enemy_stats(enemy_name)
    print(f"Combat begins against {enemy_name}!")

    while player["health"] > 0 and enemy["health"] > 0:
        player_hit = r.randint(1, player["strength"] + player["speed"] * 2)
        enemy["health"] -= player_hit
        print(f"You hit {enemy_name} for {player_hit} damage.")
        if enemy["health"] <= 0:
            print(f"You defeated {enemy_name}!")
            boost_from_enemy(player, enemy_name)
            return True

        enemy_hit = r.randint(1, enemy["strength"])
        block = r.randint(0, max(player["defence"], 1))
        damage = max(enemy_hit - block, 0)
        player["health"] -= damage
        print(f"{enemy_name} hits you for {damage}. Health: {player['health']}")
    return False



# visit room
def visit_room(player, room_number, game_rooms):
    chosen = game_rooms[room_number - 1]
    print(f"\nYou enter {chosen['room']}.")

    # items
    for item in chosen["stuff"][:]:
        print(f"You found {item}: {item_effects[item]}")
        if input("Pick up? (y/n): ").lower() == "y":
            player["items"].append(item)
            boost_stats(player, item)
            chosen["stuff"].remove(item)
    # enemy
    if chosen["enemy"]:
        print(f"You encounter {chosen['enemy']}")
        if input("Fight or run? (f/r): ").lower() == "r":
            print("You escape safely.")
            return player
        if do_combat(player, chosen["enemy"]):
            if chosen["enemy"] == "BOSS":
                print("\nYOU WIN — THE BOSS IS DEFEATED!")
                player["health"] = 0
            chosen["enemy"] = None
    return player

# main loop

playing = True

while playing:
    player = user_stats()
    game_rooms = roomers()

    while player["health"] > 0:
        rooms()
        choice = input("Room number | a=all | b=stats: ").lower()
        if choice == "a":
            print(game_rooms)
        elif choice == "b":
            print(player)
        elif choice.isdigit():
            visit_room(player, int(choice), game_rooms)

    again = input("Play again? (y/n): ").lower()
    playing = again == "y"
print("Game Over.")