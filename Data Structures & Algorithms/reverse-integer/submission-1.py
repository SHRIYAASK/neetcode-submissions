class Solution:
    def reverse(self, x: int) -> int:
        temp=str(x)
        if temp[0]=='-':
            result = temp[0] + temp[1:][::-1]
        else:
            result=temp[::-1]
        final=int(result)
        if final<-2**31 or final>2**31-1:
            return 0
        else:
            return final