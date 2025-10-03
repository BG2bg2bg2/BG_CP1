#BG 1st While loop notes

for num in range(1,21):
    print(num)

num = 1
while num <=20:
    print(num)
    num+=1

import random
goose = random.randint(1,20)
count = 0
while count != goose:
    count += 1
    print("duck")
    """if count == goose:
        break
    else:"""
    if count == 13:
        break
else:
    print("GOOSE")
print("code is done")


i = 0
while i <= 20:
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the code")
        i+= 1
print("the loop ended")