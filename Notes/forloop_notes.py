#BG 1st for loop notes

nums = [3,332,324,324,345,321,43,12,4,3,4,324,23432]

for num in nums:
    print(num)
    num/= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number")

    else:
        print(num)
print("End code")

for num in range(1,10):
    print(num)

for (nums) in range(1, 10):
    print(nums)
for (nums) in range(20,0,-2):
    print(f"\n {nums}") 
    time.sleep(4)
#this counts by 2s in revers