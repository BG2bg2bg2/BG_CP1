#BG 1st mapping notes
numbers = [234,324324,324,243242,32,324,324]
#new = []
"""for num in numbers:
    new.append(num/3)
print(new)"""

def div(num):
    return num/8


new = map(lambda num: num/8, numbers)
print(new)
for num in new:
    print(num)


#What information does map need?
#function, list, tuple

#What does map return?
#a location called a point.

#What is a lambda function
#can take in multiple items and returns only one thing but happends only once

#How does using a lambda function and the map function shorten your code?
#makes it a one line function