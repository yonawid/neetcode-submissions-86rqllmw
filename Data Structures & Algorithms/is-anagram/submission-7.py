class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        storage={}
        storage2={}
        for char in s:
            storage[char]=storage.get(char,0)+1
        for char in t:
            storage2[char]=storage2.get(char,0)+1
        return storage==storage2
        