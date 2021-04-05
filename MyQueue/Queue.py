class Queue:
    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def enqueue(self, e):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def get_front(self):
        raise NotImplementedError
