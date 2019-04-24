"""
    You are given a binary tree in which each node contains an integer value.
    
    Find the number of paths that sum to a given value.
    
    The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
    
    The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
    
    Example:
    
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
    
        10
       /  \
      5   -3
     / \    \
    3   2   11
   / \   \
  3  -2   1
    
    Return 3. The paths that sum to 8 are:
    
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11

"""
import collections
def dfs(root, target, curr, pre_dic):
    if not root:
        return 0
        
        curr += root.val
        
        res = 0
        if curr - target in pre_dic:
            res += pre_dic[curr - target]

        pre_dic[curr] += 1
        
        res += self.dfs(root.left, target, curr, pre_dic)
        res += self.dfs(root.right, target, curr, pre_dic)
        
        pre_dic[curr] -= 1
        
        return res

def pathSum(root: TreeNode, sum: int) -> int:
    
        dic = collections.defaultdict(int)
        dic[0] = 1
        return self.dfs(root, sum, 0, dic)


