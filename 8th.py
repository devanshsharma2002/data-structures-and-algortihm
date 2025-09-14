#Linear Search
class Solution:
    def linearSearch(self, nums, target):
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
            
        else:
            return -1
            
a=Solution()
print(a.linearSearch( [1, 2, 3, 4, 5, 6],2))