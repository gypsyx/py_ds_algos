"""
Binary Search
"""
from typing import Any, Union
from src.double_linked_list import DoubleLinkedList

def search_list(items, find, start = None, end = None):
    if not items:
        return -1
    if start is None:
        start = 0
    if end is None:
        end = len(items) - 1
    
    mid = (end + start) // 2
    print(f"start: {start}, end: {end}, mid: {mid}")
    if (mid == 0 and items[mid] != find) or (mid == len(items)-1 and items[len(items)-1] != find):
        return -1 

    if items[mid] == find:
        print(f"FOUND index: {mid}, item: {find}, sorted_list[mid]: {items[mid]}")
        return mid
    elif items[mid] < find:
        return search_list(items, find, mid+1, end)
    elif items[mid] > find:
        return search_list(items, find, start, mid-1)


def search_dll(dll: DoubleLinkedList, find, start = None, end = None) -> int:
    if not dll:
        return -1
    if start is None:
        start = 0
    if end is None:
        end = dll.count() - 1
    
    mid = (start + end) // 2
    mid_item = dll.get(mid)

    # breaking condition if search is out of bounds on either end
    if (mid == 0 and mid_item != find) or (mid == dll.count() -1 and dll.last() != find):
        return -1

    if mid_item == find:
        return mid
    elif mid_item > find:
        return search_dll(dll, find, start, mid-1)
    else:
        return search_dll(dll, find, mid+1, end)



def binary_search(items: Union[list, DoubleLinkedList], find) -> int:
    """
    Unified interface to search a python list or our custom doublelinkedlist
    """
    if isinstance(items, list):
        return search_list(items, find)
    elif isinstance(items, DoubleLinkedList):
        return search_dll(items, find)
    else:
        raise NotImplementedError("unknown type for items")


    

    