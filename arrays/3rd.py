#Check if the Array is Sorted II
class Solution:
    def isSorted(self, nums):
        #your code goes here
        numcpy=nums.copy()
        print(nums)
        nums.sort()
        print(nums)

        return (nums==numcpy)
    
nums=[1,2,1,4,5]
a=Solution()
print(a.isSorted(nums))