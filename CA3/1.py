import sys
import re

INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'

class MinHeap:
    class Node:
        def __init__(self, value):
            self.value = value

    def __init__(self):
        self.heap = []

    def bubble_up(self, index):
        if not isinstance(index, int):
            raise Exception('invalid index')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].value < self.heap[parent].value:
                temp = self.heap[index]
                self.heap[index] = self.heap[parent]
                self.heap[parent] = temp
                index = parent
            else:
                break

    def bubble_down(self, index):
        if not isinstance(index, int):
            raise Exception('invalid index')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        last_index = len(self.heap) - 1
        while True:
            smallest_index = index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if right_child_index <= last_index and self.heap[right_child_index].value < self.heap[smallest_index].value:
                smallest_index = right_child_index
            if left_child_index <= last_index and self.heap[left_child_index].value < self.heap[smallest_index].value:
                smallest_index = left_child_index
            if smallest_index != index:
                temp = self.heap[index]
                self.heap[index] = self.heap[smallest_index]
                self.heap[smallest_index] = temp
                index = smallest_index
            else:
                break

    def heap_push(self, value):
        self.heap.append(self.Node(value))
        self.bubble_up(len(self.heap) - 1)

    def heap_pop(self):
        if len(self.heap) == 0:
            raise Exception('empty')
        if len(self.heap) == 1:
            return self.heap.pop().value
        root = self.heap[0].value
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root

    def find_min_child(self, index):
        if not isinstance(index, int):
            raise Exception('invalid index')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if right_child_index >= len(self.heap):
            if left_child_index >= len(self.heap):
                return None
            return left_child_index
        if self.heap[left_child_index].value < self.heap[right_child_index].value:
            return left_child_index
        return right_child_index

    def heapify(self, *args):
        self.heap = []
        for value in args:
            self.heap.append(self.Node(value))
        start_index = (len(self.heap) // 2) - 1
        for i in range(start_index, -1, -1):
            self.bubble_down(i)

class HuffmanTree:
    class Node:
        def __init__(self, char=None, freq=None):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def __init__(self):
        self.root = None
        self.letters = []
        self.repetitions = []
        self.codes = {}
        self.min_heap = MinHeap()

    def set_letters(self, *args):
        self.letters = args

    def set_repetitions(self, *args):
        self.repetitions = list(map(int, args))

    def build_huffman_tree(self):
        for i in range(len(self.letters)):
            char = self.letters[i]
            freq = self.repetitions[i]
            node = HuffmanTree.Node(char, freq)
            self.min_heap.heap_push(node)

        while len(self.min_heap.heap) > 1:
            left = self.min_heap.heap_pop()
            right = self.min_heap.heap_pop()
            merged = HuffmanTree.Node(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            self.min_heap.heap_push(merged)

        self.root = self.min_heap.heap_pop()
        self._generate_codes(self.root, "")

    def _generate_codes(self, node, current_code):
        if node is not None:
            if node.char is not None:
                self.codes[node.char] = current_code
            self._generate_codes(node.left, current_code + "0")
            self._generate_codes(node.right, current_code + "1")

    def get_huffman_code_cost(self):
        cost = 0
        for char, freq in zip(self.letters, self.repetitions):
            cost += freq * len(self.codes[char])
        return cost

    def text_encoding(self, text):
        freq = {}
        for char in text:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        self.letters = list(freq.keys())
        self.repetitions = list(freq.values())
        self.build_huffman_tree()
        encoded_text = ''.join(self.codes[char] for char in text)




class Bst:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert_recursive(node, key):
            if node is None:
                return Bst.Node(key)
            if key < node.key:
                node.left = _insert_recursive(node.left, key)
            elif key > node.key:
                node.right = _insert_recursive(node.right, key)
            return node
        
        self.root = _insert_recursive(self.root, key)

    def inorder(self):
        def inOrderRecursive(node):
            if node:
                inOrderRecursive(node.left)
                print(node.key, end=' ')
                inOrderRecursive(node.right)

        inOrderRecursive(self.root)
        print()
    

class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()

