#BG 1st formatting output notes
#How do I write the format method?
Name = "Jake"
Age = 999
money = 25765765765.23
percent = .43
print("Hello {}, your are {:E}. That is so old! You have ${:.2f} you are broke Random personent {:%}".format(Name, Age,money, percent))


#What does the format method allow me to change about my outputs?
#alows you to change to general formats so that way its able to be readable to the reader


#Describe why it is important to format your outputs
#to be readable to the reader



#What is an f-string?
#something that has the f = format to the code


#How do I create an f-string?
# print(f" {Name}"")

#What do f-strings allow me to do?
#change code and be more simple for readers to have/do.


print("Hello {}, your are {:E}. That is so old! You have ${:.2f} you are broke Random personent {:%}".format(Name, Age,money, percent))

print(f"\n\nHello {Name}, you are {Age:,}, That is so old. you have ${money:2f} you are broke {percent:.2f}%. ")