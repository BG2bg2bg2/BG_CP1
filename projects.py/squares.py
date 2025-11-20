#BG 1st squares

#list of numbers
numbers = [1 , 2, 3, 4,
           5 , 6, 7, 8,
           9 ,10,11,12,
           13,14,15,16,
           17,18,19,20,
           21,22,23,24,
           25,26,27,28,
           29,30,31,32,
           33,34,35,36,
           37,38,39,40]
#map and lambda work to gether to give the output of numbers
                #pair puts the original numbers next to the squared numbers from list of numbers
#pair = map(lambda num: (f"original: {num}", f"squared: {num**2}"), numbers)

#both returns what is in pair to be availible to make the list and gives a dictionary
#both = dict(pair)

for p in map(lambda num: (f"original: {num}", f"squared: {num**2}"), numbers):
    #display what the previous code made
    print(p)
