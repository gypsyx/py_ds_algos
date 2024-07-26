from src.versioned_maps.persistent_hash_map import PMap

def test_pmap():
    m = PMap()
    m.set('c', 1)
    assert len(m.versions) == 1

    m.set('b', 1)
    assert len(m.versions) == 2

    assert id(m.versions[0]) != id(m.versions[1])

    m.set('d', 1)
    assert len(m.versions) == 3
    assert len({id(m.versions[0]), id(m.versions[1]), id(m.versions[2])}) == 3

    m.set('a', 1)
    assert len(m.versions) == 4
    assert id(m._get_node(m.versions[2], 'd')) == id(m._get_node(m.versions[3], 'd'))