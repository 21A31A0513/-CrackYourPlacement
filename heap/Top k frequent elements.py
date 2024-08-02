class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums).most_common()
        c=sorted(c,key= lambda x:x[1],reverse=True)
        #print(c)
        l=[]
        for i in range(k):
            l.append(c[i][0])
        return l
