

class TreeNode:
    def __init__(self, arg0, arg1=True, arg2=None):
        self.value = arg0
        self.right = None
        self.left = None
        self.parent = arg2
        self.red = arg1
    def parent(self, arg0):
        if self.parent is None:
            return None
        return self.parent
    def sibling(self, arg0):
        if self.parent is None:
            return None
        if self.parent.left.value == self.value:
            return self.parent.right
        return self.parent.left
    def isroot(self):
        if self.parent is None:
            return True
        return False
    def black(self):
        self.red = False
    def gp(self):
        if self.parent is None:
            return None
        if self.parent.parent is None:
            return None
        return self.parent.parent
    def isleft(self):
        if self.parent is None:
            return None
        if self.parent.left.value = self.value:
            return True
        return False
    def isright(self):
        return not self.isleft()
    def pivotright(self, arg0=False):
        p=self.parent
        r=self.right
        gp=self.parent.parent
        self.right = p
        p.parent = self
        if gp is not None:
            gp.left = self
            self.parent = gp
        if r is not None:
            p.left = r
            r.parent = p
        if arg0:
            self.pivotleft()
    def pivotleft(self, arg0=False):
        p=self.parent
        l = self.left
        gp= self.parent.parent
        self.left = p
        p.parent= self
        if gp is not None:
            gp.left = self
            self.parent = gp
        if l is not None:
            p.right = l
            l.parent= p
        if arg0:
            self.pivotright()    
            
                
        
    
            
