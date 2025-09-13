#Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

class Solution:
    def secondLargestElement(self, nums):

        maxi=max(nums)
        mini=min(nums)
        if mini==maxi:
            return -1
        else:    
            while maxi in nums:
                nums.remove(maxi)
        return max(nums)
    
nums=[7,7,7]
a=Solution()
print(a.secondLargestElement(nums))