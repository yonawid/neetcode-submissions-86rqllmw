class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):#check the length of both if they are not equal :it cant be anagran
            return False
        storage={} #a place to store the characters so we can compare them later on
        storage2={}#a place to store the characters so we can compare them later on
        for char in s:# loops through each character
            storage[char]=storage.get(char,0)+1#gets the character and adds +1 to it
        for char in t:
            storage2[char]=storage2.get(char,0)+1
        return storage==storage2#compare the hashmaps