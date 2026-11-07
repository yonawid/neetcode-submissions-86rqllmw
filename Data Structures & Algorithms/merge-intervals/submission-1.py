class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the list out first 
        #compare the end of the previous list and the start of the current list
        intervals=sorted(intervals)
        res=[]
        for start,end in intervals:
            if len(res)==0 or start > res[-1][1]:
                res.append([start,end]) 
            else:
                res[-1][1]=max(end,res[-1][1])
        return res 