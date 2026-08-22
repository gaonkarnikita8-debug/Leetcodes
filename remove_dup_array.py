class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = []

        for i in nums:
            if i not in k:
                k.append(i)
        counter = len(k)
        return f"{counter}, nums = {k}"

S1 = Solution()
# print(S1.removeDuplicates([0,1,1,2,3,3,3,4]))