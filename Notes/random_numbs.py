# BG 1st random notes

#
#
#  Can computers really generate a "random" number?
# no
#
#
# What is a python library?
# coletions of prebuilt funtions
#
#  
#  What are functions?
#  a cololetions of codes ment to do a specific task
#  
# How do you call a function?
# you call a funtion by calling it by name then use ()
#
# coments
# a well structured code does not need coments
#    
#
#
#
# What have we already learned that is similar to a function?
# methoods are atached to an alrgrithom.


# 
# What function to I call to get a random number?
# .randomint()
#
#  What are arguments?
# something that can 
# 
#
# 
#  What arguments are needed to generate a random number?
#.randomint(1,20)
#

import random

name = input("what is your character name?\n").strip()


# generate stat options
s_one = random.randint(1,10) + random.randint(1,10)
s_2 = random.randint(1,10) + random.randint(1,10)
s_3 = random.randint(1,10) + random.randint(1,10)
s_4 = random.randint(1,10) + random.randint(1,10)
s_5 = random.randint(1,10) + random.randint(1,10)
s_6 = random.randint(1,10) + random.randint(1,10)
s_7 = random.randint(1,10) + random.randint(1,10)

#telling users the stat choices
print(f"your s options are: {s_one}, {s_2}, {s_3}, {s_4}, {s_5}, {s_6}, {s_7}")

#set stats
strenght = int(input("which stat do you want as your stength \n")) +2




print(f"this is a rand number from 0-1: {random.random()}")
print(f" this is a rand numb from 1-20: {random.randint(1,20)}")
