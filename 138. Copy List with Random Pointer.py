"""
    A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
    
    Return a deep copy of the list.
    
    
    
    Example 1:
    
    
    
    Input:
    {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
    
    Explanation:
    Node 1's value is 1, both of its next and random pointer points to Node 2.
    Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
    
    
    Note:
    
    You must return the copy of the given head as a reference to the cloned list.

    
"""
"""
    # Definition for a Node.
    class Node:
    def __init__(self, val, next, random):
    self.val = val
    self.next = next
    self.random = random
"""
def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return
        
    headcopy = Node(head.val,None,None)
    visited = {head:headcopy}
        
    queue = collections.deque()
    queue.append(head)
    while queue:
        cur = queue.popleft()
        n,r = cur.next,cur.random
        if n:
            if n not in visited:
                ncopy = Node(n.val,None,None)
                visited[n] = ncopy
                queue.append(n)
                visited[cur].next = visited[n]
        if r:
            if r not in visited:
                rcopy = Node(r.val,None,None)
                visited[r] = rcopy
                visited[cur].random = visited[r]
    return headcopy
