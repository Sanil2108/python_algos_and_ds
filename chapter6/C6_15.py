class CustomStack():
    def __init__(self):
        self._n=0
        self._data=[]
        
    def push(self, val):
        self._data.append(val)
        self._n+=1
        
    def pop(self):
        if(self.is_empty()==False):
            self._n-=1
            return self._data[self._n]
    
    def is_empty(self):
        return self._n==0
    
    def __len__(self):
        return self._n
    
    def top(self):
        return self._data[self._n]

c1=CustomStack()
c2=CustomStack()
c1.push(3)
c1.push(1)
c1.push(3)
c1.push(4)
c1.push(7)

x=c1.pop()
if(x<c1.top()):
    x=c1.pop()