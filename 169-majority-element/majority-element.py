class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)/2
        s = set(nums)

        for i in s:
            if nums.count(i) > l:
                return i