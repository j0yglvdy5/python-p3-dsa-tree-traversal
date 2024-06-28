class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        # Helper function to perform depth-first search (DFS)
        def dfs(node):
            if node is None:
                return None
            # Check if current node matches the target_id
            if node.get('id') == target_id:
                return node
            # Recursively search in children
            for child in node.get('children', []):
                result = dfs(child)
                if result is not None:
                    return result
            return None

        # Start DFS from the root of the tree
        if self.root is None:
            return None
        return dfs(self.root)
