#code on how to find out if a word/phrase reads the same forwards and backwards
#USING POINTERS and little to no external libraries

class Solution:

    #create a helper function to define alphanumerism
    def alphanumeric(self, c):
        #if the asciii lies between A-Z or a-z or 0-9
        return (ord('A')<=ord(c)<=ord('Z') or
               ord('a')<=ord(c)<=ord('a')or 
               ord('0')<=ord(c)<=ord('9'))


    def isPalindrome(self, s:str) -> bool:
        #initialize the pointers first
        #left begins at 0, right begins at the string length - 1
        left, right = 0, len(s) - 1
        #while loop when pointers are valid
        while left< right:
            #if this is met but the character is not alphanumeric, increment the relevsnt pointer
            while left<right and not self.alphanumeric(s[left]):
                left += 1
            while left<right and not self.alphanumeric(s[right]):
                right += 1
        #compare the two characters in the pointers
        if s[left].lower() != s[right].lower():
            return False
        #increment the left pointer, decrement the right one so as to compare the next values
        left, right = left + 1, right - 1

        #if the loop is complete, then the phrase is a palindrome
        return True  

        