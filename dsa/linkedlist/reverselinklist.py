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


re = ReverseLink()
re.append(10)
re.append(20)
re.append(30)
re.display()
re.reverse()
re.display()
