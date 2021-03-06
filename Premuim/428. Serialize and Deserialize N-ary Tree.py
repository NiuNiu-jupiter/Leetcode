"""
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

    For example, you may serialize the following 3-ary tree



    as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

    Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.



    For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

    You do not necessarily need to follow the above suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

     

    Constraints:

    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]
    Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial = []

        def preorder(node):
            if not node:
                return
            serial.append(node.val)

            for child in node.children:
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent
            return
        preorder(root)
      
        return serial
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        data = collections.deque(data)
        
        root = Node(data.popleft(), [])

        def helper(node):

            if not data:
                return

            while data[0] != "#": # add child nodes with subtrees
                value = data.popleft()
                child = Node(value, [])
                node.children.append(child)
                helper(child)

            data.popleft()        # discard the "#"

        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
