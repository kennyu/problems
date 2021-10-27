from typing import List
import copy
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        self.grid = copy.deepcopy(grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    islands += 1
                    self.mark_island(i,j)
        return islands

    def mark_island(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] != "1":
            return
        self.grid[i][j] = "2"

        self.mark_island(i+1,j)
        self.mark_island(i,j+1)
        self.mark_island(i-1,j)
        self.mark_island(i,j-1)

# Test Cases
l1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
s = Solution()
print(s.numIslands(l1))
