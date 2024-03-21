
class BSTreeNode:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BSTree:
    def __init__(self, root: BSTreeNode = None):
        self.root = root
    
    def _get(self, key) -> tuple[BSTreeNode, BSTreeNode]:
        """
        Finds and return node and its parent
        """
        if not self.root:
            return None, None
        
        # traverse
        node = self.root
        parent = None

        while node:
            if key == node.key:
                return node, parent
            elif key < node.key:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        return None


    def get(self, key):
        node, _ = self._get(key)
        return node.value if node else None

    def set(self, key, value):
        """
        This doesn't support duplicate keys in any special way, simply overwrites the value if key exists.
        """
        if not self.root:
            self.root = BSTreeNode(key, value)
            return
        
        # search node - if found update, else create.
        self._set(key, value)


    def _set(self, key, value, node=None):
        """
        Search for key and update value if key exists, create node with (key, value) otherwise.
        """
        if not node:
            node = self.root

        if node.key == key:
            node.value = value
        elif key < node.key:
            if not node.left:
                node.left = BSTreeNode(key, value)
                return
            else:
                self._set(key, value, node.left)
        elif key > node.key:
            if not node.right:
                node.right = BSTreeNode(key, value)
                return
            else:
                self._set(key, value, node.right)


    def delete(self, key):
        node, parent = self._get(key)

        if not node:
            raise KeyError("key {key} not found")

        # node has no children, delete the node
        if node.left is None and node.right is None:
            self._replace(node, None, parent)
        # node has one child, replace node with its child
        elif node.left and not node.right:
            self._replace(node, node.left, parent)
        elif node.right and not node.left:
            self._replace(node, node.right, parent)
        else:
            # node has both children
            raise NotImplementedError()
    

    def _replace(self, replace, child, parent):
        if parent and parent.left is replace:
            parent.left = child
        elif parent and parent.right is replace:
            parent.right = child
        else: # parent = None
            self.root = replace = child



    def list_in_order(self, node= None, list_ = None):
        """
        Traverses the BST in order and returns it as a list (easy to verify, print)
        """
        if list_ is None:
            list_ = []

        if not node:
            node = self.root
            if not node:
                return list_
    
        if node.left:
            self.list_in_order(node.left, list_) 
        
        list_.append(node.key)
        
        if node.right:
            self.list_in_order(node.right, list_)
        return list_

    def list_pre_order(self):
        raise NotImplementedError()

    def list_post_order(self):
        raise NotImplementedError()