# -*- coding: utf-8 -*-

import Queue


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value=value)
        if self.root is None:
            self.root = node
            return self.root
        q = Queue.Queue()
        q.put(self.root)
        _index = None
        while True:
            cur = q.get()
            if cur.left is None:
                cur.left = node
                return self.root
            if cur.right is None:
                cur.right = node
                return self.root
            q.put(cur.left)
            q.put(cur.right)

    # 先序遍历
    def p_traversal(self):
        if self.root is None:
            raise RuntimeError('Binary tree is empty!')
        _q = Queue.Queue()
        _q.put(self.root)
        print_str = ''
        while not _q.empty():
            cur = _q.get()
            print_str += str(cur.value)
            if cur.left:
                _q.put(cur.left)
            if cur.right:
                _q.put(cur.right)
        print print_str

    # 递归实现先序遍历
    def recursion_p(self, root):
        cur = root
        if cur:
            print cur.value
            if cur.left:
                self.recursion_p(cur.left)
            if cur.right:
                self.recursion_p(cur.right)

    # 递归实现中序遍历
    def recursion_af(self, root):
        cur = root
        if cur:
            self.recursion_p(cur.left)
            print cur.value
            self.recursion_p(cur.right)


if __name__ == '__main__':
    b = BinaryTree()
    b.add(1)
    b.add(2)
    b.add(3)
    b.add(4)
    b.add(5)
    b.add(6)
    b.add(7)
    # b.p_traversal()
    b.recursion_p(b.root)
    print '========================='
    b.recursion_af(b.root)
