class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if num not in nums:
                self.new_nums.append(num)
        return len(self.new_nums),self.new_nums


s = Solution()
nums = s.removeDuplicates([1,2,2,3,4,4,5,5])
print(nums)