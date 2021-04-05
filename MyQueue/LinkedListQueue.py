class LinkedListQueue:

    class _Node:

        def __init__(self, e=None, node_next=None):
            self.e = e
            self.next = node_next

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):

        if not self._tail:
            self._tail = self._Node(e)
            self._head = self._tail

        else:
            self._tail.next = self._Node(e)
            self._tail = self._tail.next

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty Queue.")

        ret_node = self._head
        self._head = self._head.next
        ret_node.next = None

        if not self._head:
            self._tail = None

        self._size -= 1
        return ret_node.e

    def get_front(self):

        if self.is_empty():
            raise ValueError("Queue is empty")

        return self._head.e

    def __str__(self):
        res = ["Queue: front "]

        cur = self._head

        while cur:
            res.append(str(cur.e) + "->")
            cur = cur.next

        res.append("Null tail")
        res = ''.join(res)
        return res


if __name__ == "__main__":
    queue = LinkedListQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)

        if i % 3 == 2:
            queue.dequeue()
            print(queue)
