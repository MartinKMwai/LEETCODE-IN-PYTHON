#if we have 1, 2, 3, the subsets here will be 
#_, 1, 2, 3, (1,2), (1,3), (2,3), (1,2,3)
#bactracking, where for every number in the array, we dcide to add it to the subset or not

class Solution:
    def subset(self, nums:List[int]) -> List[int]:
        #create a result set where we store all of the sets we create
        result = []
        subset = [] #to store the subsets

        #create a dfs function and pass in the index of the number we are on
        def dfs(i):
            #if i is then larger than the length of our number array, we append a copy of our subset to the result and return
            if i >= len(nums):
                result.append(subset.copy())
                return 

            #in the case where we need to add the number i
            subset.append(nums[i])
            dfs(i+1)

            #in the case where we do not, we just pop the number we just added to the subset
            subset.pop()
            dfs(i+1)

            #pass the first index
        dfs(0)
        return result