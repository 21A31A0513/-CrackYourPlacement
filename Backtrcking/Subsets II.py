class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def rec(i,l,res):
            if i>=len(nums):
                if l[:] not in res:
                    res.append(l[:])
                return
            l.append(nums[i])
            rec(i+1,l,res)
            l.pop()
            rec(i+1,l,res)
            return res
        res=[]
        return rec(0,[],res)
