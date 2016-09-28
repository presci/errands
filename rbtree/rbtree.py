from utils.node import TreeNode as Node


class RBTree:
    def __init__(self):
        self.root= None
        pass
    def add(self, arg0):
        if self.root is None:
            self.root = Node(arg0, False)
            return
        self.__add(self.root, arg0)
    def __add(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = Node(value, False, node)
                self.rebalance(node.left)
            else:
                self.__add(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value, False, node)
                self.rebalance(node.right)
            else:
                self.__add(node.right, value)
    def rebalance(self, node):
        if node.isroot() is True:
            return node.black()
        if node.parent.red == False:
            return
        if node.uncle() is not None and node.uncle().red == True:
            node.parent.black()
            node.uncle.black()
            node.gp().red = True
            return self.rebalance(node.gp())
        self.pivot(node)
    def pivot(self, node):
        if node.gp() is None:
            return
        if node.parent.isleft() and node.isleft():
            node.parent.pivotright()
        if node.parent.isleft() and node.isright():
            node.pivotleft(true)
        if node.parent.isright() and node.isright():
            node.parent.pivotleft()
        if node.parent.isright() and node.isleft():
            node.pivotright(true)    
            
        
    def print__inline(self, node):
        if node is None:
            return
        if node.left is not None:
            self.print__inline(node.left)
        print node.value
        if  node.right is not None:
            self.print__inline(node.right)
            
            
rb= RBTree()
rb.add(10)
rb.add(40)
rb.add(5)
rb.add(35)
rb.add(2)
rb.print__inline(rb.root)
