#BG 1st pseudocode notes

loop = 12
string = (loop * 1**12)

colum = 0
row = 0
while True:
    colum = colum * 2
    row = row * 2
    fullcode = (colum * row + string)
    print(fullcode)
    colum = colum + 1
    row = row + 1