class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        m=-100000000
        prefix,suffix=1,1
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            m=max(m,max(prefix,suffix))
        return m    
