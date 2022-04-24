class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) == 1:
                return i
