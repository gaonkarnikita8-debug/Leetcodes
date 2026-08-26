class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        outlist = []
        result = []

        for i in nums1:
            for j in nums2:
                if i == j:
                    outlist.append(i)
                
        for k in outlist:
            if k not in result:
                result.append(k)

        return result

S1 = Solution()
# print(S1.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))