from src.binary_search_tree import BSTree

def test_set_balanced_tree():
    tree = BSTree()
    tree.set(50, "fifty")
    tree.set(30, "thirty")
    tree.set(20, "twenty")
    tree.set(40, "forty")
    tree.set(70, "seventy")
    tree.set(60, "sixty")
    tree.set(80, "eighty")

    out = tree.list_in_order() 
    assert out == [20, 30, 40, 50, 60, 70, 80]

def test_set_unbalanced_tree():
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(30, "thirty")
    tree.set(40, "forty")
    tree.set(50, "fifty")
    tree.set(60, "sixty")
    tree.set(70, "seventy")
    tree.set(80, "eighty")
    
    out = tree.list_in_order() 
    assert out == [20, 30, 40, 50, 60, 70, 80]

def test_get_balanced_tree():
    tree = BSTree()
    elements = [
        (50, "fifty"), 
        (30, "thirty"),
        (20, "twenty"),
        (40, "forty"),
        (70, "seventy"),
        (60, "sixty"),
        (80, "eighty"),
    ]

    for element in elements:
        key, value = element
        tree.set(key, value)

    out = tree.list_in_order() 
    assert out == [20, 30, 40, 50, 60, 70, 80]
    
    for element in elements:
        key, value = element
        assert tree.get(key) == value

def test_delete_no_children_no_parent():
    tree = BSTree()
    tree.set(10, "ten")
    tree.delete(10)
    assert tree.list_in_order() == []

def test_delete_no_children_has_parent():
    # node to delete is right node of parent
    tree = BSTree()
    tree.set(10, "ten")
    tree.set(20, "twenty")
    tree.delete(20)
    assert tree.list_in_order() == [10]

    # node to delete is left node of parent
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(10, "ten")
    tree.delete(10)
    assert tree.list_in_order() == [20]

def test_delete_one_child_no_parent():
    # node to delete has left child only
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(10, "ten")
    tree.delete(20)
    assert tree.list_in_order() == [10]

    # node to delete has right child only
    tree = BSTree()
    tree.set(10, "ten")
    tree.set(20, "twenty")
    tree.delete(10)
    assert tree.list_in_order() == [20]


def test_delete_one_child_has_parent():
    """
        20
        /
       10
       /
      5
    """
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(10, "ten")
    tree.set(5, "ten")
    tree.delete(10)
    assert tree.list_in_order() == [5, 20]

def test_delete_one_child_has_parent_2():
    """
        20
        /
       10
         \
          15
    """
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(10, "ten")
    tree.set(15, "fifteen")
    tree.delete(10)
    assert tree.list_in_order() == [15, 20]


def test_delete_one_child_has_parent_3():
    """
        20
          \
           40
            \
             50
    """
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(40, "forty")
    tree.set(50, "fifty")
    tree.delete(40)
    assert tree.list_in_order() == [20, 50]


def test_delete_one_child_has_parent_4():
    """
        20
          \
           40
           /
          30 
    """
    tree = BSTree()
    tree.set(20, "twenty")
    tree.set(40, "forty")
    tree.set(30, "thirty")
    tree.delete(40)
    assert tree.list_in_order() == [20, 30]

    
