# User stats
def user_stats():
    user_name = input("Enter a name for your character: ")
    return {
        "name": user_name,
        "health": 90,
        "speed": 2,
        "defence": 5,
        "strength": 10,
        "items": [],
        "intel": []
    }

# Item boosts
item_effects = {
    "note": {"commet": "You have accses to all of the rooms"},
    "note": {"commet": "You have accses to know the health of the BOSS"},
    "gun": {"strength": r.randint(3, 9)},
    "jetpack": {"speed": r.randint(5, 9)},
    "book": {"strength": r.randint(4, 9), "defence": r.randint(5, 10)},
    "ball_o_shield": {"defence": r.randint(4, 9)}
}

# Boost stats from items
def boost_stats(player, item):
    if item in item_effects is "note":
        player['intel'] = item_effects["note"]