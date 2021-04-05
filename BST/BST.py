from LinkedList.LinkedList import LinkedList
from Stack.ArrayStack import ArrayStack


class BST:

    class _Node:

        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # 向二分搜索树中添加新的元素e
    def add(self, e):

        self._root = self._add(self._root, e)

    # 向以node为根的二分搜索树中插入元素E， 递归算法
    # 返回插入新节点后二分搜索树的根
    def _add(self, node, e):

        # if e == node.e:
        #     return
        # elif e < node.e and not node.left:
        #     node.left = self._Node(e)
        #     self._size += 1
        #     return
        # elif e > node.e and not node.right:
        #     node.right = self._Node(e)
        #     self._size += 1
        #     return

        if not node:
            self._size += 1
            return self._Node(e)

        if e < node.e:
            node.left = self._add(node.left, e)
        elif e > node.e:
            node.right = self._add(node.right, e)

        return node

    # 看二分搜索树中是否包含元素e
    def contains(self, e):
        return self._contains(self._root, e)

    # 看以node为根的二分搜索数中是否包含元素e，递归算法
    def _contains(self, node, e):

        if not node:
            return False

        if e == node.e:
            return True
        elif e < node.e:
            return self._contains(node.left, e)
        else:  # e > node.e
            return self._contains(node.right, e)

    # 二分搜索树的前序遍历
    def pre_order(self):
        self._pre_order(self._root)

    # 前序遍历以node为根的二分搜索树，递归算法
    def _pre_order(self, node):

        if not node:
            return
        print(node.e)
        self._pre_order(node.left)
        self._pre_order(node.right)

    # 二分搜索树的非递归前序遍历
    def pre_order_nr(self):
        stack = ArrayStack()
        stack.push(self._root)
        while not stack.is_empty():
            cur = stack.pop()
            print(cur.e)

            if cur.right:
                stack.push(cur.right)
            if cur.left:
                stack.push(cur.left)

    # 二分搜索树的中序遍历
    def in_order(self):
        self._in_order(self._root)

    # 中序遍历以node为根的二分搜索树，递归算法
    def _in_order(self, node):
        if not node:
            return

        self._in_order(node.left)
        print(node.e)
        self._in_order(node.right)

    # 二分搜索树的后序遍历
    def post_order(self):
        self._post_order(self._root)

    # 后续遍历以node为根的二分搜索树，递归算法
    def _post_order(self, node):
        if not node:
            return

        self._post_order(node.left)
        self._post_order(node.right)
        print(node.e)

    # 二分搜索树的层序遍历
    def level_order(self):
        q = LinkedList()
        q.add_last(self._root)
        while not q.is_empty():
            cur = q.remove(0)
            print(cur.e)

            if cur.left:
                q.add_last(cur.left)
            if cur.right:
                q.add_last(cur.right)

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

    # 寻找二分搜索树的最大元素
    def maximum(self):
        if self._size == 0:
            raise ValueError("BST is empty!")

        return self._maximum(self._root).e

    # 返回以node为根的二分搜索树的最大值所在的节点
    def _maximum(self, node):
        if not node.right:
            return node

        return self._maximum(node.right)

    # 从二分搜索树中删除最小值所在的节点，返回最小值
    def remove_min(self):
        ret = self.minimum()
        self._root = self._remove_min(self._root)
        return ret

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

    # 从二分搜索树中删除最大值所在的节点
    def remove_max(self):
        ret = self.maximum()
        self._root = self._remove_max(self._root)
        return ret

    # 删除掉以node为根的二分搜索树中的最大节点
    # 返回删除节点后新的二分搜索树的根
    def _remove_max(self, node):

        if not node.right:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node

        node.right = self._remove_max(node.right)
        return node

    # 从二分搜索树中删除元素为e的节点
    def remove(self, e):
       self._root = self._remove(self._root, e)

    # 删除掉以node为根的二分搜索树中值为e的节点，递归算法
    # 返回删除节点后新的二分搜索树的根
    def _remove(self, node, e):

        if not node:
            return None

        if e < node.e:
            node.left = self._remove(node.left, e)
            return node
        elif e > node.e:
            node.right = self._remove(node.right, e)
            return node
        else:  # e == node.e

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

    def __str__(self):
        res = []
        self._generate_bst_string(self._root, 0, res)
        res = ''.join(res)
        return res

    def _generate_bst_string(self, node, depth, res):

        if not node:
            res.append(self._generate_depth_string(depth) + "None\n")
            return

        res.append(self._generate_depth_string(depth) + str(node.e) + "\n")
        self._generate_bst_string(node.left, depth + 1, res)
        self._generate_bst_string(node.right, depth + 1, res)

    def _generate_depth_string(self, depth):
        res = []
        for i in range(depth):
            res.append("--")
        res = ''.join(res)
        return res


if __name__ == "__main__":
    bst = BST()
    nums = [5, 3, 6, 8, 4, 2]
    for i in nums:
        bst.add(i)
    # # bst.pre_order()
    # # print("\n")
    # # bst.in_order()
    # # print("\n")
    # # bst.post_order()
    # # bst.pre_order_nr()
    # bst.level_order()

    # from random import randint
    #
    # for i in range(1000):
    #     bst.add(randint(0, 10000))
    #
    # nums = []
    # while not bst.is_empty():
    #     nums.append(bst.remove_min())
    #
    # print(nums)
    # for i in range(1, len(nums)):
    #     if nums[i-1] > nums[i]:
    #         raise ValueError("Error")
    # print("removeMin test completed.")
    #
    # for i in range(1000):
    #     bst.add(randint(0, 10000))
    #
    # nums = []
    # while not bst.is_empty():
    #     nums.append(bst.remove_max())
    #
    # print(nums)
    # for i in range(1, len(nums)):
    #     if nums[i-1] < nums[i]:
    #         raise ValueError("Error")
    # print("removeMax test completed.")

    bst.add(100)
    bst.pre_order()
    print("\n")
    bst.remove(100)
    bst.pre_order()