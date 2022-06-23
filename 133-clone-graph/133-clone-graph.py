"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return node
        
        
        # DFS failed, let's try BFS
        # Why am i trying BFS? what is the trafeoff?
        # because BFS is iterative and controlled traversal
        
        graph = defaultdict(Node)
        graph[node.val] = Node(node.val)
        queue = deque([node])
        
        while queue:
            currNode = queue.popleft()
            # ⭐️ picking up nodes from a hashmap
            # inside BFS was new for me
            clone = graph[currNode.val]
            
            for child in currNode.neighbors:
                
                if child.val not in graph:
                    graph[child.val] = Node(child.val)
                    # ⭐️This is brilliant. Only append nodes
                    # if not in graph otherwise simply add to child
                    queue.append(child)
                    
                clone.neighbors.append(graph[child.val])
                
                
        return graph[node.val]
                
        