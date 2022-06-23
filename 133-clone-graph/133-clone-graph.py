"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def localdfs(self,node):
        if node not in self.visited:
            self.visited.add(node)
            print(node.val)
            print(node.neighbors)
            print("")
            for child in node.neighbors:
                self.localdfs(child)
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = set()
        if not node:
            return node
        graph = defaultdict(Node)
        graph[node] = Node(node.val)
        
        def dfs(node,graph):
            
            for child in node.neighbors:
                if child not in graph:
                    graph[child] = Node(child.val)
                    graph[node].neighbors.append(graph[child])
                    # print(graph[node].neighbors)
                    dfs(child,graph)
                else:
                    graph[node].neighbors.append(graph[child])
        
        dfs(node,graph)
        # self.localdfs(graph[node])
        return graph[node]
                
                
        