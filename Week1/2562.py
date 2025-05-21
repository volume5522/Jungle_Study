nums = [int(input()) for _ in range(9)]

max_val = max(nums)
position = nums.index(max_val) + 1

print(max_val)
print(position)
