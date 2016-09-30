from utils.node import RBNode as Node
import pdb



class RBTree:
    def __init__(self):
        self.root= None
    def add(self, value):
        if value == 110:
            pdb.set_trace()
        if self.root is None:
            self.root = Node(value, None, False)
            return
        return self.__add(value, self.root)
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
            return node.black()
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
            return self.pivotright(node.parent)
        if node.isleft() and node.parent.isright():
            return self.pivotright(node, True)
        if node.isright() and node.parent.isright():
            return self.pivotleft(node.parent)
        if node.isright() and node.parent.isleft():
            return self.pivotleft(node, True)    
    def pivotright(self, arg0, arg1=False):
        P = arg0.parent
        C = arg0.right
        GP = arg0.gp()
        arg0.right = P
        P.parent = arg0
        P.left = C
        P.red = True
        arg0.black()
        if C is not None:
            C.parent = P
        arg0.parent = GP
        if GP is not None:
            GP.left = arg0
        else:
            self.root = arg0
            arg0.black()
        if arg1 :
            self.pivotleft(arg0)    
    def pivotleft(self, arg0, arg1=False):
        P = arg0.parent
        C = arg0.left
        GP = arg0.gp()
        arg0.left = P
        P.parent = arg0
        P.right = C
        P.red = True
        arg0.black()
        if C is not None:
            C.parent = P
        arg0.parent = GP
        if GP is not None:
            GP.right = arg0
        else:
            self.root = arg0
            arg0.black()
        if arg1:
            self.pivotright(arg0)    
    def printme_inline(self, node):
        if node is None:
            return
        self.printme_inline(node.left)
        print node
        self.printme_inline(node.right)



rbtree= RBTree()
rbtree.add(10)
rbtree.add(30)
rbtree.add(40)
rbtree.printme_inline(rbtree.root)
print "---------------"
rbtree.add(7)
print "---------------"
rbtree.printme_inline(rbtree.root)
rbtree.add(57)
print "---------------"
rbtree.add(80)
#rbtree.add(25)
rbtree.printme_inline(rbtree.root)
