class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,T in enumerate(temperatures):
            while stack and T>stack[-1][1]:
                indx,temp=stack.pop()
                res[indx]=i-indx
            stack.append((i,T))
        return(res)