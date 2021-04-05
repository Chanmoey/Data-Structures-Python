# from MyQueue import MyQueue


class LoopQueue:

    def __init__(self, capacity=10):
        self._data = [None] * (capacity + 1)
        self._front = 0
        self._tail = 0
        self._size = 0

    def get_capacity(self):
        return len(self._data) - 1

    def is_empty(self):
        return self._front == self._tail

    def get_size(self):
        return self._size

    def enqueue(self, e):

        if (self._tail + 1) % len(self._data) == self._front:
            self._resize(self.get_capacity() * 2)

        self._data[self._tail] = e
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def dequeue(self):

        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty Queue")

        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if self._size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:
            self._resize(self.get_capacity() // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")

    def _resize(self, new_capacity):
        new_data = [None] * (new_capacity + 1)

        for i in range(self._size):
            new_data[i] = self._data[(i + self._front) % len(self._data)]

        self._data = new_data
        self._front = 0
        self._tail = self._size

    def __str__(self):
        res = ["Queue: size = {} ", "capacity = {}\n", "front ["]
        i = self._front

        while i != self._tail:
            res.append(str(self._data[i]))

            if (i + 1) % len(self._data) != self._tail:
                res.append(", ")

            i = (i + 1) % len(self._data)

        res.append("] tail")

        res = ''.join(res)
        return res.format(self._size, self.get_capacity())

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    queue = LoopQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)

        if i % 3 == 2:
            queue.dequeue()
            print(queue)
