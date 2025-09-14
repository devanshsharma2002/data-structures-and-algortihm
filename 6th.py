#Left Rotate Array by K Places

class Solution:
    def rotateArray(self, nums, k):
        def rotate():
            temp=0
            zero=0
            temp=nums[zero]
            nums.remove(temp)
            nums.append(temp)
        for i in range(k):
            rotate()
        return nums
a=Solution()
print(a.rotateArray( [1, 2, 3, 4, 5, 6],2))