# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """

#          # counter = nums.count(0)
       
#         for i in nums:
#             if i == 0:
                
            
#         # for j in range(0, counter):
#         #     nums.append(0)
        
#         return nums

# S1 = Solution()
# print(S1.moveZeroes([0,0,1]))


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num = 0

        for i in digits:
            num = num * 10 + i

        num = num + 1
        num = str(num)

        nums = map(int, num)
        print(list(nums)) 

S1 = Solution()
# S1.plusOne([1,2,3])