class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        storage={}
        storage2={}
        for x in s:
            storage[x]=storage.get(x,0)+1
        for y in t:
            storage2[y]=storage2.get(y,0)+1
        return storage==storage2

        