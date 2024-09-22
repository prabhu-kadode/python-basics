class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        node = Node(data)
        if self.head==None:
            self.head = node
            return
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        
        last_node.next = node
    def display_nodes(self):
        current_node = self.head
        while(current_node):
            current_node.lol = True
            print(current_node.data)
            current_node = current_node.next
    def display_last_node(self):
        last_node = self.head
        prev = last_node
        while(last_node.next):
            prev = last_node
            last_node = last_node.next
        print(last_node)
       
    def check_item_existance(self,key):
        current_node = self.head
        while(current_node and current_node.data != key):
            current_node = current_node.next
        if current_node:
            print("Node",current_node.data,current_node.lol)
        else:
            print("no data")
    def delete_list(self,key):
         current_node = self.head
         if current_node.data == key:
           self.head = current_node.next
           current_node = None
           return 
         prev = current_node
       
         while(current_node and current_node.data != key):
            prev = current_node
            current_node = current_node.next
         if current_node:
            print("Node",current_node.data,current_node.lol)
            prev.next = current_node.next
          
         else:
            print("no data")
    def find_middle(self):
       
        slow = self.head
        fast = self.head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
           
        print(slow.data)
        
       
       
        
       

link = LinkList()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.append(6)
link.find_middle()
link.display_nodes()
link.delete_list(1)
link.display_nodes()

link.display_last_node()

link.check_item_existance(3)