from src.stack import Stack
import pytest

def test_push():
    colors = Stack()
    colors.push("yellow")
    assert colors.count() == 1
    colors.push("orange")
    assert colors.count() == 2

    colors.push("red")
    assert colors.count() == 3
    colors.push("blue")
    assert colors.count() == 4

def test_top():
    colors = Stack()
    colors.push("yellow")
    assert colors.top() == "yellow"
    colors.push("orange")
    assert colors.top() == "orange"

    colors.push("red")
    assert colors.top() == "red"
    colors.push("blue")
    assert colors.top() == "blue"

def test_pop():
    colors = Stack()
    colors.dump()
    colors.push("yellow")
    colors.push("orange")
    colors.push("red")
    colors.dump()
    assert colors.pop() == "red"
    assert colors.count() == 2
    assert colors.top() == "orange"
    colors.dump()

    assert colors.pop() == "orange"
    assert colors.count() == 1
    assert colors.top() == "yellow"
    colors.dump()

    assert colors.pop() == "yellow"
    assert colors.count() == 0
    assert colors.top() is None
    colors.dump()
    
    with pytest.raises(IndexError):
        colors.pop()
        assert colors.count() == 0
        assert colors.top() is None

