class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp=Counter(nums)
        sort_items=sorted(temp.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sort_items[i][0])
        return res

