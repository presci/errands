from utils.node import RBNode as Node
import pdb



class RBTree:
    def __init__(self):
        self.root= None
    def add(self, value):
        if self.root is None:
            self.root = Node(value, None, False)
            return
        self.__add(value, self.root)
    def __add(self, value, node):
        if node.value > value:
            if node.left is None:
                node.left = Node(value, node)
                self.rebalance(node.left)
            else:
                self.__add(value, node.left)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value, node)
                self.rebalance(node.right)
            else:
                self.__add(value, node.right)
    def rebalance(self, node):
        ## Case 1
        if node.isroot():
            self.root = node
            node.black()
            return
        ## Case 2
        if not node.parent.red:
            return
        ## Case 3
        uncle = node.uncle()
        if uncle is not None and uncle.red and node.parent.red:
            uncle.red = False
            node.parent.red = False
            node.gp().red = True
            self.rebalance(node.gp())
        ## Case 4
        self.pivot(node)
    def pivot(self, node):
        if node.isleft() and node.parent.isleft():
            self.pivotright(node.parent)
        elif node.isleft() and node.parent.isright():
            self.pivotright(node, True)
        elif node.isright() and node.parent.isright():
            self.pivotleft(node.parent)
        elif node.isright() and node.parent.isleft():
            self.pivotleft(node, True)    
    def pivotright(self, arg0, arg1=False):
        if arg0.value == 230:
            pdb.set_trace()
        P = arg0.parent
        C = arg0.right
        GP = arg0.gp()
        arg0.right = P
        P.parent = arg0
        P.left = C
        if C is not None:
            C.parent = P
        arg0.parent = GP
        if GP is not None:
            GP.left = arg0
        if arg1 :
            self.pivotleft(arg0)
        else:
            arg0.red = False
            P.red = True
        self.rebalance(arg0)
    def pivotleft(self, arg0, arg1=False):
        P = arg0.parent
        C = arg0.left
        GP = arg0.gp()
        arg0.left = P
        P.right = C
        if C is not None:
            C.parent = P
        arg0.parent = GP
        if GP is not None:
            GP.right = arg0
        if arg1:
            self.pivotright(arg0)
        else:
            arg0.red = False
            P.red = True
        self.rebalance(arg0)
    def printme_inline(self, node):
        if node is None:
            return
        self.printme_inline(node.left)
        print node
        self.printme_inline(node.right)



rbtree= RBTree()
rbtree.add(40)
rbtree.add(30)
rbtree.add(10)
rbtree.add(50)
rbtree.add(75)
rbtree.add(300)
rbtree.add(345)

rbtree.printme_inline(rbtree.root)
