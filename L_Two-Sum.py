'''
space complexity o(n)
time complexity o(n)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {}  # value : index

        for i, n in enumerate(nums):
            if target - n in previous_map:
                return [previous_map[target - n], i]
            previous_map[n] = i
