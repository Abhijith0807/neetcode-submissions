class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        frow,lrow=0,rows-1
        while frow<=lrow:
            midrow=(frow+lrow)//2
            if target>matrix[midrow][cols-1]:
                frow=midrow+1
            elif target<matrix[midrow][0]:
                lrow=midrow-1
            else:
                break
        midrow=(frow+lrow)//2
        lptr=0
        rptr=cols-1
        while lptr<=rptr:
            mid=(lptr+rptr)//2
            if target==matrix[midrow][mid]:
                return(True)
            elif target>matrix[midrow][mid]:
                lptr=mid+1
            else:
                rptr=mid-1
        return(False)
        