#BG 1st ideot proofing
def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

while True:
  fname = input("enter your first name ")
  if len(fname) > 15:
     print("your name can't be over 15 letters")
  elif not fname.find(" ") == -1:
    print("no spaces allowed for first name")
  elif not fname.isalpha():
      print("You must enter a name and it cant have numbers")
  else:
    break

while True:
  lname = input("enter your last name ")
  if len(lname) > 20:
     print("last name is too long")
  elif not lname.find(" ") == -1:
     print("must not have spaces")
  elif not lname.isalpha():
     print("last name must not have have numbers ")
  else:
    break

while True:
     gpa = input("what is your gpa? ")
     if is_number(gpa) == False:
        print("Gpa must be a number")
     elif float(gpa) > 4.0:
        print("Must be 4.0 or smaller")
     elif float(gpa) < 0:
        print("needs to be bigger than 0")
     else:
      break

while True:
      pnumb1 = input("What is the first 3 numbers of your phone number? ")
      if is_number(pnumb1) == False or len(pnumb1) != 3:
        print("enter exactly 3 digits")
      else:
        break

while True:
      pnumb2 = input("What is the next 3 numbers of your phone number? ")
      if is_number(pnumb2) == False or len(pnumb2) != 3:
        print("enter a number with exactly 3 digits")
      else:
        break
while True:
      pnumb3 = input("What is the last 4 numbers of your phone number? ")
      if is_number(pnumb3) == False or len(pnumb3) != 4:
        print(f"Please enter a number with exactly four digits.")
      else:
        break

fn = fname.capitalize()
ln = lname.capitalize()
print(f"\n \nname: {fn} {ln}")
gr = float(gpa)
p = (f"{pnumb1} {pnumb2} {pnumb3}")
print(f"phone number {p} \ngrade: {gr:.1f}")
