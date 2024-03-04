class TreeNode():
    def __init__(self, value, left =-1, right = -1) -> None:
        self.left = left
        self.right = right
        self.value = value
    #end constructor
#end record

treelist = []

def insertTreeNode(treelist, value):
    newNode = TreeNode(value)
    if len(treelist) == 0:
        treelist[0] = newNode
    else:
        current = 0
        next = 0
        while next != -1:
            if value < treelist[current].value:
                next = treelist[current].left         