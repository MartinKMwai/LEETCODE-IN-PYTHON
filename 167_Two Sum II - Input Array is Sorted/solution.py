#Same as the regular 2 sum but the array is sorted
#indexes begin at 1, not 0
#Solution Guaranteed
#Cannot use an element twice

class Solution:
    def twoSum(self, numbers:List[int], target:int)->List[int]:
        #left pointer at the beginning, right pointer at the end
        left, right = 0, len(numbers)- 1
        #create a loop that runs as long as the left pointer is smaller than the right one
        while left< right:
            #add the numbers at these pointers
            CurrentSum = numbers[left] +numbers [right]
            #create an if statement
            #if sum> target, move the right pointer to the left
            if CurrentSum > target:
                right = right - 1
            #if sum<target, move left pointer to the right
            elif CurrentSum < target:
                left = left+1
            #if sum = target, return the indices, +1
            else:
                return [left+1, right+1]