import pytest
from src.linked_list import LinkedList
from src.double_linked_list import DoubleLinkedList

@pytest.mark.parametrize("ListClass", [LinkedList])
def test_push(ListClass):
    colors = ListClass()
    colors.push("yellow")
    assert colors.count == 1
    colors.push("orange")
    assert colors.count == 2

    colors.push("red")
    assert colors.count == 3
    colors.push("blue")
    assert colors.count == 4

def test_pop():
    colors = LinkedList()
    colors.push("yellow")
    colors.push("orange")
    colors.push("red")
    assert colors.pop() == "red"
    assert colors.count == 2
    assert colors.pop() == "orange"
    assert colors.count == 1

    assert colors.pop() == "yellow"
    assert colors.count == 0
    assert colors.pop() == None
    assert colors.count == 0

def test_get():
    colors = LinkedList()
    colors.push("yellow")
    assert colors.get(0) == "yellow"
    colors.push("orange")
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"
    colors.push("red")
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"
    assert colors.get(2) == "red"
    with pytest.raises(IndexError):
        colors.get(-1)
    
    assert colors.pop() == "red"
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"
    with pytest.raises(IndexError):
        colors.get(2)

    assert colors.pop() == "orange"
    assert colors.get(0) == "yellow"
    with pytest.raises(IndexError):
        colors.get(1)
    assert colors.pop() == "yellow"
    with pytest.raises(IndexError):
        colors.get(2)

def test_shift():
    colors = LinkedList()
    colors.push("yellow")
    assert colors.get(0) == "yellow"
    colors.shift("orange")
    assert colors.get(0) == "orange"
    assert colors.get(1) == "yellow"
    colors.shift("red")
    assert colors.get(0) == "red"
    assert colors.get(1) == "orange"
    assert colors.get(2) == "yellow"

def test_unshift():
    colors = LinkedList()
    colors.push("yellow")
    colors.push("orange")
    colors.push("red")
    assert colors.count == 3
    assert colors.unshift() == "yellow"
    assert colors.count == 2
    assert colors.unshift() == "orange"
    assert colors.count == 1
    assert colors.unshift() == "red"
    assert colors.count == 0
    assert colors.unshift() == None

def test_last():
    colors = LinkedList()
    colors.push("yellow")
    assert colors.last() == "yellow"
    colors.push("orange")
    assert colors.last() == "orange"
    colors.push("red")
    assert colors.last() == "red"

def test_first():
    colors = LinkedList()
    colors.push("yellow")
    assert colors.first() == "yellow"
    colors.push("orange")
    assert colors.first() == "yellow"
    colors.shift("red")
    assert colors.first() == "red"

def test_remove():
    colors = LinkedList()
    colors.push("yellow")
    colors.push("orange")
    colors.push("red")
    colors.push("blue")

    assert colors.remove("red") == 2
    assert colors.count == 3
    assert colors.get(2) == "blue"
    assert colors.get(1) == "orange"
    assert colors.get(0) == "yellow"
    assert colors.first() == "yellow"
    assert colors.last() == "blue"

    assert colors.remove("blue") == 2
    assert colors.last() == "orange"
    assert colors.first() == "yellow"
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"
    