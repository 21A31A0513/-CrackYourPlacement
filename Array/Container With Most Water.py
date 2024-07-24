class Solution:
    def maxArea(self, height: List[int]) -> int:
        s,e=0,len(height)-1
        m=0
        while s<e:
            x=(e-s)*min(height[e],height[s])
            m=max(m,x)
            if height[s]<height[e]:
                s+=1
            else:
                e-=1
        return m
