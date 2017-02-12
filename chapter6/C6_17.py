class CustomStack2():
    def __init__(self, size):
        self.data=[0]*size
        self._n=0

    def __len__(self):
        return self._n

    def push(self, a):
        if(len(self.data)<self._n+1):
            self.data.append(a)
        else:
            self.data[self._n]=a
        self._n+=1
        return self.data[:self._n]

    def pop(self):
        if(self._n>0):
            self._n-=1
            return self.data[self._n]

    def top(self):
        return self.data[self._n-1]

    def is_empty(self):
        return self._n==0
