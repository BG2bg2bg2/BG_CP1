#BG 1st psudocode to code

import random as r
#Data
#List of rooms available to visit
#Rooms are described by a dictionary of 9 rooms with the following values
room = [
    "Earth",
    "LA",
    "Ua",
    "Quip",
    "LASS",
    "IPLA",
    "BLAT",
    "Uit",
    "HIPOS"]

def rooms():
    for r, room_names in enumerate(room, start-1):
        print(f"{r}: {room_names}")
   
#	Description is text displayed to user
#	Elements are the artifacts in the room like weapons and shields
#	Enemies must be fought or run from but if user survives players stats upgrades randomly

def roomers():
    return[
        {"room": "Earth", "stuff": ["note", "gun"], "enemy": None},
    ]

#Elements are a dictionary with the following values which, which change user stats

def user_stats():
    user_name = input("enter a name for your character")
#Name,
    user = {
    "name": user_name,
    #health
    "health": 90,
    #speed
    "Speed":2,
    #defence
    "defence":5,
    #stength
    "stength":10
    }
    return user

#Only one element can be used per battle.
while True:
    enter = input("A")
    if enter == "A" or enter == "a":
        for a in rooms():
            print(rooms)
    else:
        continue

#Player and enemies are described by a dictionary named players.
#Set user’s attributes
#health = 30
#Stealth = 0
#Speed = 2,
#Defence = 3
#Strength = 7

#Boss attributes

#	Health 70
#	Stealth = 3
#	Speed = 3
#	Defence = 2
#	Strength = 30

#Enemy 3 = GLARB
#	Health = 100
#	Stealth = 100
#	Speed = 300
#	Defence = 200
#	Strength = 34543
#Avoid GLARB!!!!!!!!

#Functions:
#visit_room(room_number)#
#	Display room description 
#	If enemy in room do combat
#	If item in room do item

#do_combat
    #Function player_attack_roll()
#    Roll random number between 1 and player strength plus speed
#    Function player_defend(enemy_damage)
#    Block = random number between 1 and and player defense minus stealth minus speed plus enemy speed#
#
 #   If player or enemy is at 0 end combat with out come of returning health or ending game	
  #  Use_item
   #     Describe item
    #    Ask user to use, discard, or leave item.
     #   If use then add item attributes to users attributes, remove item from room, place item in users hands.
      #  Else If discard, subtract item attribute from user attributes and remove item from room and from users hands
       # Else if leave item  do nothing.

#    Main loop
 #   While user lives
  #  Display rooms
   # If user enters room 1
    #    display you enter a hidden place on Earth and you see a note and a gun you go to the gun first and are asked if you want to pick it up then you go to read the note
    #    If user enters room 2
     #       display you enter a hidden ship called LA (Lost Aliens) and you see a jet pack and a note
      #      Ask user to pick up body o pack then read note
       # If user enters room 3
        #    display you enter a patrol ship called UA (Unified Aliens) and you run into an enemy scout
         #   Display enemy stats and ask if you want to run or fight
          #      Do combat if chose to fight
    #If user enters room 4
     #           display you enter your outside on this little island with some people you know and some others that you don't recognise but you talk to each one anyways and you get intel of what the place is called (Quip Quick update intel place) and you get intel of what the bosses sats are
     #   Display boss stats
      #  Display write them down on a piece of paper
   # If user enters room 5
    #Display your in a Lost Alien Space Ship and you see an enemy named GLARB
    #Display enemy 3 stats
    #Display run!!!!
    #Display you died by not running too fast
    #isplay avoid GLARB at all costs
   # Display GLARB Great Lost Alien Rebellion to Boss
    #    If user enters room 6
     #       Display you enter IPLA Intel Place for Lost Aliens
      #      Display you see an enemy
       #     Display enemy stats
        #        Do combat
        #If user enters room 7
         #   Display you enter a place called BLAT and you see a book
          #  Display you read the book
           # Display all enemy stats
           # Display all rooms with enemies
            #Display rooms to avoid with no loot
            #Display you leave room never to return
  #      If user enters room 8
   #         You enter Uit a place for Unified Intel Trade
    #            You see a chest with a ball
     #           Display Ball o shield stats
      #          Ask to pick up it and use it or discard it
       # If user enters room 9
        #    Display you found a key somewhere in the hall and you unlock the door to the room
         #   Display you see a man on a chair in some random part of the galaxy
          #  Display You enter my domain isn't my work done well
           # Display your work is nothing but theory and kidnapping I know why you do it and it is not good
            #Display I challenge you weather I know or not on how much life you have
             #   Do combat
 #   Choose a number for going into a room with that same number to go into
  #  Call visit room(room number)
   # If user dead break
    