class DoctorNode: 
    def __init__(self,name:str):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree: 
    def __init__(self):
        self.root = None

    def _find(self, node, name): 
        if node is None:
            return None
        if node.name == name:
            return node
        left = self._find(node.left, name)
        if left: 
            return left
        return self._find(node.right, name)
    
    def insert(self, parent_name, child_name, side):
        if self.root is None: 
            print("Error: The tree has no root yet.")
            return False
        
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Error: Parent doctor '{parent_name}' not found in the tree.")
            return False
        
        side = side.lower()
        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return False
        

        new_node = DoctorNode(child_name)


        if side == "left":
            if parent.left is None:
                parent.left = new_node
            else: 
                print(f"Error: Left child of '{parent_name}' already has a left report.")
                return False
        else:
            if parent.right is None: 
                parent.right = new_node
            else:
                print(f"Error: Right child of '{parent_name}' already has a right report.")
                return False
            
        return True
    
    def preorder(self, node):
        if node is None: 
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
    
    def inorder(self, node): 
        if node is None: 
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
    
    def postorder(self, node):
        if node is None: 
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
    


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))


    tree.insert("Dr. Phan", "Dr.Newton", "middle") 
    tree.insert("Dr. Nobody", "Dr.Y", "left")
    tree.insert("Dr. Phan", "Dr.Extra", "left")
