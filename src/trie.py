from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # key: character, value: TrieNode
        self.is_word = False


class Trie:
    def __init__(self, root: TrieNode):
        self.root = root
    

    def insert(self, word: str):
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode(c)
        
        node.is_word = True
        return node

    
    def search(self, word: str):
        return self._search(word)
    
    def _search(self, word: str, prefix_check: False)
        node = self.root

        for c in word:
            if c in node:
                node = node.children[c]
            else:
                return False
            
        return node.is_word if not prefix_check else True


    def delete(self, word: str):
        pass


    def starts_with(self, prefix: str):
        return self._search(prefix, True)


    def list_words(self, prefix=''):
        words = []
        node = self.root

        for child in node.children.items():


        return words