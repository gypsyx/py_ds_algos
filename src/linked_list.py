
import logging
log = logging.getLogger(__name__)

class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value} : {nval}]"

class LinkedList:
    def __init__(self):
        self.begin: LinkedListNode = None
        self.last_node: LinkedListNode = None
        self._count = 0

    def push(self, value):
        """
        Appends the value to the end of the list.
        Time: O(1), constant time operation
        """
        node = LinkedListNode(value)

        if self.count == 0:
            self.begin = self.last_node = node
        else:
            current_last = self.last_node
            self.last_node = node
            current_last.next = self.last_node
        self._increase_count()


    def pop(self):
        """
        Removes the item at the end of the list and returns it.
        Time: O(1) + O(n) ~ O(n). Takes O(n) to find the previous node.
        """
        if self.count == 0:
            return None
        
        current_last = self.last_node
        previous = self._previous_node(self.last_node)
        self.last_node = previous
        if self.last_node:
            self.last_node.next = None
        else:
            self.begin = self.last_node
        self._decrease_count()
        return current_last.value
    
    def _previous_node(self, previous_to: LinkedListNode):
        """Returns the node before previous_to node."""
        
        current = self.begin
        while True:
            if current.next == previous_to:
                return current
            elif current.next is None:
                return None
            
            current = current.next

    def _increase_count(self) -> None:
        self.count += 1
    
    def _decrease_count(self) -> None:
        self.count  = (self.count - 1) if self.count > 0 else 0 

    @property
    def count(self) -> int:
        return self._count
    
    @count.setter
    def count(self, value) -> None:
        if value >= 0:
            self._count = value
        else:
            raise ValueError("count should be positive")
    
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
        while True:
            print(current.value, sep=" ", end=" ")
            if current.next is None:
                print("]")
                break

            current = current.next

    def get(self, index):
        """
        Returns the item at index
        Time: O(n), traverses the full list (in worst case)
        """
        if index >= self.count or index < 0:
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
        prev = None

        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                    current.next = None
                
                if current.value == self.last_node.value:
                    # removing last node so move last_node pointer to previous node
                    self.last_node = prev
                self._decrease_count()
                return index
            index += 1
            prev = current
            current = current.next
            
        return -1
        

    def shift(self, value):
        """
        Adds an item at the head of the linkedlist, making this the new first item.
        Time: O(1), constant time op.
        """
        new_node = LinkedListNode(value)
        self.begin, new_node.next = new_node, self.begin
        self._increase_count()

    def unshift(self):
        """
        Removes and returns the first item in the list.
        Time: O(1), constant time op. Compare this to pop which is O(n).
        """
        first = self.begin
        self.begin = first.next if first else None
        self._decrease_count()
        return first.value if first else None

    def first(self):
        """
        Returns the first item in the list.
        Time: O(1)
        """
        return self.begin.value if self.begin else None

    def last(self):
        """
        Returns the last item in the list.
        Time: O(1)
        """
        return self.last_node.value if self.last_node else None



        


