class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):#check the length first because if the length arenot equal it cant be anagram
            return False

        storage1={}#dictionary for storing
        storage2={}
        for char in s:
            storage1[char]=storage1.get(char,0)+1#gets the current count and adds 0 if nothing is there yet and then adds 1
        for char in t:
            storage2[char]=storage2.get(char,0)+1
        return storage1==storage2#compare both dictionaries if they are the same return true.
            