class SortedDoublyLinkedList():
    class _Node():
        def __init__(self, element, previous, next):
            self._next = next
            self._element = element
            self._previous=previous

        def get_previous(self):
            return self._previous

    def __init__(self):
        self._n = 0
        self._front = None

    def add_element(self, element):
        self._n += 1
        print(self._n)
        if (self._front == None):
            self._front = self._Node(element, None, None)
            return
        if (element < self._front._element):
            N = self._Node(element, None, self._front)
            self._front = N
            return
        temp = self._front
        while (temp._next != None):
            if (element < temp._element):
                N = self._Node(element, temp.get_previous(), temp)
                temp._previous._next = N
                temp._previous = N
                break
            else:
                temp = temp._next
        if (temp._next == None):
            if(temp._element>element):
                N=self._Node(element, temp.get_previous(), temp)
                temp._previous._next=N
                temp._previous=N
            else:
                N=self._Node(element, temp, None)
                temp._next=N

    def delete_element(self, target):
        temp=self._front
        while(temp != None):
            if(temp._element == target):
                if(temp._previous != None):
                    temp._previous._next=temp._next
                if(temp._next != None):
                    temp._next._previous=temp._previous
                break
            temp=temp._next

    def traverse(self):
        temp = self._front
        if (self._n > 0):
            while (temp != None):
                print(temp._element)
                temp = temp._next

S = SortedDoublyLinkedList()
S.add_element(15)
S.add_element(18)
S.add_element(16)
S.add_element(17)
S.traverse()
S.delete_element(16)
S.traverse()