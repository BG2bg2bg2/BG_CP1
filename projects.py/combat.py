#BG 1st combat DD vircion

import random



class user:
    def __init__ (self):
        self.name = input("enter your name: ")
        characters = ["Ranger", "Rogue", "Mage", "Assasine", "Knight"]

        health = [20,20,20,10,100]
        attack = [55,20,50,20,70]
        defense = [20,20,40,20,50]
        speed = [30,33,34,40,10]
        potion = [10, 10, 10, 5, 50]

        for a in range(0,5):
            print(f" {a} {characters [a]} health = {health[a]}, attack = {attack[a]} defense = {defense[a]} speed = {speed[a]}, potion = {potion[a]}")

        self.character_index = int(input("Choose the number for the corosponding characters. (0-4): "))

        self.class_name = characters[self.character_index]
        self.health = health[self.character_index]
        self.defense = defense[self.character_index]
        self.attack = attack[self.character_index]
        self.potion = potion[self.character_index]
        self.speed = speed[self.character_index]

    
    def display_stats(self):
        print(self.name)
        print(f"{self.class_name}")
        print(f"health = {self.health}")
        print(f"defense = {self.defense}")
        print(f"attack = {self.attack}")
        print(f"potion strength = {self.potion}")
        print(f"speed = {self.speed}\n")

    def do_attack(self):
        attack_strength = (random.randint(1, self.attack))
        return attack_strength
    
    def do_defend(self, attack_strength):
        defense_block = random.randint(1, self.defense)
        lost = attack_strength - defense_block
        if lost < 0:
            print("you blocked the attack!")
        else:
            self.health -= lost
            print(f"you lost {lost}. Now you have {self.health} health.")

    def drink_potion(self):
        health_gain = random.randint(1, self.potion)
        self.health += health_gain
        print(f"you gained {health_gain}. Now you have {self.health}")

    def super_attack(self):
        attack_strength = 2*random.randint(1, self.attack)
        print(f"you did {attack_strength} damage by using your weight")
        lose_life = attack_strength / random.randint(1, self.health)
        a = round(lose_life)
        self.health -= a
        print(f"fun you lost {a} health now you have {self.health}")

    def flee(self):
        run = random.randint(1, self.speed)
        if run == self.speed:
            print("you ran with spikes on your heels and slowly killing the monster at your feet")
            print("YOU SUCCESSFULY WON THE GAME!")
            print("GAME OVER YOU WON")

        elif run > self.speed/2:
            print("You were climbing a mountain and making a land slide killing the monster but cutting yourself on jaged edges")
            print("YOU beat that monster but now you face a new monster on the mountain")
            print("want to continue your quest or jump off?")
            print("Depends on how you look at it!!!")
        else:
            print("You died by falling in a pit that was behind a log that you, yourself has setted up")
            print("You DIE GOOD LUCK NEXT TIME (if there is a next time)")
class Monster:
    def __init__ (evil):
        evil.monster_index = random.randint(0,4)
        evil.villain_list = ["Werewolf", "Colosial Spider", "Rodent of Unusual Size", "'Venom'", "Dragon"]
        evil.health_list = [40, 40, 20, 40, 200]
        evil.attack_list = [110, 40, 100, 40, 140]
        evil.defense_list = [10,10,20,10,25]
        
        evil.villains = evil.villain_list[evil.monster_index]
        evil.health = evil.health_list[evil.monster_index]
        evil.attack = evil.attack_list[evil.monster_index]
        evil.defense = evil.defense_list[evil.monster_index]
    def display_evil(evil):
        print(evil.villains)
        print(f"health = {evil.health}")
        print(f"attack = {evil.attack}")
        print(f"defense = {evil.defense}\n")

    def do_attack(evil):
        attack_strength = (random.randint(1, evil.attack))
        return attack_strength
    
    def do_defend(evil, attack_strength):
        defense_block = random.randint(1, evil.defense)
        lost = attack_strength - defense_block
        if lost < 0:
            print("{evil.villain} blocked the attack!\n")
        else:
            evil.health -= lost
            print(f"Monster lost {lost}. Now it has {evil.health} health.\n")

player = user()
player.display_stats()
player.flee()

enemy = Monster()
enemy.display_evil()

print(enemy.do_attack())
print(player.do_attack())
enemy.do_defend(player.do_attack())



pds = [player.do_attack(), player.drink_potion(), player.flee()]

print(pds)
for a in pds:
    choose = int(input(f"enter a number to do {pds}"))
    if choose == 0:
        a = player.do_attack()
    
    elif choose == 1:
        a = pds(2)
    elif choose == 3:
        a = pds(3)
print(a)