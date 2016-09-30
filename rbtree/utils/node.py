class RBNode:
    def __init__(self,arg0, arg1=None,arg2=True):
        self.value=arg0
        self.parent=arg1
        self.red=arg2
        self.left = None
        self.right = None
    def __str__(self):
        return "value: {%s,%s}, parent: %s, left: %s, right: %s" % (str(self.value), str(self.red), self.getparent(), self.getleft(), self.getright())
    def getparent(self):
        if self.parent is None:
            return "None"
        return "{%s,%s}" % (str(self.parent.value), str(self.parent.red)) 
    def getleft(self):
        if self.left is None:
            return "None"
        return "{%s,%s}" % (str(self.left.value), str(self.left.red))
    def getright(self):
        if self.right is None:
            return "None"
        return "{%s,%s}" % (str(self.right.value), str(self.right.red))
    def isroot(self):
        if self.parent is None:
            return True
        return False
    def isleft(self):
        if self.parent is None:
            return None
        if self.parent.left is not None and  self.parent.left.value == self.value:
            return True
        return False
    def isright(self):
        return not self.isleft()
    def gp(self):
        if self.parent is None:
            return None
        if self.parent.parent is None:
            return None
        return self.parent.parent
    def uncle(self):
        if self.gp() is None:
            return None
        if self.parent.isleft():
            return self.parent.parent.right
        return self.parent.parent.left
    def black(self):
        self.red = False
        
