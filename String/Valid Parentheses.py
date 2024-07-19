class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            n=len(stack)
            if n>0 and stack[0]=='(' and i==')':
                stack.pop(0)
            elif n>0 and stack[0]=='[' and i==']':
                stack.pop(0)
            elif n>0 and stack[0]=='{' and i=='}':
                stack.pop(0)
            else:
                stack.insert(0,i)
        return len(stack)==0
       
