#BG 1st Flexible Calculator

import statistics

def operate(*args, **kwargs):
    #kwargs are used to send the operation the user selected to the cp
    operation = kwargs.get("operation", "sum")  #default operation is sum

    #args are used to send multiple numbers to the function
    if operation == "sum":
        return sum(args)

    elif operation == "average":
        return statistics.mean(args)

    elif operation == "max":
        return max(args)

    elif operation == "min":
        return min(args)

    elif operation == "product":
        product = 1
        for n in args:
            product *= n
        return product


def collect_numbers():
    nums = []
    while True:
        #Ask the user for numbers until they type "done"
        entry = input("Enter a number or type 'done': ")
        if entry.lower() == "done":
            break
        try:
            #Convert inputs to floats
            nums.append(float(entry))
        except:
            print("Invalid number. Try again.")
    return nums


#MAIN LOOP
while True:

    #Show available operations
    print("\nAvailable operations: sum, average, max, min, product")

    #Ask the user what operation they want to perform
    op_choice = input("Enter the operation you want: ").lower()

    #If choice invalid → restart
    if op_choice not in ["sum", "average", "max", "min", "product"]:
        print("Invalid operation. Try again.")
        continue

    print("\nEnter numbers. Type 'done' when finished.")

    #collecting numbers and converting
    numbers = collect_numbers()

    if len(numbers) == 0:
        print("No numbers entered. Restarting...")
        continue

    #Compute result and print it
    result = operate(*numbers, operation=op_choice)

    print("\n--- RESULT ---")
    print(f"Operation: {op_choice}")
    print(f"Numbers: {numbers}")
    print(f"Result: {result}")
    print("--------------")

    #Ask the user if they want to restart or quit
    again = input("Type 'restart' to do another calculation or anything else to quit: ")
    if again.lower() != "restart":
        break
