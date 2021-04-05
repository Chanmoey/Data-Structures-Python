RED = True
BLACK = False


class RBTree:

    class _Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            # new node must be a leaf node and merge to the current leaf node
            # so it is red by default
            self.color = RED

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _is_red(self, node):
        if not node:
            return BLACK
        return node.color

    #       node                            x
    #       /  \          左旋转            / \
    #      T1   x     ------------>      node T3
    #          / \                       /  \
    #         T2  T3                    T1   T2
    def _left_rotate(self, node):

        x = node.right

        # 左旋转
        node.right = x.left
        x.left = node

        x.color = node.color
        node.color = RED

        return x

    #       node                            x
    #       /  \          右旋转            / \
    #      x    T2    ------------->      y node
    #     / \                               /  \
    #    y  T1                             T1   T2
    def _right_rotate(self, node):

        x = node.left

        # 又旋转
        node.left = x.right
        x.right = node

        x.color = node.color
        node.color = RED

        return x

    # 颜色翻转
    def _flip_colors(self, node):

        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    # 向红黑树中添加新的元素(key value)
    def add(self, key, value):

        self._root = self._add(self._root, key, value)
        self._root.color = BLACK  # 最终根节点喂黑色节点

    # 向以node为根的红黑树中插入元素(key, value)， 递归算法
    # 返回插入新节点后红黑树的根
    def _add(self, node, key, value):

        if not node:
            self._size += 1
            return self._Node(key, value) # 默认插入红色节点

        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:  # key == node.key
            node.value = value

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._left_rotate(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._right_rotate(node)

        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _get_node(self, node, key):

        if not node:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self._get_node(node.left, key)
        else:  # key > node.key
            return self._get_node(node.right, key)

    def contains(self, key):
        return self._get_node(self._root, key) is not None

    def get(self, key):
        node = self._get_node(self._root, key)
        return node.value if node is not None else None

    def set(self, key, new_value):
        node = self._get_node(self._root, key)
        if not node:
            raise ValueError("Key '{}' doesn't exist!".format(str(key)))

        node.value = new_value

    # 寻找二分搜索树的最小元素
    def minimum(self):
        if self._size == 0:
            raise ValueError("BST is empty!")

        return self._minimum(self._root).e

    # 返回以node为根的二分搜索树的最小值所在的节点
    def _minimum(self, node):
        if not node.left:
            return node

        return self._minimum(node.left)

    # 删除掉以node为根的二分搜索树中的最小节点
    # 返回删除节点后新的二分搜索树的根
    def _remove_min(self, node):

        if not node.left:
            right_node = node.right
            node.right = None
            self._size -=1
            return right_node

        node.left = self._remove_min(node.left)
        return node

    # 从二分搜索树中删除元素为e的节点
    def remove(self, key):

        node = self._get_node(self._root, key)
        if node:
            self._root = self._remove(self._root, key)
            return node.value

        return None

    # 删除掉以node为根的二分搜索树中键为key的节点，递归算法
    # 返回删除节点后新的二分搜索树的根
    def _remove(self, node, key):

        if not node:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node
        else:  # key == node.key

            # 删除节点左子树为空的情况
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node

            # 删除节点左子树为空的情况
            if not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node

            # 带删除节点左右子树均不为空的情况
            # 找到比待删除节点大的最小节点， 既待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left

            node.left = node.right = None

            return successor