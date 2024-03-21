from src.queue import Queue

def test_put():
    colors = Queue()
    colors._invariant()
    assert colors.count() == 0

    colors.put("yellow")
    assert colors.count() == 1
    colors.put("orange")
    assert colors.count() == 2
    colors.put("red")
    assert colors.count() == 3
    colors._invariant()


def test_get():
    pass