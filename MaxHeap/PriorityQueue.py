from MaxHeap.MaxHeap import MaxHeap


class PriorityQueue:

    def __init__(self):
        self._maxHeap = MaxHeap()

    def get_size(self):
        return self._maxHeap.size()

    def is_empty(self):
        return self._maxHeap.is_empty()

    def get_front(self):
        return self._maxHeap.find_max()

    def enqueue(self, e):
        self._maxHeap.add(e)

    def dequeue(self):
        return self._maxHeap.extract_max()
