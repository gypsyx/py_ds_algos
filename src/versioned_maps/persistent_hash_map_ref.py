class PersistentNode:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node(key={self.key}, value={self.value})'

class PersistentHashMap:
    def __init__(self):
        self.current_root = None
        self.version_history = []  # Store roots of all versions

    def _set(self, node, key, value):
        if node is None:
            return PersistentNode(key, value)
        if key < node.key:
            return PersistentNode(node.key, node.value, self._set(node.left, key, value), node.right)
        elif key > node.key:
            return PersistentNode(node.key, node.value, node.left, self._set(node.right, key, value))
        else:
            return PersistentNode(key, value, node.left, node.right)

    def set(self, key, value):
        new_root = self._set(self.current_root, key, value)
        print(f"current_root {id(self.current_root)} new_root {id(new_root)}")
        self.version_history.append(new_root)
        self.current_root = new_root

    def _get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.value

    def get(self, key, version=None):
        if version is None:
            node = self.current_root
        else:
            if version < 0 or version >= len(self.version_history):
                raise IndexError("Invalid version number")
            node = self.version_history[version]
        return self._get(node, key)

    def show_versions(self):
        return [self._to_dict(self.version_history[i]) for i in range(len(self.version_history))]

    def _to_dict(self, node):
        if node is None:
            return None
        return {
            'id': id(node),
            'key': node.key,
            'value': node.value,
            'left': self._to_dict(node.left),
            'right': self._to_dict(node.right)
        }

    def revert_to_version(self, version):
        if version < 0 or version >= len(self.version_history):
            raise IndexError("Invalid version number")
        self.current_root = self.version_history[version]

# Example Usage
phm = PersistentHashMap()
phm.set("d", 1)
phm.set("b", 2)
phm.set("f", 3)
phm.set("a", 4)

# print(phm.get("a"))  # Output: 3
# print(phm.get("b"))  # Output: 2

# print("Version 0:", phm.get("a", version=0))  # Output: 1
# print("Version 1:", phm.get("a", version=1))  # Output: 1
# print("Version 2:", phm.get("a", version=2))  # Output: 3

print("Versions history:")
for i, version in enumerate(phm.show_versions()):
    print(f"Version {i}: {version}")

# Revert to a previous version
# phm.revert_to_version(1)
# print("Reverted to version 1, a:", phm.get("a"))  # Output: 1
# print("Reverted to version 1, b:", phm.get("b"))  # Output: 2
