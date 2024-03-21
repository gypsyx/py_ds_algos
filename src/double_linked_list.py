
class DoubleLinkedListNode:
    def __init__(self, value, prev = None, nxt = None):
        self.prev = prev
        self.next = nxt
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self._count = 0

    def _invariant(self):
        # if list has one item begin=end=item
        # if list has >= 1 item, begin.prev = None, end.next = None
        # if list has 2 items, begin.next = end
        # if list has zero items beging = end = None
        # count should never be less than zero
        def count():
            """Internal count that traverses the list fully. The one exposed via public interface is more efficient but we need this for checks"""
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
            # assert self.end  == None
        elif count == 1:
            assert self.begin is self.end
            assert self.begin.prev is None
            assert self.begin.next is None
            # assert self.end.prev is None
            # assert self.end.next is None
        elif count == 2:
            assert self.begin.prev is None
            assert self.begin.next is self.end
            assert self.end.prev is self.begin
            assert self.end.next is None
        else:
            assert self.begin.prev is None
            assert self.begin.next is not None
            assert self.end.prev is not None
            assert self.end.next is None

    
    def push(self, value):
        node = DoubleLinkedListNode(value)

        if self.count() == 0:
            self.begin = self.end = node
        else:
            current_last = self.end
            self.end = node
            current_last.next = self.end
            self.end.prev = current_last
        self._count += 1
        self._invariant()

    def pop(self):
        if self.count() == 0:
            return
        
        item = self.end
        prev = item.prev
        if prev:
            self.end = prev
            self.end.prev = prev.prev
            prev.next = None
        else:
            self.end = None
            self.begin = None
        
        self._count -= 1
        self._invariant()
        return item.value

    def count(self):
        return self._count

    def get(self, index):
        """
        Returns the item at index
        Time: O(n), traverses the full list (in worst case)
        """
        self._invariant()
        if index >= self.count() or index < 0:
            raise IndexError("index out of range")
        
        counter = 0
        current = self.begin
        
        while current:
            if counter == index:
                return current.value
            counter += 1
            current = current.next
    

    def remove(self, value):
        """
        Removes first matching item in the list & returns its index. Returns -1 if item not found.
        Time: O(n) worst case, traverses the entire list
        """
        index = 0
        current = self.begin
        while current:
            if current.value == value:
                self.detach_node(current)
                return index
            index += 1
            current = current.next
        return -1

    def detach_node(self, node):
        """Detaches the node from the list"""
        prev = node.prev
        nxt = node.next

        if prev:
            prev.next = nxt
        else:
            # node being detached is the head
            self.begin = nxt

        if nxt:
            nxt.prev = prev
        else:
            # node being detached is the tail
            self.end = prev

        self._count -= 1

    def shift(self, value):
        """Adds a item to the head of the list, shifting every node by 1 position"""

        if self.count() == 0:
            self.push(value)
            return
        
        current_begin = self.begin
        new_node = DoubleLinkedListNode(value)
        self.begin = new_node
        self.begin.next = current_begin

        if self.count() == 1:
            self.end = current_begin
            self.end.prev = self.begin
        
        self._count += 1
        self._invariant()


    def unshift(self):
        """Remove and return the head of the list."""
        if self.count() == 0:
            return
        
        first = self.begin
        if self.count() == 1:
            self.begin = self.end = None
        else:
            self.begin = first.next
            self.begin.prev = None
            if self.begin.next is None:
                self.end.prev = None

        self._count -= 1
        self._invariant()
        return first.value

    def first(self):
        """Returns the first item in the list."""
        return self.begin.value if self.begin else None

    def last(self):
        """Returns the last item in the list"""
        return self.end.value if self.end else None

    def dump(self) -> None:
        """
        Tool for debugging.
        Time: O(n), traverses the entire list
        """
        if self.begin is None:
            print("[ ]")
            return
        
        current = self.begin

        print("[ ", sep=" ", end= " ")
        while current:
            print(current.value, sep=" ", end=" ")
            if current.next is None:
                print("]")
                break
            current = current.next