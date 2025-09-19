#BG 1st conditonals notes

import random

player_hp = 20
player_attack = 5
player_defense = 5
player_damage = 5

monster_hp = 15
monster_attack = 3
monster_damage = 10
monster_defence = 2

hit_roll = random.randint(1,20) + player_attack
damage_roll = random.randint(1,8) + player_damage

if hit_roll == 20:
    print("You got a crit! that means you get ro roll for damage twice!")
    damage_roll = random.randint(1,8)+ random.randint(1,8) + player_damage
    print(f"you did {damage_roll-monster_defence} damage!")
    monster_hp -= (damage_roll-monster_defence)
elif hit_roll == 1:
    print("you rolled a critical failure! Now the monster gets to attack you!")
    damage_roll = random.randint(1,12) + monster_damage
    player_hp -= (damage_roll - player_defense)
    print(f"the monster rolled {damage_roll}")
elif hit_roll + player_attack >= 12:
    print("You hit! Roll for damage.")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defence:
        print(f"you did{damage_roll-monster_defence} .")
        monster_hp -= (damage_roll-monster_defence)
    else:
        print("you did no damage.")

else:
    print("You missed.")

if True > 0
    attack_roll = random.randint(1,20) + monster_attack
    if hit_roll