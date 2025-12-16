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
            item.list("stuff")[:]
