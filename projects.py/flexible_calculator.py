#BG 1st flexible calculator

#bring in a library
import statistics

num = []

#funtion to do keep the numbers
def op(*oper, **opor):
    print(opor)
    for o in oper:
        print(f"number: {o} {opor['oporation']}")
print(f"avalible operations: ",(op ()))
#while the code is true do the folowing
while True:
    #ask the user to enter what they want to do
    print("Availible operations: sum, average, max, min, product")
    type_of_math = input("enter what you want to do: ")
    #if the user input is not true 
        #restart
    #while the code is not done
    #ask the user to enter the numbers until user enters done
    #"""display result"""
    #ask the user to restart or quit

    def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum += f"{story['name']} is the main character of the story. "
    if "place" in story.keys():
        sum += f"The story takes place in {story['place']}. "
    if "confict" in story.keys():
        sum += f"The problem is {story['confict']}."
    return sum

print(summary(name="luke skywalker", place="galaxy far far away", confict="rescue the princess"))
print(summary(name="Harry potter", confict="Kill the dark lord"))
