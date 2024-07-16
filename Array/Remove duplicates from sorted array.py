class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        k=len(l)
        nums[:k+1]=l
        return k
