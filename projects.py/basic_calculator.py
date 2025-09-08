# BG 1st Basic calucator


def is_n(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
  

while True:
    n1 = input("enter a number")
    if is_n(n1) == False:
       print("Must be a number")
    else:
       break
while True:
    n2 = input("enter a second number")
    if is_n(n2) == False:
       print("must be a number")
    else:
       break

while True:
    n1 = int(n1)
    n2 = int(n2)
    print(n1 {} n2)
