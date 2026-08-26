class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0

        for num in nums:
            if nums.count(num) == 1:
                return num
            else:
                counter += 1

S1 = Solution()
# print(S1.singleNumber([2,3,2,3,1]))