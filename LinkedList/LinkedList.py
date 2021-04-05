class LinkedList:

    class _Node:

        def __init__(self, e=None, node_next=None):
            self.e = e
            self.next = node_next

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    # 获取链表中元素个数
    def get_size(self):
        return self._size

    # 返回链表是否为空
    def is_empty(self):
        return self._size == 0

    # 在链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用: )
    def add(self, index, e):

        if index < 0 or index > self._size:
            raise ValueError("Add failed. Illegal index.")

        prev = self._dummy_head
        for i in range(index):
            prev = prev.next

        # node = self._Node(e)
        # node.next = prev.next
        # prev.next = node

        prev.next = self._Node(e, prev.next)
        self._size += 1

    # 在链表头添加新的元素e
    def add_first(self, e):
        self.add(0, e)

    # 在链表末尾添加新的元素
    def add_last(self, e):
        self.add(self._size, e)

    # 获得链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用: )
    def get(self, index):
        if index < 0 or index > self._size:
            raise ValueError("Get failed. Illegal index.")
        cur = self._dummy_head.next

        for i in range(index):
            cur = cur.next

        return cur.e

    # 获取链表的第一个元素
    def get_first(self):
        return self.get(0)

    # 获取链表的最后一个元素
    def get_last(self):
        return self.get(self._size - 1)

    # 修改链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用: )
    def set(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError("Set failed. Illegal index.")

        cur = self._dummy_head.next

        for i in range(index):
            cur = cur.next

        cur.e = e

    # 查找链表中是否有元素e
    def contains(self, e):

        cur = self._dummy_head

        while cur:
            if cur.e == e:
                return True
            cur = cur.next

        return False

    # 删除链表的index(0-based)位置的元素e
    # 在链表中不是一个常用的操作，练习用: )
    def remove(self, index):

        if index < 0 or index > self._size:
            raise ValueError("Remove failed. Illegal index.")

        prev = self._dummy_head
        for i in range(index):
            prev = prev.next

        ret_node = prev.next
        prev.next = ret_node.next
        ret_node.next = None
        self._size -= 1

        return ret_node.e

    # 从链表中删除第一个元素，返回删除的元素
    def remove_first(self):
        return self.remove(0)

    # 从链表中删除第一个元素，返回删除的元素
    def remove_last(self):
        return self.remove(self._size - 1)

    # 从链表中删除元素e
    def remove_element(self, e):

        prev = self._dummy_head
        while prev.next:
            if prev.next.e == e:
                break
            prev = prev.next

        if prev.next:
            del_node = prev.next
            prev.next = del_node.next
            del_node.next = None

    def __str__(self):

        res = []

        cur = self._dummy_head.next

        while cur:
            res.append(str(cur))
            cur = cur.next

        res.append("None")
        res = '->'.join(res)

        return res


if __name__ == "__main__":
    linkedList = LinkedList()
    for i in range(5):
        linkedList.add_first(i)
        print(linkedList)

    linkedList.add(2, 666)
    print(linkedList)

    linkedList.remove(2)
    print(linkedList)

    linkedList.remove_first()
    print(linkedList)

    linkedList.remove_last()
    print(linkedList)
