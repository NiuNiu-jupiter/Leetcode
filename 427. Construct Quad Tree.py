"""
    We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.
    
    Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.
    
    Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:
    
    Given the 8 x 8 grid below, we want to construct the corresponding quad tree:
    
    
    
    It can be divided according to the definition above:
    
    
    
    
    
    The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.
    
    For the non-leaf nodes, val can be arbitrary, so it is represented as *.
    
    
    
    Note:
    
    N is less than 1000 and guaranteened to be a power of 2.
    If you want to know more about the quad tree, you can refer to its wiki.
    
    """

"""
    # Definition for a QuadTree node.
    class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
    self.val = val
    self.isLeaf = isLeaf
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomLeft = bottomLeft
    self.bottomRight = bottomRight
    """
class Solution:
    def construct(self, grid):
        """
            :type grid: List[List[int]]
            :rtype: Node
            """
        
        if not grid:
            return None
        return self.build(grid)
    
    def build(self,grid):
        if not grid:
            return None
        n = len(grid)
        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        else:
            return Node('*',
                        False,
                        self.build([grid[i][:n//2] for i in range(0, n//2)]),
                        self.build([grid[i][n//2:] for i in range(0, n//2)]),
                        self.build([grid[i][:n//2] for i in range(n//2, n)]),
                        self.build([grid[i][n//2:] for i in range(n//2, n)])
                        )

def isLeaf(self, grid):
    s = set([grid[i][j] for i in range(len(grid[0])) for j in range(len(grid))])
    return len(s) == 1
