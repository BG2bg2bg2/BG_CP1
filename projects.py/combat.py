#BG 1st combat DD virstion

import time
import random

list_of_charactures = []
charactures = ['roge', 'ranger', 'knight', 'mage']
stragth = [10, 60, 90, 100]
realowed_time = [1, 5, 3, 10]
health = [40, 30, 100, 40]

for i in range(len(list_of_charactures)):
    user = {"charactur": charactures[i], 'strangth': stragth[i], "slow time": realowed_time[i], "life": health[i]}
keys = ['characture', 'strangth', 'slow time', 'life']
values = [
    ['roge', 10, 1, 40],
    ['ranger', 60, 5, 30]
    ['knight', 90, 3, 100]
    ['mage', 100, 10, 40]
]

i = input('enter a number')
for i in range(len(list_of_charactures)):
    user_choice = user

print(user)