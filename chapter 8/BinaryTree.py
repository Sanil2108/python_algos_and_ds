class BinaryTree():
    
    class _Node():
        
        def __init__(self, val):
            self.left = None
            self.right = None
            self.value = val
            self.parent = None
            self.before = 0

    def left(self, node):
        return node.left

    def right(self, node):
        return node.right

    def sibling(self, node):
        if(node.parent.left == node):
            return node.parent.right
        else:
            return node.parent.left
        
    def root(self):
        return self.root
    
    def parent(self, node):
        return node.parent
    
    def num_children(self, node):
        count=0
        if node.left != None:
            count+=1
        if node.right != None:
            count+=1
        return count

            
    def __init__(self, val):
        self.root = self._Node(val)
        self.current = self.root
    
    def add(self, value, node):
        n = self._Node(value)
        n.parent = node
        if(node.left == None):
            node.left = n
            n.before = node.before + 1
            return n
        elif(node.right == None):
            node.right = n
            n.before = node.before + 1
            return n
        else:
            raise Exception('Cannot insert more nodes here')
            
    def delete(self, node):
        if(node.parent.left == node):
            node.parent.left = None
        else:
            noe.parent.right = None
            
    def traverse(self):
        BinaryTree._traverse2(self.root)

    @staticmethod
    def _traverse2(root):
        for i in range(root.before):
            print('-', end='')
        print(root.value)
        if(root.left != None):
            BinaryTree._traverse2(root.left)
        if(root.right != None):
            BinaryTree._traverse2(root.right)