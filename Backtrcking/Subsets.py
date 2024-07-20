class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(i,l,res):
            if i>=len(nums):
                res.append(l[:])
                return
            l.append(nums[i])
            rec(i+1,l,res)
            l.pop()
            rec(i+1,l,res)
        res=[]
        rec(0,[],res)
        print(res)
        return res

