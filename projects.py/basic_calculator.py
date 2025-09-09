# BG 1st Basic calucator


def is_n(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
  
  
while True:
  a1 = input("enter an operator [+ , -, *, /, **, //, %, 'a' for all or (blank) to exit] ")
  if a1 == "":
    print("Exiting calc")
    break

  while True:
      n1 = input("enter a number ")
      if is_n(n1) == False:
        print("Must be a number")
      else:
        n1 = float(n1)
        break
  while True:
      n2 = input("enter a second number ")
      if is_n(n2) == False:
        print("must be a number")
      else:
        n2 = float(n2)
        break
  if a1 == "+" or a1 == "a":
    print(f"\n{n1:.2f} + {n2:.2f} = {n1 + n2:.2f}")
  if a1 == "-" or a1 == "a":
    print(f"\n{n1:.2f} - {n2:.2f} = {n1 - n2:.2f}")
  if a1 == "/" or a1 == "a":
    print(f"\n{n1:.2f} / {n2:.2f} = {n1 / n2:.2f}")
  if a1 == "*" or a1 == "a":
    print(f"\n{n1:.2f} * {n2:.2f} = {n1 * n2:.2f}")
  if a1 == "%" or a1 == "a":
    print(f"\n{n1:.2f} % {n2:.2f} = {n1 % n2:.2f}")
  if a1 == "//" or a1 == "a":
    print(f"\n{n1:.2f} // {n2:.2f} = {n1 // n2:.2f}")
  if a1 == "**" or a1 == "a":
    try:
      print(f"\n{n1:.2f} ** {n2:.2f} = {n1 ** n2:.2f}")
    except:
      print("\nvalue too large for exponent")


    
