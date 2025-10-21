#BG 1st function notes


p_health = 100
m_health = 100
def damage(amount, turn):
  if turn == "player":
    return m_health - amount, p_health
  else:
     return m_health, p_health - amount

m_health, p_health = damage(10, "player")
print(f"{m_health} montster health")
print(f"{p_health} player health")



#def = definitoins


def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]
    
    return initials

total = add(5,5)
print(total)
print(f" 10 + 72 = {add(10,72)}")
x = 0
while x < add (3,9):
    print("duck")
    x += 1
add(3,9)
print("Goose!")
print(initials("Brett Gerlach"))

print(f"a = {ord("a")} ")
print(f"98 = {chr(98)}")