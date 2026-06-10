class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for j in range(0, len(nums)):
            temp=1
            for i in range(0,len(nums)):
                if i!=j:
                    temp*=nums[i]
            res.append(temp)
        return res
        
        





