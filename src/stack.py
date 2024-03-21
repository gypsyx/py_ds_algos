"""
A LIFO (Last In First Out) Stack data structure.

As you can see below all stack operations are constant time, so
it is a really fast datastructure.
"""

class StackNode:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        next_val = self.next and self.next.value or None
        return f"[{self.value} : {next_val}]"


class Stack:
    def __init__(self):
        self._top = None
        self._count = 0

    def push(self, value):
        """
        Adds a new value to the top of the stack
        
        Time: O(1), constant time. Fast
        """
        
        if self._top is None:
            self._top = StackNode(value, None)
        else:
            current_top = self._top
            self._top = StackNode(value, current_top)
        self._count += 1


    def pop(self):
        """
        Pops the last added item.

        Time: O(1), constant time. Fast.
        """
        if self.count() == 0:
            raise IndexError("can't pop an empty stack")
        
        current_top = self._top
        self._top = current_top.next
        self._count -= 1
        return current_top.value

    def top(self):
        return self._top.value if self._top else None

    def count(self):
        return self._count

    def dump(self):
        """
        Tool for debugging
        
        Time: O(n).This is only for debugging.
        """
        if self.count() == 0:
            print("[ ]")
            return
        
        current = self._top
        print("[ ", sep=" ", end=" ")
        while current:
            print(current.value, sep=" ", end=" ")
            if not current.next:
                print("]")
                break

            current = current.next