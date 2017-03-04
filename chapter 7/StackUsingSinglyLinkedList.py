class CustomStacksUsingLL2():
    
    #---Custom _Node class---#
    class _Node():
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element=element
            self._next=next
    #---Class ended---#
    
    def __init__(self):
        self._size = 0
        self._head = None
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size==0
    
    def push(self, value):
        self._head=_Node(value, self._head)
        self._size+=1
        
    def top(self):
        if(self.is_empty()):
            raise Exception('Empty')
        return self._head
    
    def pop(self):
        if(self.is_empty()):
            raise Exception('Empty')
        ans=self._head._element
        self._size-=1
        self._head=self._head._next
        return ans