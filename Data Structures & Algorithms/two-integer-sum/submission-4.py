class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for x, y in enumerate(nums):
            diff = target - y

            if diff in hmap:
                return [hmap[diff], x]

            hmap[y] = x
       