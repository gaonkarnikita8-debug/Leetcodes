class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
#Input: nums = [1,2,3,1]

# Output: true
# [1,2,3,4] = false
# Explanation:
# The element 1 occurs at the indices 0 and 3.

        counter = 0

        for num in nums:
            if nums.count(num) > 1:
                counter += 1
            else:
                counter += 0

        if counter >= 1:
            return True
        else:
            return False

S1 = Solution()
# print(S1.containsDuplicate([1,2,3,4,5]))