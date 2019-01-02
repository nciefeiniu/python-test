# -*- coding: utf-8 -*-


class Node():
    def __init__(self, value=None, nexts=None):
        self.next = nexts
        self.value = value


class LinkList():
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root:
            return False
        return True

    def length(self):
        if self.is_empty():
            return 0
        _l = 1
        _index = self.root
        while _index.next:
            _l += 1
            _index = _index.next
        return _l

    # 头插法
    def push_head(self, node):
        if self.is_empty():
            self.root = node
        else:
            node.next = self.root
            self.root = node

    # 尾插法
    def push_tail(self, node):
        if self.is_empty():
            self.root = node
        else:
            _index = self.root
            while _index.next:
                _index = _index.next
            _index.next = node

    # 在指定指针位置插入
    def insert(self, index, node):
        if index > self.length():
            raise RuntimeError('指针超过了链表长度。')
        if index < 0:
            raise RuntimeError('指针不能为负数。')
        if index == 0:
            self.push_head(node)
            return
        if index == self.length():
            self.push_tail(node)
            return
        _pre = self.root
        for i in xrange(index - 1):
            _pre = _pre.next
        node.next = _pre.next
        _pre.next = node

    # 在指定位置删除节点
    def remove(self, index):
        if self.is_empty():
            raise RuntimeError('链表为空，不能删除!')
        if index < 0:
            raise RuntimeError('指针不能小于零')
        if index == 0:
            self.root = self.root.next
            return
        _pre = self.root
        for i in xrange(index - 1):
            _pre = _pre.next
        _pre.next = _pre.next.next

    # 打印链表
    def print_link_list(self):
        if self.is_empty():
            print 'Link list is empty.'
        else:
            _index = self.root
            _text = ''
            while _index:
                # print _index.value
                _text += str(_index.value) + '->'
                _index = _index.next
            _text += 'NULL'
            print _text

    # 反转链表
    def rev_link_list(self):
        _index = self.root
        _pre = None
        while _index:
            _index.next, _pre, _index = _pre, _index, _index.next
        return _pre

    # 递归方式，从尾到头输出链表
    def recursion(self):
        _index = self.root
        self.do_rec(_index)

    def do_rec(self, root):
        _index = root
        if _index.next:
            _index = _index.next
            self.do_rec(_index)

        print _index.value


if __name__ == '__main__':
    l = LinkList()
    print l.is_empty()
    node = Node(nexts=None, value='2')
    l.push_head(node)
    print l.is_empty()
    l.print_link_list()
    print l.length()
    node = Node(value='5')
    l.push_head(node)
    l.print_link_list()
    print l.length()
    l.push_tail(Node(10))
    l.print_link_list()

    l.insert(2, Node(value=12))
    l.print_link_list()

    l.insert(4, Node(value=12))
    l.print_link_list()
    #
    # root = l.rev_link_list()
    # while root:
    #     print root.value
    #     root = root.next

    print '========递归============='
    l.print_link_list()
    l.recursion()