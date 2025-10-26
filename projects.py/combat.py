#BG 1st combat DD virstion

import random



class user:
    def __init__ (self, class_name):
        self.class_name = class_name
        self.health = 30
        self.defense = 3
        self.attack = 20
        self.potion = 12
        self.speed = 10
    
    def display_stats(self):
        print(f"{self.class_name}")
        print(f"health = {self.health}")
        print(f"defense = {self.defense}")
        print(f"attack = {self.attack}")

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
        print(f"you gained {health_gain} now you have {self.health}")

    def super_attack(self):
        attack_strength = 2*random.randint(1, self.attack)
        print(f"you did {attack_strength} damage by using your weight")
        lose_life = attack_strength / random.randint(1, self.health)
        a = round(lose_life)
        self.health -= a
        print(f"fun you lost {a} health now you have {self.health}")

    def flee(self):
        run = random.randint(1, self.speed)
        if run == self.speed():
            print("you ran with spikes on your heels and slowly killing the monster at your feet")
            print("YOU SUCCESSFULY WON THE GAME!")
            print("GAME OVER YOU WON")

        elif run <= 2/self.speed():
            print("You were climbing a mountain and making a land slide killing the monster but cutting yourself on jaged edges")
            print("YOU beat that monster but now you face a new monster on the mountain")
            print("want to continue your quest or jump off?")
            print("Depends on how you look at it!!!")
        else:
            print("You died by falling in a pit that was behind a log that you, yourself has setted up")
            print("You DIE GOOD LUCK NEXT TIME (if there is a next time)")

player = user("Knight")
player.display_stats()
pa = player.do_attack()
print(f"your attack was {pa}")
player.do_defend(14)
player.drink_potion()
player.super_attack()
