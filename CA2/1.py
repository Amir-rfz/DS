import sys
import re


class Queue:
    def __init__(self):
        self.__data = []

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        return self.__data.pop(0)

    def size(self):
        return len(self.__data)

    def empty(self):
        return len(self.__data)==0

    def one_line_str(self):
        return " ".join(self.__data)


class Stack:
    def __init__(self, capacity=10):
        self.__data = []
        self._capacity = capacity

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        return self.__data.pop(-1)

    def put(self, value):
        self.pop()
        self.push(value)

    def peek(self):
        return self.__data[self.size()-1]

    def expand(self):
        self._capacity *= 2

    def capacity(self):
        return self._capacity

    def size(self):
        return len(self.__data)

    def empty(self):
        return len(self.__data)==0

    def one_line_str(self):
        return " ".join(self.__data)


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

    
class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
