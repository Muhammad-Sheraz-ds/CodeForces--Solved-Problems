import random


class doublyLinkedList:
    class Node:
        def __init__(self,data=None):
            self.data=data
            self.next=None
            self.prev=None

    class DLLIterator:
        def __init__(self, node=None):
            self.current = node
        def __eq__( self, rhs ):
            return self.current == rhs.current
        def __ne__( self, rhs ):
            return self.current != rhs.current
        def getObject( self ):
            return self.current.data
        def __iter__(self):  # this is not mandatory, why
            return self
        def __next__( self ):
            if self.current.next.next != None: # tail ????
                cur_node = self.current
                self.current = self.current.next
                return self
            else:
                raise StopIteration
        def remove( self ):
            if self.current != None and self.current.prev != None and self.current.next != None:
                self.current.next.prev = self.current.prev
                self.current.prev.next = self.current.next
                tmp = self.current
                self.__next__()
                del tmp

    class DLLRIterator:
        def __init__(self, node=None):
            self.current = node
        def __eq__( self, rhs ):
            return self.current == rhs.current
        def __ne__( self, rhs ):
            return self.current != rhs.current
        def getObject( self ):
            return self.current.data
        def __iter__(self):  # this is mandatory, why
            return self
        def __next__( self ):
            if self.current.prev.prev != None: # head
                cur_node = self.current
                self.current = self.current.prev
                return self
            else:
                raise StopIteration

    def __init__(self):
        self.head=self.Node()
        self.tail=self.Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def __iter__(self):
        return self.DLLIterator(self.head)

    def __reversed__(self):
        return self.DLLRIterator(self.tail)

    def begining(self):
        return self.DLLIterator(self.head)

    def end(self):
        return self.DLLIterator(self.tail.prev)

    def rbegining(self):
        return self.DLLRIterator(self.tail)

    def rend(self):
        return self.DLLRIterator(self.head.next)

    def add_node(self,o):
        if self.head.next==None:
            t = self.Node(o)
            t.next = self.tail
            self.head.next=t
            t.prev = self.head
            self.tail.prev = t

        else:
            t = self.head.next
            while t!=self.tail:
                if t.data > o:
                    break
                t=t.next
            tmp=self.Node(o)
            tmp.next = t
            tmp.prev = t.prev
            t.prev.next=tmp
            t.prev = tmp



def main():
    n,q= map(int,input().split())
    array = list(map(int,input().split()))
    dll = doublyLinkedList()
    sum= [0]*n
    for i in range(n):
        dll.add_node(array[i])
    i=0
    for val in dll:
        sum[i] = sum[i-1]+val.getObject()
        i+=1


    for i in range(q):
        x,y= map(int,input().split())
        id=x-y-1
        print(sum[x]-sum[id])


main()

