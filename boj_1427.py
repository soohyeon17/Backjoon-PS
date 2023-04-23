n = input()
nums = []
for i in n:
 nums.append(int(i))
nums.sort(reverse = True)
print(''.join(str(i) for i in nums))