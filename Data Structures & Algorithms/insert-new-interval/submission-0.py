class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        for current in intervals:
            if current[1]< newInterval[0]:
                ans.append(current)
            elif current[0]>newInterval[1]:
                ans.append(newInterval)
                newInterval=current
            else:
                newInterval=[min(current[0],newInterval[0]),max(current[1],newInterval[1])]
        ans.append(newInterval)
        return ans
