from Array.Array import Array


class MaxHeap:

    def __init__(self, arr=None, capacity=None):
        if isinstance(arr, Array):
            self._data = arr
            for i in range(self._parent(arr.get_size() - 1), -1, -1):
                self._sift_down(i)
            return
        if not capacity:
            self._data = Array()
        else:
            self._data = Array(capacity=capacity)

    # 返回堆中的元素个数
    def size(self):
        return self._data.get_size()

    # 返回一个布尔值，表示堆中是否为空
    def is_empty(self):
        return self._data.is_empty()

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    def _parent(self, index):
        if index == 0:
            raise ValueError('index-0 doesn\'t have parent.')
        return (index - 1) // 2

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    def _left_child(self, index):
        return index * 2 + 1

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    def _right_child(self, index):
        return index * 2 + 2

    # 向堆中添加元素
    def add(self, e):
        self._data.add_last(e)
        self._sift_up(self._data.get_size() - 1)

    def _sift_up(self, k):

        while k > 0 and self._data.get(self._parent(k)) < self._data.get(k):
            self._data.swap(k, self._parent(k))
            k = self._parent(k)

    # 看堆中得最大元素
    def find_max(self):
        if self._data.get_size() == 0:
            raise ValueError('Can not find_max when heap is empty.')
        return self._data.get(0)

    # 取出堆中最大元素
    def extract_max(self):

        ret = self.find_max()

        self._data.swap(0, self._data.get_size() - 1)
        self._data.remove_last()
        self._sift_down(0)

        return ret

    def _sift_down(self, k):

        while self._left_child(k) < self._data.get_size():

            j = self._left_child(k)
            if j + 1 < self._data.get_size() and self._data.get(j + 1) > self._data.get(j):
                j = self._right_child(k)
            # self._data[j] 是 left_child 和 right_child 中的最大值

            if self._data.get(k) >= self._data.get(j):
                break

            self._data.swap(k, j)
            k = j

    # 取出堆中的最大元素，并且替换成元素e
    def replace(self, e):

        ret = self.find_max()
        self._data.set(0, e)
        self._sift_down(0)
        return ret
