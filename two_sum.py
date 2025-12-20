class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i ,num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return[seen[complement],i]
            seen[num]=i

obj=Solution()
nums=[3,2,4]
target=6
result=obj.twoSum(nums,target)
print(result)

        
