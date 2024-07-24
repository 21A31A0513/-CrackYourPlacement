class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums).most_common()
        l=[]
        for i in c:
            if i[1]!=2:
                break
            else:
                l.append(i[0])
        return l
        
