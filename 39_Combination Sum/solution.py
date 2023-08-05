#we have a list of numbers that are are supposed to be added up to a target number
#the combinations must be unique
#we can have a number repeat several times
#numbers = [2,3,6,7], target = 7
#solutions = [[2,2,3], [7]]

class solutions:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[]]:
        #we create a list to store all our subsets
        result = []

        #we create a dfs function that takes i(pointer to keep track of viable candidates)
        #current list that we are creating, and the total of the numbers in our current list

        def dfs(i, current:List[int], total: int):
            #if our total and our target are the same, we append the candidate to the current list and return
            if target ==total:
                result.append(current.copy())
                return 
            
            #if the total is larger than the target or i is larger than the list olfg candidates, we break out asap
            if total>target or i >= len(candidates):
                return 

            #if we choose to add candidate 
            result.append(candidate[i])
            dfs(i, current, total + candidate[i])

            #if we choose not to add candidate
            result.pop()
            dfs(i+1, current, total)

        #we then call dfs to start at index 0, with an empty current set and a total of 0
        dfs(0, [], 0)
        return result