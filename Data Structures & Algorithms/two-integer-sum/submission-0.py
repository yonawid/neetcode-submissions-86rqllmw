class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage={}
        for key,value in enumerate(nums):
            diff=target-value
            if diff in storage:
                return[storage[diff],key]
            storage[value]=key
        return