from Array.Array import Array


class ArrayStack:

    def __init__(self, capacity=10):
        self._array = Array(capacity=capacity)

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self._array.get_capacity()

    def push(self, e):
        self._array.add_last(e)

    def pop(self):
        return self._array.remove_last()

    def peek(self):
        return self._array.get_last()

    def __str__(self):
        res = ['Stack: ', '[']
        for i in range(self._array.get_size()):
            res.append(str(self._array.get(i)))
            if i != self._array.get_size() - 1:
                res.append(", ")

        res.append("] top")

        res = ''.join(res)
        return res

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":

    stack = ArrayStack()

    for i in range(5):
        stack.push(i)
        print(stack)

    stack.pop()
    print(stack)
