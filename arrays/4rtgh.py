#Remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp=0
        newlist=[]
        while nums:
            temp=nums[0]
            print (temp)
            newlist.append(temp)

            while temp in nums:
                nums.remove(temp)
            print (len(newlist),newlist)

        return (len(newlist),newlist)

a=Solution()
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
