class Solution:
    def isValid(self, s: str) -> bool:
        operdict={'{':'}','[':']','(':')'}
        stack=deque()
        top=-1
        for i in s:
            if top==-1:
                stack.append(i)
                top=top+1
            else:
                if stack[top] in operdict:
                    if i==operdict[stack[top]]:
                        stack.pop()
                        top=top-1
                    else:
                        stack.append(i)
                        top=top+1
                else:
                    stack.append(i)
                    top=top+1
        if top==-1:
            return(True)
        else:
            return(False)

        