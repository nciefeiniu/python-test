# -*- coding: utf-8 -*-


def get_deep(root):
    '''
    求二叉树的最大深度，递归
    :param root:
    :return: int
    '''
    _left, _right = 0, 0
    if root.left:
        _left = get_deep(root.left)
    if root.right:
        _right = get_deep(root.right)
    return max(_left, _right) + 1

