from Array.Array import Array


class ArrayQueue:
    def __init__(self, capacity=10):
        self._array = Array(capacity=capacity)

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self._array.get_capacity()

    def enqueue(self, e):
        self._array.add_last(e)

    def dequeue(self):
        return self._array.remove_first()

    def get_front(self):
        return self._array.get_first()

    def __str__(self):
        res = ["Queue: ", "front ["]
        for i in range(self._array.get_size()):
            res.append(str(self._array.get(i)))
            if i != self._array.get_size() - 1:
                res.append(", ")

        res.append("] tail")

        res = ''.join(res)
        return res

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    queue = ArrayQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)

        if i % 3 == 2:
            queue.dequeue()
            print(queue)