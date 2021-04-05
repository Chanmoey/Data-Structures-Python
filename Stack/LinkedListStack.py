from LinkedList.LinkedList import LinkedList


class LinkedListStack:

    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, e):
        self._list.add_first(e)

    def pop(self):
        return self._list.remove_first()

    def peek(self):
        return self._list.get_first()

    def __str__(self):
        res = "Stack: top {}".format(self._list)
        return res


if __name__ == "__main__":

    stack = LinkedListStack()

    for i in range(5):
        stack.push(i)
        print(stack)

    stack.pop()
    print(stack)