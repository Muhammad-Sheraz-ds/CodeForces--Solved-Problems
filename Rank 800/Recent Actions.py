class Node:
    def __init__(self,data,previous=None,next=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None,self.head)
        self.head.next=self.tail
        self.size = 0

    def insert_first(self,obj):
        tmp = Node(obj,self.head,self.head.next)
        self.head.next.previous = tmp
        self.head.next=tmp
        self.size+=1

    def insert_top(self,obj):
        tmp = Node(obj,self.head,self.head.next)
        self.head.next.previous=tmp
        self.head.next=tmp
        self.size+=1


    def insert_end(self,obj):
        tmp = Node(obj,self.tail.previous,self.tail)
        self.tail.previous.next = tmp
        self.tail.previous = tmp
        self.size += 1

    def isert_before(self,n1,n2):
        if self.is_empty():
            raise ('Empty list')
        else:
            t = self.head.next
            while True:
                if t == self.tail:
                    raise (f'{n1} is not in list')
                if t.data == n1:
                    break
                t = t.next
            tmp = Node(n2)
            tmp.next = t
            tmp.previous = t.previous
            t.previous.next = tmp
            t.previous = tmp
            self.size+=1

    def insert_after(self,n1,n2):
        if self.is_empty():
            self.head = Node(n2)
            self.tail = Node(n2)
            self.size=1
        else:
            t = self.head.next
            while True:
                if t==self.tail:
                    raise f'{n1} is not in the list'
                if t.data==n1:
                    tmp = Node(n2,t,t.next)
                    t.next.previous = tmp
                    t.next = tmp
                    self.size+=1
                    break
                t = t.next

    def append(self,item):
        tmp = Node(item,self.tail.previous,self.tail)
        self.tail.previous.next = tmp
        self.tail.previous = tmp
        self.size+=1

    def __str__(self):
        s = ''
        cn = self.head.next
        while True:
            s+=str(cn.data) + ' '
            if cn.next == self.tail:
                break
            cn = cn.next
        return s

    def remove(self,item):
        if self.size == 0:
            raise ('Empty list')
        else:
            t = self.head.next
            while t.data != item:
                t = t.next
            t.previous.next = t.next
            t.next.previous = t.previous
            self.size-=1
    def is_empty(self):
        return self.size==0

    def is_present(self,item):
        t = self.head.next
        while t!=self.tail:
            if t.data==item:
                return True
            t=t.next
        return False


def Recent_Action():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        lst = DoubleLinkedList()
        l = list(map(int,input().split()))
        for j in range(1,n+1):
            lst.append(j)
        for i in l:
            if not lst.is_present(i):
                lst.remove(lst.tail.previous.data)
            else:
                lst.remove(i)
            lst.insert_top(i)
        print(lst)
Recent_Action()