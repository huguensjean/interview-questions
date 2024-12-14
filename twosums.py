def twoSum(nums, target):
    # Iterate over the list in steps of 2, checking each consecutive pair.
    for i in range(0, len(nums) - 1):
        if nums[i] + nums[i+1] == target:
            return [i, i+1]
    return None  # If no pair found that sums to target

print("\nFind the indices of the first two consecutive numbers that add to a target sum.")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nInput list:")
print(l)
print("\nTarget:", 11)
indices = twoSum(l, 11)

if indices is not None:
    print("\nIndices:", indices)
    print("\nNumbers at those indices:", l[indices[0]], "and", l[indices[1]],
          "add up to", l[indices[0]] + l[indices[1]])
else:
    print("\nNo two consecutive numbers add up to the target.")
