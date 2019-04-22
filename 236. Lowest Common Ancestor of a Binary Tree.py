
"""
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    
    Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
    
    
    
    
    Example 1:
    
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    Example 2:
    
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    
    
    Note:
    
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    return dfs(root, p, q)

def dfs(node, p , q):
    
    # If looking for me, return myself
    if not node or node == p or node== q:
        return root
    
    # else look in left and right child
    left = dfs(node.left, p ,q )
    right = dfs(node.right, p, q)

    # if both children returned a node, means
    # both p and q found so parent is LCA
    if left and right:
        return node
    else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way,
        # because in such scenarios, node where 'p' found is LCA
        return left if left else right





