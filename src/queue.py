
class QueueNode:
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt

    def __repr__(self):
        pass

class Queue:
    def __init__(self):
        self.begin = None
        self.end = None
        self._count = 0

    def _invariant(self):
        def count():
            count = 0
            current = self.begin

            while current:
                count += 1
                current = current.next
            return count
        count = count()
        assert count >= 0
        
        if count == 0:
            assert self.begin == self.end == None
        elif count == 1:
            assert self.begin is self.end
            assert self.begin.prev is None
            assert self.begin.next is None
            assert self.end.prev is None
            assert self.end.next is None
        elif count == 2:
            assert self.begin.prev is None
            assert self.begin.next is self.end
            assert self.end.prev is self.begin
            assert self.end.next is None
        else:
            assert self.begin.prev is None
            assert self.begin.next is not self.end
            assert self.end.next is None
            assert self.end.prev is not self.begin

    def get(self):
        """Removes and returns the oldest(head) item."""
        head = self.begin
        self.begin = self.begin.next
        self.begin.prev = None
        self._count -= 1
        return head

    def put(self, value):
        """Adds item to the end of the queue."""
        
        if self.count() == 0:
            self.begin = self.end = QueueNode(value, None, None)
        else:
            current_end = self.end
            self.end = QueueNode(value, current_end, None)
            current_end.next = self.end
        self._count += 1


    def count(self):
        return self._count
    
    # def empty(self):
    #     return (self._count == 0)