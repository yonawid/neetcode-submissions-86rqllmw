class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #convert the list into hashmap
        store=Counter(nums)
        heap=[]
        for num,freq in store.items():
            heap.append((-freq,num))

        heapq.heapify(heap)

        counter=[]
        for _ in range(k):
            val=heapq.heappop(heap)
            counter.append(val[1])
        return counter


        