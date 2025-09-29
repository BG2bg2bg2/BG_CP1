# BG 1st list notes
import random
not_sibs = ["mom", "dad", "Ammon", "Fred", "Nielsen", "Russle", "Gabrel", "Alma", "Nephi", 5.76, False]


print(not_sibs[5])
print(random.choice(not_sibs, weights=[10, 10, 10, 10, 10,10], k=5))
print(f"the list is, {len(not_sibs)} people long")
print(not_sibs)
#replacing is this
not_sibs[0] = "Eric"
#not this
#not_sibsreplace("Fred", "Parker") this only works for strings

not_sibs[6:-1] = ["lavender", "Green"]
not_sibs.pop()
not_sibs.pop(6)
not_sibs.remove("dad")

#not_sibs clear()
#not_sibs.append("Fred") adds to the end of the list
not_sibs.insert(2, "Anderwel")
#adds things the the end of the list
not_sibs.extend(["Joseph", "Isreal", "USA"])
print(not_sibs)

board = [[ 1,2,3]
         [4,5,6],
         [7,8,9]
        ]

