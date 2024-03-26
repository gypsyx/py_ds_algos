from copy import deepcopy
from src.double_linked_list import DoubleLinkedList

# NOTE: Leaving this here to demo that this isn't bubble sort.
def bubble_sort_list2(items):
    output = deepcopy(items)
    print(output)

    for i, vi in enumerate(items):
        for j, vj  in enumerate(items):
            if vi == vj:
                continue

            if vi > vj:
                #swap
                output[i], output[j] = output[j], output[i]
                print(output)
    return output

def bubble_sort_list(items):
    print()
    for i in range(len(items)):
        for j in range(0, len(items) - 1):
            if  items[j] > items[j+1]:
                #swap
                items[j], items[j+1] = items[j+1], items[j]
                print(items)
    return items

def bubble_sort_linked_list(link):
    outer_node = link.begin

    while outer_node:
        node = link.begin

        while node and node.next:
            if node.value > node.next.value:
                node.value, node.next.value = node.next.value, node.value
            node = node.next
        outer_node = outer_node.next


def is_linked_list_sorted(link):
    node = link.begin

    while node and node.next:
        if node.value > node.next.value:
            return False
        node = node.next
    return True

