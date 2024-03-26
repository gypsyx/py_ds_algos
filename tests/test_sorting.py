from src.sorting import (
    bubble_sort_list, 
    bubble_sort_list2, 
    bubble_sort_linked_list,
    is_linked_list_sorted
)
from src.double_linked_list import DoubleLinkedList
from src.linked_list import LinkedList
import pytest

def test_bubble_sort_list():
    assert bubble_sort_list([5, 4, 3]) == [3,4,5]
    assert bubble_sort_list2([5, 4, 3, 2, 1]) == [1,2,3,4,5]

@pytest.mark.parametrize("ListType", (DoubleLinkedList, LinkedList))
def test_bubble_sort_linked_list(ListType):
    dll = ListType()
    for i in range(5, 0, -1):
        dll.push(i)

    print()
    dll.dump()
    bubble_sort_linked_list(dll)
    dll.dump()
    assert is_linked_list_sorted(dll)






