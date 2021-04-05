"""
实现一个属于我们自己的数组类
"""


class Array:

    # 构造函数，传入数组的容量capacity，默认为10
    def __init__(self, arr=None, capacity=10):

        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
            return

        self._data = [None] * capacity
        self._size = 0

    # 获取数组中的元素个数
    def get_size(self):
        return self._size

    # 获取数组的容量
    def get_capacity(self):
        return len(self._data)

    # 返回数组是否为空
    def is_empty(self):
        return self._size == 0

    # 向所有元素后添加一个新元素
    def add_last(self, e):
        self.add(self._size, e)

    # 在数组的第一个位置添加一个元素
    def add_first(self, e):
        self.add(0, e)

    # 在第index个位置插入一个新元素e
    def add(self, index, e):

        if index < 0 or index > self._size:
            raise ValueError("Add failed. Require index >= 0 and index <= size.")

        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        self._data[index] = e
        self._size += 1

    # 获取index索引位置的元素
    def get(self, index):

        if index < 0 or index >= self._size:
            raise ValueError("Get failed. Index is illegal.")

        return self._data[index]

    def get_last(self):
        return self.get(self._size - 1)

    def get_first(self):
        return self.get(0)

    # 修改index索引位置的元素为e
    def set(self, index, e):

        if index < 0 or index >= self._size:
            raise ValueError("Set failed. Index is illegal.")

        self._data[index] = e

    # 查找数组中是否有元素e
    def contains(self, e):

        for i in range(self._size):
            if self._data[i] == e:
                return True

        return False

    # 查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    def find(self, e):

        for i in range(self._size):
            if self._data[i] == e:
                return i

        return -1

        # 查找数组中所有元素e所在的索引，如果不存在元素e，则返回-1
    def findall(self, e):
        index = []

        for i in range(self._size):
            if self._data[i] == e:
                index.append(i)

        if index:
            return index

        return -1

    # 从数组中删除index位置的元素，返回删除的元素
    def remove(self, index):

        if index < 0 or index >= self._size:
            raise ValueError("Remove failed. Index is illegal.")

        ret = self._data[index]

        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]

        self._size -= 1
        self._data[self._size] = None

        # 如果数组的空间为1，len(self._data) // 2 就会为1，不合理
        if self._size == len(self._data) // 4 and len(self._data) // 2 != 2:
            self._resize(len(self._data) // 2)

        return ret

    # 从数组中删除第一个元素，返回删除的元素
    def remove_first(self):
        return self.remove(0)

    # 从数组中删除最后一个元素，返回删除的元素
    def remove_last(self):
        return self.remove(self._size - 1)

    # 从数组中删除元素e
    def remove_element(self, e):
        index = self.find(e)

        if index != -1:
            self.remove(index)

    # 从数组中删除所有元素e
    def remove_all_element(self, e):
        index = self.findall(e)

        if index:

            for i in range(len(index)):
                removed = index[i]
                self.remove(removed)
                index = [i - 1 for i in index]

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data

    def swap(self, i, j):

        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise ValueError('Index is illegal.')

        self._data[i], self._data[j] = self._data[j], self._data[i]

    # 让我们的数组可以作为字符串显示出来
    def __str__(self):
        res = "Array: size = {}, capacity = {}\n{}".format(self._size, len(self._data), self._data[: self._size])
        return res

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    arr = Array(capacity=10)
    for i in range(10):
        arr.add_last(i)
    print(arr)

    arr.add(1, 100)
    print(arr)

    arr.add_first(0)
    print(arr)

    arr.remove(2)
    print(arr)

    arr.remove_element(4)
    print(arr)

    arr.remove_last()
    print(arr)

    arr.remove_all_element(e=0)
    print(arr)
