#wer are given a grid with 0 and 1, assuming that this grid is surrounded by 0.
#assujme that any adjacent 1, connected vertically or horizontally, are an island
#reurn the number of isloands in our grid

class Solution:
    def numberofIslands(self, grid:[List[List[str]]])->int:
        #if we do not have a grid, then we return 0
        if not grid:
            return 0

        #we define the dimensions of our grid
        rows, columns = len(grid), len(grid[0])
        #create a set fot for the visited positions
        visit= set()
        #create an island counter to track number of islands
        island = 0

        #we are using a bfs to visit all the 1 and those that are adjacent to it
        def bfs(row, column):
            #create a double-edged queue from which we pop and add stiuff we have visited and should visit respectively
            queue = collections.deque()
            visit.add(row, column)
            queue.append((row, column))

            #while we still have a queue, we continue expanding out island
            while queue:
                #while we have a queue, we pop the element we are gonna visit
                row, column = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                #
                for drow, dcolumn in directions:
                    if ((r + drow) in range (rows) and 
                    (c + dcolumn) in range (columns) and 
                    grid[r + drow][c+dcolumn]=="1" and 
                    ((r+drow), (c+dcolumn)) not in visit):

                        queue.append(((row+drow), (column+dcolumn)))
                        visit.add(((row+drow), (column+dcolumn)))

        for row in range (rows):
                for column in range (column):
                    if grid[row][column]=='1' and (row, column) not in visit:
                        bfs(row, column)

                        island = island + 1
        return islands




