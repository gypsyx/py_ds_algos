

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
        """Adds a new value to the top of the stack"""
        
        if self._top is None:
            self._top = StackNode(value, None)
        else:
            current_top = self._top
            self._top = StackNode(value, current_top)
        self._count += 1


    def pop(self):
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
        pass