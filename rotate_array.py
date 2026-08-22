class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        new_list = []
        len_nums = len(nums)
        for i in nums:
            if k == 0:
                break
            else:
                new_list.append(nums[len_nums - 1])
                nums.pop()
                len_nums -= 1
                k -= 1
        new_list.extend(nums)
        print(new_list)

S1 = Solution()
# S1.rotate([-1,-100,3,99], k=2)
