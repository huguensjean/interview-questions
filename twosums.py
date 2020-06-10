def twoSum(nums, target):
        group_adjacent = lambda a, k: zip(*([iter(a)] * k))
        adj_list = group_adjacent(nums, 2)
        index = 0
        for i in adj_list:
            if sum(i) == target:
                break
            index += len(i)
        return [index, index+1]

l = [1,2,3,4,5,6,7,8,9]
print(twoSum(l, 11))
