class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_front(self, value):
        
        newNode=Node(value)
        
        newNode.next=self.head.next
        newNode.prev=self.head
        
        self.head.next.prev = newNode
        self.head.next = newNode
        
    
    def insert_back(self, value):
        
        newNode=Node(value)
        
        newNode.next=self.tail
        newNode.prev=self.tail.prev
        
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        
    def reverse(self):
        tempLinkedList= LinkedList()
        tempNode = self.head.next
        while(tempNode != self.tail):
            tempLinkedList.insert_front(tempNode.value)
            tempNode = tempNode.next
        
        self.head = tempLinkedList.head
        self.tail = tempLinkedList.tail

    def one_line_str(self):
        temp = self.head.next
        resultList = []
        while(temp != self.tail):
            resultList.append(temp.value)
            temp = temp.next 
        
        return " ".join(resultList)

    def size(self):
        temp = self.head.next
        size = 0
        while(temp != self.tail):
            size += 1
            temp = temp.next 
        return size
            
    def pop_front(self):
        value = self.head.next.value
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return value

    def pop_back(self):
        value = self.tail.prev.value
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return value



def getTask(task):
    result = task.split()
    return result

numOfTask = int(input())
tasks = []
for _ in range(numOfTask):
    task = input()
    tasks.append(getTask(task))

L = LinkedList()
for task in tasks:
    if(task[0]=="back"):
        if(L.size() == 0):
            print("No job")
        else:
            print(L.pop_back())
    elif(task[0]=="front"):
        if(L.size() == 0):
            print("No job")
        else:
            print(L.pop_front())
    elif(task[0]=="reverse"):
        L.reverse()
    elif(task[0]=="push_back"):
        L.insert_back(task[1])
    elif(task[0]=="push_front"):
        L.insert_front(task[1])
    
    # print(L.one_line_str())