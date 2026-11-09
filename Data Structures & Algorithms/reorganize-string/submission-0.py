class Solution:
    def reorganizeString(self, s: str) -> str:
        store=Counter(s)
        heap=[]
        for char,freq in store.items():
            heap.append((-freq,char))
        heapq.heapify(heap)
        res=[]
        prev=None

        while heap:
            freq,char=heapq.heappop(heap)
            res.append(char)
            freq+=1
            if prev:
                heapq.heappush(heap,prev)        
                prev=None
            if freq<0:
                prev=(freq,char)

        if prev:
            return ""

        return "".join(res)