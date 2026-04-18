# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        res = []
        
        def dfs(node):
            if not node:
                res.append("#")
                return
            # Root -> Left -> Right (Pre-order)
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # Split by our delimiter and convert to a list/iterator
        vals = data.split(",")
        i = 0 # Pointer to track our position in the list
        
        def dfs():
            nonlocal i
            if vals[i] == "#":
                i += 1
                return None
            
            # Create the node and move the pointer
            node = TreeNode(int(vals[i]))
            i += 1
            
            # Recurse in the exact same order as serialization
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()