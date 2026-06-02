class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage=set()
        for n in nums:
            if n in storage:
                return True
            storage.add(n)
        return False