#Solution to the valid parenthesis problem
#using the stack to track pairs, hashmaps to put them together

class Solution :
    def isValid(self, s: string) -> bool:
        #initialize the stack
        stack =[]
        #initialize key value pairs
        closeToOpen = {')':'(', '}':'{', ']':'['}
        
        #go through every character in the input string
        for c in s:
            if c in closeToOpen:
                #if it is a closing bracket and there are no open brackets on top of the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(c)
                #return true or false depending upon whether all characters have been processed
        return True if not stack else False
