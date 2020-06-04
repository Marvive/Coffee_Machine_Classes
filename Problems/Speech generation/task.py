# nums = input()
# # print(nums)
# nums = list(map(int, nums))
# # print(nums)
#
# for num in nums:
#     if num == 0:
#         new_val = "zero"
#     if num == 1:
#         new_val = "one"
#     if num == 2:
#         new_val = "two"
#     if num == 3:
#         new_val = "three"
#     if num == 4:
#         new_val = "four"
#     if num == 5:
#         new_val = "five"
#     if num == 6:
#         new_val = "six"
#     if num == 7:
#         new_val = "seven"
#     if num == 8:
#         new_val = "eight"
#     if num == 9:
#         new_val = "nine"
#     print(new_val)

digits = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']

num = input()

for nums in num:
    print(digits[int(nums)])
