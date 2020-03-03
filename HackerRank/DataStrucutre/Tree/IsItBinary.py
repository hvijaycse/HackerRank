class MYNode:
    def __init__(self, Data):
        self.data = Data
        self.left = None
        self.right = None

class myBinaryTree:
    def __init__(self):
        self.root  = None
        
    def Insert(self, Node_data):
        New_Node = MYNode( Node_data)
        root = self.root
        if not root:
            self.root = New_Node
            return
        while root:
            parent =  root
            if Node_data < root.data:
                root = root.left
            elif Node_data > root.data:
                root = root.right
            else:
                return False
        if parent.data > Node_data:
            parent.left = New_Node
        else:
            parent.right = New_Node
        return True

def Level( root):
    if not root:
        return []
    return_array = []
    Parents =[root]
    while Parents:
        child = []
        for Parent in Parents:
            if Parent:
                return_array.append( Parent.data)
                child.append( Parent.left)
                child.append( Parent.right)
        Parents = child
    return return_array
            

def check_binary_search_tree_(root):
    if not root:
        return False
    My_tree = myBinaryTree()
    My_tree.Insert(root.data)
    Childs = [root.left, root.right]
    while Childs:
        SemiChild = []
        for child in Childs:
            if child:
                if not My_tree.Insert( child.data):
                    return False
                SemiChild.append( child.left)
                SemiChild.append( child.right)
        Childs = SemiChild
    Orginal_Level = Level(root)
    My_Level = Level( My_tree.root)
    if Orginal_Level != My_Level:
        return False
    else:
        return True
    