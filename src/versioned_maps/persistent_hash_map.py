class PHMNode:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class PMap:
    def __init__(self):
        self.root = None
        self.versions = []

    def set(self, key, value):
        # create a root node if it doesn't exist
        # point the new version to this new root node
        # point root pointer to this new root node
        new_root = self._set(self.root, key, value)
        self.versions.append(new_root)
        self.root = new_root

    def _set(self, node, key, value):
        if node is None:
            return PHMNode(key, value, None, None)
        elif key < node.key:
            return PHMNode(node.key, node.value, self._set(node.left, key, value), node.right)
        elif key > node.key:
            return PHMNode(node.key, node.value, node.left, self._set(node.right, key, value))
        else:
            # create a new node with given key, value but pointing to the existing nodes
            return PHMNode(key, value, node.left, node.right)

    def get(self, key, version=0):
        if len(self.versions) < version < 0:
            raise ValueError(f"{version} is not valid")
        
        root = self.versions[version]
        return self._get(root, key)
    
    def _get(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        elif key == node.key:
            return node.value
        else:
            raise KeyError(f"key {key} doesn't exist")
        
    def _get_node(self, root, key, version=0):
        if key < root.key:
            return self._get_node(root.left, key)
        elif key > root.key:
            return self._get_node(root.right, key)
        elif key == root.key:
            return root


    def revert_to_version(self, version = 0):
        if len(self.versions) < version < 0:
            raise ValueError(f"{version} is not valid")
        
        new_root = self.versions[version]
        self.root = new_root
        # TODO - you can get rid of all versions above this if needed.


def test_phm():
    m = PMap()
    m.set('b', 1)
    assert len(m.versions) == 2

# test_phm()