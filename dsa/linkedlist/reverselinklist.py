class Linklist:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class ReverseLink:
    def __init__(self) -> None:
        self.head = None
    def append(self,data):
        if self.head is None:
            self.head = Linklist(data)
            return
        lastNode = self.head
        while(lastNode.next):
            lastNode = lastNode.next
        lastNode.next = Linklist(data)
        return lastNode
    def display(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        
        print(self.head)
    def reverse(self):
        current = self.head
        previous = None
        while(current):
            nextnode= current.next
            current.next = previous
            previous  = current
            current = nextnode
        
        self.head = previous
    def countNodes(self):
        count = 0
        current = self.head
        while(current):
            count+=1
            current = current.next
        print('total count',count)
        return count
    def displayNth(self,n):

        count = self.countNodes()
        if n > count:
            print("not possible")
            return 
        node = count - n
        temp = self.head
        print(node)
        for i in range(1,node+1):
            temp =temp.next
            print("sss",i)
        print(temp.data)
       


re = ReverseLink()
for i in range(1,6):
  re.append(i)
re.display()
re.reverse()
re.display()
re.countNodes()
re.displayNth(4)
