#Fibonacci Heap implementation
import math

class FibonacciHeapNode:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        self.next = self
        self.prev = self

class FibonacciHeap:
    def _init_(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key, value):
        new_node = FibonacciHeapNode(key, value)
        self._merge_into_root_list(new_node)
        if self.min_node is None or new_node.key < self.min_node.key:
            self.min_node = new_node
        self.total_nodes += 1
        return new_node

    def _merge_into_root_list(self, node):
        if self.min_node is None:
            self.min_node = node
        else:
            node.next = self.min_node.next
            node.prev = self.min_node
            self.min_node.next.prev = node
            self.min_node.next = node

    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                children = []
                child = min_node.child
                while True:
                    children.append(child)
                    child = child.next
                    if child == min_node.child:
                        break
                for child in children:
                    self._merge_into_root_list(child)
                    child.parent = None

            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev

            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()

            self.total_nodes -= 1

        return min_node

    def _consolidate(self):
        max_degree = int(math.log2(self.total_nodes)) + 1
        degree_table = [None] * (max_degree + 1)
        nodes = []
        x = self.min_node
        while True:
            nodes.append(x)
            x = x.next
            if x == self.min_node:
                break

        for w in nodes:
            x = w
            d = x.degree
            while degree_table[d] is not None:
                y = degree_table[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                degree_table[d] = None
                d += 1
            degree_table[d] = x

        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None or node.key < self.min_node.key:
                    self.min_node = node

    def _link(self, y, x):
        y.prev.next = y.next
        y.next.prev = y.prev
        y.next = y
        y.prev = y
        y.parent = x

        if x.child is None:
            x.child = y
        else:
            y.next = x.child.next
            y.prev = x.child
            x.child.next.prev = y
            x.child.next = y

        x.degree += 1
        y.mark = False

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        parent = node.parent

        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, node, parent):
        if parent.child == node:
            parent.child = node.next if node != node.next else None
        parent.degree -= 1
        node.parent = None
        node.mark = False
        self._merge_into_root_list(node)

    def _cascading_cut(self, node):
        parent = node.parent
        if parent:
            if node.mark:
                self._cut(node, parent)
                self._cascading_cut(parent)
            else:
                node.mark = True