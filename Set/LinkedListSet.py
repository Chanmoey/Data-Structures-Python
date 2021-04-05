from LinkedList.LinkedList import LinkedList


class LinkedListSet:

    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def contains(self, e):
        return self._list.contains(e)

    def add(self, e):
        if not self._list.contains(e):
            self._list.add_first(e)

    def remove(self, e):
        self._list.remove_element(e)


if __name__ == "__main__":
    my_set = LinkedListSet()
    my_set.add(5)