class Node:
    def __init__(self, value):
        self.Value = value
        self.Left = None
        self.Right = None
        
class TREE:
    def __init__(self, Numbers):
        self.Numbers = Numbers
        New_node = Node(1)
        self.root = New_node
    
    def Inserts(self):
        Parents = [self.root]
        Level = 1
        while( self.Numbers):
            Level = Level + 1
            New_parents = []
            for Parent in Parents:
                Left, Right = map( int, input().split())
                if Left != -1:
                    New_node = Node(Left)
                    Parent.Left = New_node
                    New_parents.append( New_node)
                if Right != -1:
                    New_node = Node(Right)
                    Parent.Right = New_node
                    New_parents.append( New_node)
                self.Numbers -= 1
            Parents = New_parents
        self.MaxLevel = Level
        return
    
    def Inorder(self, root):
        Return_array = []
        Parents = []
        while True:
            while root:
                Parents.append( root)
                root = root.Left
            if Parents:
                Current = Parents.pop()
                Return_array.append( Current.Value)
                root = Current.Right
            else:
                break
        return Return_array
        
    
    def Swapper( self, k, root):
        Parents = [root]
        Defaultk = k
        level = 1
        while level <= self.MaxLevel:
            New_Parents = []
            if level == k:
                for Child in Parents:
                    if not Child:
                        continue
                    Child.Left, Child.Right = [Child.Right, Child.Left]
                k = k + Defaultk
            for Child in Parents:
                if not Child:
                    continue
                New_Parents.append( Child.Left)
                New_Parents.append( Child.Right)
            level = level + 1
            Parents = New_Parents
        
def Query_solver( Tree, Queries):
    Answers = []
    for k in Queries:
        Tree.Swapper(k, Tree.root)
        Inorder = Tree.Inorder( Tree.root)
        Answers.append( Inorder)
    return Answers

if __name__ == '__main__':
    Nodes = int( input())
    tree = TREE(Nodes)
    tree.Inserts()
    Queries = []
    Count = int( input())
    while Count:
        Count -= 1
        Queries.append( int( input()))
    Answers = Query_solver( tree, Queries)
    print( '\n'.join( [ ' '.join( str(x) for x in Ans) for Ans in Answers]))
    exit(0)