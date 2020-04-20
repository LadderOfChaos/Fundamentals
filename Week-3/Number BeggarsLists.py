numbers = input().split(", ")
count = int(input())
nums= []

for i in numbers:
    nums.append(int(i))

result = [0] * count

for b in range(len(nums)):
    index = b % count
    result[index] += nums[b]
print(result)