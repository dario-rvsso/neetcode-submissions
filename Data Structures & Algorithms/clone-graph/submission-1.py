"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node == None:
            return None

        nodes = {}

        def clone(node, nodes):
            if node.val in nodes:
                return nodes[node.val]
            
            if node.val not in nodes:
                curr = Node()
                curr.val = node.val
                if curr.val not in nodes:
                    nodes[curr.val] = curr

                for neighbor in node.neighbors:
                    clone(neighbor, nodes)
                    if neighbor not in nodes[curr.val].neighbors:
                        nodes[curr.val].neighbors.append(nodes[neighbor.val])
                
                return curr
        
        clone(node, nodes)
        return nodes[node.val]

            