class LinkedListMap:

    class _Node:

        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next

        def __str__(self):
            res = '{} : {}'.format(self.key, self.value)
            return res

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _get_node(self, key):

        cur = self._dummy_head.next
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next

        return None

    def contains(self, key):
        return self._get_node(key) is not None

    def get(self, key):
        node = self._get_node(key)
        return node.value if node is not None else None

    def add(self, key, value):

        node = self._get_node(key)
        if not node:
            self._dummy_head.next = self._Node(key, value, self._dummy_head.next)
            self._size += 1
        else:
            node.value = value

    def set(self, key, new_value):

        node = self._get_node(key)
        if not node:
            raise ValueError("key {} doesn't exist".format(key))

        node.value = new_value

    def remove(self, key):

        prev = self._dummy_head
        while prev.next:
            if prev.next.key == key:
                break
            prev = prev.next

        if prev.next:
            del_node = prev.next
            prev.next = del_node.next
            del_node.next = None
            self._size -= 1
            return del_node.value

        return None


if __name__ == "__main__":
    my_dict =  LinkedListMap()
    my_dict.add("hello", "world")