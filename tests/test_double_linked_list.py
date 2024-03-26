import pytest
from src.double_linked_list import DoubleLinkedList

@pytest.fixture(autouse=True)
def colors():
    linked_list = DoubleLinkedList()
    yield linked_list
    linked_list.invariant()

def test_push(colors):
    colors.push("yellow")
    assert colors.count() == 1
    colors.dump()
    colors.push("orange")
    assert colors.count() == 2

    colors.push("red")
    assert colors.count() == 3
    colors.push("blue")
    assert colors.count() == 4
    colors.dump()
    print(f"INFO: test complete")


def test_pop_1_item(colors):
    # push/pop 1 item
    colors.push("yellow")
    assert colors.count() == 1
    assert colors.pop() == "yellow"
    assert colors.count() == 0
    
    # push/pop 2 items
    colors.push("yellow")
    colors.push("orange")
    assert colors.count() == 2
    assert colors.pop() == "orange"
    assert colors.count() == 1
    assert colors.pop() == "yellow"
    assert colors.count() == 0


def test_pop_2_items(colors):
    colors.push("yellow")
    colors.push("orange")
    assert colors.count() == 2
    assert colors.pop() == "orange"
    assert colors.count() == 1
    assert colors.pop() == "yellow"
    assert colors.count() == 0


def test_pop_3_items(colors):
    colors.push("yellow")
    colors.push("orange")
    colors.push("red")
    assert colors.count() == 3
    assert colors.pop() == "red"
    assert colors.count() == 2
    assert colors.pop() == "orange"
    assert colors.count() == 1
    assert colors.pop() == "yellow"
    assert colors.count() == 0


def test_get_after_push(colors):
    colors.push("yellow")
    assert colors.get(0) == "yellow"
    
    colors.push("orange")
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"
    
    colors.push("red")
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"
    assert colors.get(2) == "red"


def test_get_invalid_index(colors):
    with pytest.raises(IndexError):
        colors.get(-1)

    with pytest.raises(IndexError):
        colors.get(0)


def test_get_after_pop(colors):
    for color in ["yellow", "orange", "red"]:
        colors.push(color)

    assert colors.count() == 3
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
        colors.get(0)


def test_first(colors):
    colors.push("yellow")
    assert colors.first() == "yellow"
    colors.push("orange")
    assert colors.first() == "yellow"
    # colors.shift("red")
    # assert colors.first() == "red"


def test_shift_empty_list(colors):
    colors.shift("orange") # [orange]
    assert colors.get(0) == "orange"


def test_shift_non_empty_list(colors):
    colors.push("yellow") # [yellow]
    assert colors.get(0) == "yellow"
    
    colors.shift("orange") # [orange, yellow]
    assert colors.get(0) == "orange"
    assert colors.get(1) == "yellow"
    
    colors.shift("red") # [red, orange, yellow]
    assert colors.get(0) == "red"
    assert colors.get(1) == "orange"
    assert colors.get(2) == "yellow"


def test_unshift_empty_list(colors):
    assert colors.unshift() == None


def test_unshift_one_item_list(colors):
    colors.push("yellow")
    assert colors.unshift() == 'yellow'
    assert colors.count() == 0
    assert colors.first() == colors.last() == None


def test_unshift_two_item_list(colors):
    colors.push("yellow")
    colors.push("orange")

    assert colors.unshift() == "yellow"
    assert colors.count() == 1
    assert colors.first() == colors.last() == "orange"


def test_unshift_many_items_list(colors):
    colors.push("yellow")
    colors.push("orange")
    colors.push("red")

    assert colors.unshift() == "yellow"
    assert colors.count() == 2
    assert colors.unshift() == "orange"
    assert colors.count() == 1
    assert colors.unshift() == "red"
    assert colors.count() == 0
    assert colors.unshift() == None


def test_remove(colors):
    for color in ['yellow', 'orange', 'red', 'blue']:
        colors.push(color)

    assert colors.remove("red") == 2 # [yellow, orange, blue]
    assert colors.count() == 3
    assert colors.get(2) == "blue"
    assert colors.get(1) == "orange"
    assert colors.get(0) == "yellow"
    assert colors.first() == "yellow"
    assert colors.last() == "blue"

    assert colors.remove("blue") == 2 # [yellow, orange]
    assert colors.count() == 2
    assert colors.first() == "yellow"
    assert colors.last() == "orange"
    assert colors.get(0) == "yellow"
    assert colors.get(1) == "orange"

    assert colors.remove("doesnt_exist") == -1
