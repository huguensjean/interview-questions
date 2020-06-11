def twoSum(nums, target):
        group_adjacent = lambda a, k: zip(*([iter(a)] * k))
        adj_list = group_adjacent(nums, 2)
        index = 0
        for i in adj_list:
            if sum(i) == target:
                break
            index += len(i)
        return [index, index+1]

print("\nFind the indices of the first two numbers that add to a target sum.")
l = [1,2,3,4,5,6,7,8,9]
print("\nInput list:")
print(l)
print("\nTarget: ", 11)
indx = twoSum(l, 11)
print("\nInput list indices:", indx)
print("\nInput list numnbers %d and %d add to %d"% (l[indx[0]], l[indx[1]], l[indx[0]]+l[indx[1]]))
