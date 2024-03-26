from src.binary_search import DoubleLinkedList, binary_search
from time import perf_counter


def test_search_list():
    items = [1, 2, 3, 4, 5 ,6]
    assert binary_search(items, 1) == 0
    assert binary_search(items, 6) == 5
    assert binary_search(items, 3) == 2
    assert binary_search(items, -5) == -1
    assert binary_search(items, 8) == -1


def test_search_dll():
    dll = DoubleLinkedList()
    for item in [1, 2, 3, 4, 5, 6]:
        dll.push(item)
    
    assert binary_search(dll, 1) == 0
    assert binary_search(dll, 6) == 5
    assert binary_search(dll, 3) == 2
    assert binary_search(dll, -5) == -1
    assert binary_search(dll, 8) == -1


# TODO: write a performance test for both search_list and search_dll
def test_dll_binary_search_performance(benchmark):
    items = [i for i in range(1, 1_000_001)]
    dll = DoubleLinkedList()
    for item in items:
        dll.push(item)
    
    benchmark(binary_search, dll, 1)

def test_list_binary_search_performance(benchmark):
    items = [i for i in range(1, 1_000_001)]
    
    index = benchmark(binary_search, items, 1)
    assert index == 0


def test_performance():
    items = [i for i in range(1, 10001)]
    dll = DoubleLinkedList()
    for item in items:
        dll.push(item)
    
    assert binary_search(dll, 1) == 0


if __name__ == '__main__':
    """
    This section is to run this module under cProfile
    """
    test_performance()

    