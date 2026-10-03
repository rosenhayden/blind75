#graph bfs on the matrix if we reach one of the edges of the matrix then iterate our exit counter
# for our vistited list we keep track of pairs bc the 'nodes' dont have values
# only had pairs that = "." to the queue
# as we traverse all pathes reachable from the start we check each nodes coordinates, if they are on the edge of the maze and not at the provided start, we have an exit.
# edge would be defined as
# maze[0][x] and maze[len(maze)][x] for any 0 <= x <= len(maze[0])
# maze[y][0] and maze[y][len(maze[0])] for any 0<= y <= len(maze)
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        q = deque([[entrance[0],entrance[1],0]])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            x0,y0,steps = q.popleft()
            #found exit
            if (0 in [x0,y0] or x0==m-1 or y0==n-1) and ([x0,y0] != entrance):
                return steps
            #traverse valid neighbors
            for xn,yn in directions:
                x,y=xn+x0,yn+y0
                if 0<=x<m and 0<=y<n and maze[x][y] == ".":
                    maze[x][y] = "+"
                    q.append([x,y,steps+1])
        return -1
