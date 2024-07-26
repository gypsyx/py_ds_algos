from src.versioned_maps.versioned_maps import SimpleVersionedMap
import pytest

@pytest.fixture(scope='function')
def svm():
    svmap = SimpleVersionedMap()
    svmap.set('name', 'dinesh1.0') # version 0
    svmap.set('age', 43) # version 1
    svmap.set('fav_colors', ['yellow', 'red', 'blue']) # version 2
    return svmap

def test_set_get_basic(svm):
    svm.show_versions()

    assert svm.get('name') == 'dinesh1.0'
    assert svm.get('age', 1) == 43
    assert svm.get('fav_colors', 2) == ['yellow', 'red', 'blue']

    # change name
    # breakpoint()
    svm.set('name', 'dinesh2.0')
    assert svm.get('name', 3) == 'dinesh2.0'
    assert svm.get('name', 2) == 'dinesh1.0'
    assert svm.get('name', 1) == 'dinesh1.0'
    assert svm.get('name') == 'dinesh1.0'

def test_delete(svm):
    svm.delete('age', 2)
    assert svm.get('age', 1) == 43
    
    with pytest.raises(KeyError):
        svm.get('age', 0)
    
    with pytest.raises(KeyError):
        svm.get('age', 2) # we deleted this above

    

def test_revert(svm):
    svm.revert_to_version(0)
    assert len(svm.versions) == 1