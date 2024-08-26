class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def getHeight(self):
        l = 0
        r = 0
        if(self.left):
            l = self.left.getHeight()
        if(self.right):
            r = self.right.getHeight()

        if(l > r):
            return(l+1)
        else:
            return(r+1)

    def isBalancedBinaryTree(self):

        if(self.left is None and self.right is None):
            return True

        if(self.left):
            lh = self.left.getHeight()
            print("lh -> ", lh)
        if(self.right):
            rh = self.right.getHeight()
            print("rh -> ", rh)

        if (abs(lh - rh) <= 1) and self.left.isBalancedBinaryTree() is True and self.right.isBalancedBinaryTree() is True:
            return True
        return False


t = Tree(10)
t.left = Tree(20)
t.right = Tree(30)
t.left.left = Tree(40)
t.left.right = Tree(50)

print("is Balanced Binary Tree ", t.isBalancedBinaryTree())
