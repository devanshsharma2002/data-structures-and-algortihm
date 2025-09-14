#Left Rotate Array by One

class Solution:
    def rotateArrayByOne(self, nums):
        temp=0
        zero=0
        temp=nums[zero]
        nums.remove(temp)
        nums.append(temp)
        
        return nums


a=Solution()
print(a.rotateArrayByOne([-1, 0, 3, 6]))