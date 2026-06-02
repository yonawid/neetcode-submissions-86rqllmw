class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map=set() # creates a set to store the numbers
        for n in nums:#loops through all the numbers inside the list
            if n in map: #checks the values inside the map
                return True#returns True if there is duplicate
            map.add(n) #adds value to the map
        return False #no duplicates were found