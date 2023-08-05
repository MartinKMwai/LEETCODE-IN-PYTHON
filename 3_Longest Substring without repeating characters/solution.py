#We use ther sliding window technique

class Solution:
    def LongestsubstringNoRepetition(self, s:string)->int:
        #create a set
        charSet= set()
        left = 0 #left pointer at the beginning of the string
        longest= 0 #the lolngest substring is 0 at the beginning

        #when the right pointer is still in the range of the string
        for right in range(len(s)):
            #when the character at the right pointer is in the set already
            while s[right] in charSet:
                #remove the character at the left pointer
                charSet.remove(s[left])
                #move the left pointer to the right
                left = left + 1
            #add the character in the right pointer to the set
            charSet.add(s[right])
            #calculate the length of the new set
            currentlength = right - left + 1
            #update our longest with the larger value between longest & currentlength
            longest = max(longest, currentlength)

        #return the longest string we have
        return longest

