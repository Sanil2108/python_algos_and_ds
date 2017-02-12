class CustomQueues1():
    def __init__(self):
        self._front=-1
        self._n=0
        self._data=[]
        
    def enqueue(self, val):
        if(self._front is -1):
            self._front+=1
        self._data.append(val)
        self._n+=1
    
    def dequeue(self):
        if(self.is_empty()):
            raise Exception('Queue is empty')
        else:
            self._front+=1
            return self._data[self._front-1]
    
    def is_empty(self):
        if(self._front!=-1):
            return self._n-1<self._front
        else:
            return True
        
    def __len__(self):
        if(self.is_empty()==False):
            return self._n-self._front
        else:
            return 0
        
    def top(self):
        if(self.is_empty()):
            raise Exception('Queue is empty')
        else:
            return self._data[self._front]