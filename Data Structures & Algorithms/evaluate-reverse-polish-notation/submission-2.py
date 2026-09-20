class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalstack=deque()
        for n in tokens:
            if n=='+':
                el2=evalstack.pop()
                el1=evalstack.pop()
                elop=int(el1)+int(el2)
                evalstack.append(elop)
            elif n=='-':
                el2=evalstack.pop()
                el1=evalstack.pop()
                elop=int(el1)-int(el2)
                evalstack.append(elop)
            elif n=='*':
                el2=evalstack.pop()
                el1=evalstack.pop()
                elop=int(el1)*int(el2)
                evalstack.append(elop)
            elif n=='/':
                el2=evalstack.pop()
                el1=evalstack.pop()
                elop=int(float(el1)/int(el2))
                evalstack.append(elop)
            else:
                evalstack.append(n)
        return(int(evalstack.pop()))
        