# BG 1st Combat DD Version
import random

class User:
    def __init__(self):
        self.name = input("Enter your name: ")

        self.characters = ["Ranger", "Rogue", "Mage", "Assassin", "Knight"]

        self.health_list  = [70, 55, 50, 45, 120]   
        self.attack_list  = [50, 60, 55, 70, 30]    
        self.defense_list = [25, 20, 20, 15, 40]    
        self.speed_list   = [30, 40, 28, 45, 15]    
        self.potion_list  = [20, 15, 25, 10, 35] 






        for i in range(5):
            print(f"{i}. {self.characters[i]} : Health={self.health_list[i]}, "
                  f"Attack={self.attack_list[i]}, Defense={self.defense_list[i]}, "
                  f"Speed={self.speed_list[i]}, Potion={self.potion_list[i]}")

        while True:
            try:
                self.character_index = int(input("Choose your character (0–4): "))
                if 0 <= self.character_index < 5:
                    break
                else:
                    print("Pick a number between 0–4.")
            except ValueError:
                print("Please enter a number.")

        self.class_name = self.characters[self.character_index]
        self.health = self.health_list[self.character_index]
        self.defense = self.defense_list[self.character_index]
        self.attack = self.attack_list[self.character_index]
        self.potion = self.potion_list[self.character_index]
        self.speed = self.speed_list[self.character_index]

    def display_stats(self):
        print(f"\n{self.name} the {self.class_name}")
        print(f"Health: {self.health}")
        print(f"Defense: {self.defense}")
        print(f"Attack: {self.attack}")
        print(f"Potion: {self.potion}")
        print(f"Speed: {self.speed}\n")

    def do_attack(self):
        return random.randint(1, self.attack)

    def do_defend(self, attack_strength):
        block = random.randint(1, self.defense)
        lost = attack_strength - block
        if lost <= 0:
            print("You blocked the attack!")
        else:
            self.health -= lost
            print(f"You lost {lost} health. Now you have {self.health}.")

    def drink_potion(self):
        gain = random.randint(1, self.potion)
        self.health += gain
        print(f"You healed {gain} HP. Now you have {self.health}.")

    def super_attack(self):
        damage = 2 * random.randint(1, self.attack)
        print(f"You dealt {damage} damage with a super attack!")
        backlash = random.randint(1, max(1, self.attack // 3))
        self.health -= backlash
        print(f"The recoil hurt you for {backlash} HP. You now have {self.health}.")
        return damage

    def flee(self, enemy):
        run = random.randint(1, self.speed)
        if run == self.speed:
            print("You escaped and defeated the monster in your rush! YOU WIN!")
            enemy.health = 0
        elif run > self.speed / 2:
            print("You escaped but got hurt escaping.")
            self.health = 1
        else:
            print("You tripped and the monster got you! You died.")
            self.health = 0


class Monster:
    def __init__(evil):
         evil.names = ["Werewolf", "Colossal Spider", "Giant Rat", "Venom", "Dragon"]
         evil.health_list = [90, 60, 30, 50, 220]
         evil.attack_list = [50, 30, 25, 45, 70]
         evil.defense_list = [20, 15, 10, 18, 30]

         i = random.randint(0, 4)
         evil.villains =  evil.names[i]
         evil.health =  evil.health_list[i]
         evil.attack =  evil.attack_list[i]
         evil.defense =  evil.defense_list[i]

    def display_evil(evil):
        print(f"\nYou are facing a { evil.villains}!")
        print(f"Health: { evil.health}, Attack: { evil.attack}, Defense: { evil.defense}\n")

    def do_attack( evil):
        return random.randint(1,  evil.attack)

    def do_defend( evil, damage):
        block = random.randint(1,  evil.defense)
        lost = damage - block
        if lost <= 0:
            print(f"The { evil.villains} blocked your attack!")
        else:
             evil.health -= lost
             print(f"{ evil.villains} lost {lost} HP. It now has { evil.health} HP.\n")


#  Main Game Loop 
print("Welcome to DD!")

while True:
    player = User()
    player.display_stats()
    enemy = Monster()
    enemy.display_evil()

    player_turn = random.choice([True, False])

    while player.health > 0 and enemy.health > 0:
        if player_turn:
            action = input("Choose: a = attack\n s = super\n h = potion\n f = flee\n Your choice is: ").lower()
            if action == "a":
                enemy.do_defend(player.do_attack())
            elif action == "s":
                enemy.do_defend(player.super_attack())
            elif action == "h":
                player.drink_potion()
            elif action == "f":
                player.flee(enemy)
            else:
                print("Invalid choice.")
                continue
            player_turn = False
        else:
            player.do_defend(enemy.do_attack())
            player_turn = True

        if player.health <= 0:
            print("YOU DIED! Game over.")
        elif enemy.health <= 0:
            print("You defeated the monster! YOU WON!")

    # Play again?
    play_again = input("\nDo you want to start a NEW GAME? (y/n): ").lower()
    if play_again not in ("y", "yes"):
        print(f"Thanks for playing DD with the {enemy.villains}!")
        break
