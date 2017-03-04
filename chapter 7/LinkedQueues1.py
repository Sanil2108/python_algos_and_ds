class LinkedQueue1():
    
    #---Custom _Node implementation---#
    class _Node():
        
        def __init__(self, element, next):
            self._element=element
            self._next=next
    #---Class ended---#
    
    def __init__(self):
        self._n=0
        self._front=None
        
    def __len__(self):
        return self._n
        
    def enqueue(self, value):
        N=_Node(value, self._front)
        self._front=N
        self._n+=1
        
    def dequeue(self):
        if(self._n==0):
            raise Exception('Queue is empty')
            
        N=self._front
        while(N._next!=None):
            N=N._next
            
        ans=N.element
        self._n-=1
        
        return ans

    def first(self):
        N=self._front
        while(N._next!=None):
            N=N._next
        return N