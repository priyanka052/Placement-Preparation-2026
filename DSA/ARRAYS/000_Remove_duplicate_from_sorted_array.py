# LeetCode 2: Remove Duplicate from Sorted Array Sum
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea:
# Use two pointers to overwrite duplicates in-place while maintaining relative order.
# SOLUTION

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l