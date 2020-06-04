# put your python code here
x = int(input())
nums = [x ** 2]
while x != 0:
    y = int(input())
    x += y
    nums.append(y ** 2)

print(sum(nums))
