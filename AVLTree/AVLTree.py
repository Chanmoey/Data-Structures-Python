class AVLTree:

    class _Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_bst(self):
        keys = []
        self._in_order(self._root, keys)

        for i in range(1, len(keys)):
            if keys[i - 1] > keys[i]:
                return False
        return True

    def _in_order(self, node, keys):

        if not node:
            return

        self._in_order(node.left, keys)
        keys.append(node.key)
        self._in_order(node.right, keys)

    # 判断该二叉树是否是一棵平衡二叉树
    def is_balanced(self):
        return self._is_banlanced(self._root)

    # 判断以Node为根的二叉树是否是一棵平衡二叉树，递归算法
    def _is_balanced(self, node):

        if not node:
            return True

        balance_factor = self._get_balance_factor(node)
        if abs(balance_factor) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)

    def _get_height(self, node):
        if not node:
            return 0
        else:
            return node.height

    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        """
                对节点y进行向右旋转操作，返回旋转后的新的根节点x
                        y                                 x
                       / \                               / \
                      x   T4      向右旋转 (y)           z    y
                     / \        -------------->       / \   / \
                    z   T3                           T1 T2 T3  T4
                   / \
                  T1  T2
        """
        x = y.left
        t3 = x.right

        # 向右旋转
        x.right = y
        y.left = t3

        # 更新height值
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

    def _left_rotate(self, y):
        """
        对节点y进行向左旋转操作，返回旋转后的新的根节点x
             y                                 x
            / \                               / \
           T1  x      向右旋转 (y)            y    z
              / \     -------------->      / \   / \
             T2  z                        T1 T2 T3  T4
                / \
               T1 T2
        """

        x = y.right
        t2 = x.left

        # 向左旋转
        x.left = y
        y.right = t2

        # 更新height
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

    # 向二分搜索树中添加新的元素(key value)
    def add(self, key, value):

        self._root = self._add(self._root, key, value)

    # 向以node为根的二分搜索树中插入元素(key, value)， 递归算法
    # 返回插入新节点后二分搜索树的根
    def _add(self, node, key, value):

        if not node:
            self._size += 1
            return self._Node(key, value)

        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:  # key == node.key
            node.value = value

        # 更新height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 计算平衡因子
        balance_factor = self._get_balance_factor(node)
        # if balance_factor > 1:
        #     print("unbalance : {}".format(balance_factor))

        # 平衡维护
        # LL
        if balance_factor > 1 and self._get_balance_factor(node.left) >= 0:
            return self._right_rotate(node)

        # RR
        if balance_factor < -1 and self._get_balance_factor(node.right) <= 0:
            return self._left_rotate(node)

        # LR
        if balance_factor > 1 and self._get_balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # RL
        if balance_factor < -1 and self._get_balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
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
            ret_node = node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            ret_node = node
        else:  # key == node.key

            # 删除节点左子树为空的情况
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                ret_node = right_node

            # 删除节点右子树为空的情况
            elif not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                ret_node = left_node

            # 带删除节点左右子树均不为空的情况
            # 找到比待删除节点大的最小节点， 既待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            else:
                successor = self._minimum(node.right)
                successor.right = self._remove(node.right, successor.key)
                successor.left = node.left

                node.left = node.right = None

                ret_node = successor

        if not ret_node:
            return

        # 更新height
        ret_node.height = 1 + max(self._get_height(ret_node.left), self._get_height(ret_node.right))

        # 计算平衡因子
        balance_factor = self._get_balance_factor(ret_node)
        # if balance_factor > 1:
        #     print("unbalance : {}".format(balance_factor))

        # 平衡维护
        # LL
        if balance_factor > 1 and self._get_balance_factor(ret_node.left) >= 0:
            return self._right_rotate(ret_node)

        # RR
        if balance_factor < -1 and self._get_balance_factor(ret_node.right) <= 0:
            return self._left_rotate(ret_node)

        # LR
        if balance_factor > 1 and self._get_balance_factor(ret_node.left) < 0:
            ret_node.left = self._left_rotate(ret_node.left)
            return self._right_rotate(ret_node)

        # RL
        if balance_factor < -1 and self._get_balance_factor(ret_node.right) > 0:
            ret_node.right = self._right_rotate(ret_node.right)
            return self._left_rotate(ret_node)
        return ret_node
