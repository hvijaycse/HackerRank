class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def topView(root, Dict = {}, Level =0, height = 0):
    if not root:
        return
    if Level not in Dict:
        Dict[Level] = [root.info, height]
    else:
        if Dict[Level][1] > height:
            Dict[Level] = [root.info, height] 
    topView(root.left, Dict, Level - 1, height + 1)
    topView(root.right, Dict, Level + 1, height + 1)
    if Level == 0:
        for i in sorted(Dict):
            print( Dict[i][0], end = ' ')
    
        
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)