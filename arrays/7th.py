#Move Zeros to End
class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
        return nums
a=Solution()
print(a.moveZeroes([0,0,0,0,0,12,0]))