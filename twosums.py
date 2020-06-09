def twoSum(self, nums: List[int], target: int) -> List[int]:
        group_adjacent = lambda a, k: zip(*([iter(a)] * k))
        adj_list = group_adjacent(nums, 2)
        index = 0
        for i in adj_list:
            if sum(i) == target:
                break
            index += len(i)
        return [index, index+1]
