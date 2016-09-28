class RBNode:
    def __init__(self,arg0, arg1=None,arg2=False):
        self.value=arg0
        self.parent=arg1
        self.red=arg2
        self.left = None
        self.right = None
    def isleft(self):
        if self.parent is None:
            return None
        if self.parent.left.value == self.value:
            return True
        return false
    def isright(self):
        return not self.isleft()
    def pivotright(self, arg0=False):
        gp = self.gp()
        p = self.p
        r = self.r
        p.parent = self
        self.right = p
        if gp is not None:
            gp.right = self
            self.parent = gp
        if r is not None:
            p.left=r
            r.parent=p
        if arg0 :
            self.pivotleft()    
    def pivotleft(self, arg0=False):
        gp = self.gp()
        p = self.p
        l = self.l
        self.left = p
        p.parent = self
        if gp is not None:
            self.parent = gp
            gp.right = self
        if l is not None:
            l.parent = p
            p.right = l
        if arg0:
            self.pivotright()
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
                
