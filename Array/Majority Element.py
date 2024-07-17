class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums).most_common()
        return c[0][0]
