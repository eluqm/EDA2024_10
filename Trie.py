from TNode import TNode

class Trie:
    def __init__(self):
        self.root = TNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if not curr.has_child(c):
                curr.add_children(c, TNode())
            curr = curr.get_child(c)
        curr.set_end(True)
        curr.increments_fecuency()

    def delete(self, word):
        self._remove(self.root, word, 0)

    def _remove(self, curr, word, idx):
        if idx == len(word):
            if not curr.is_end():
                return False
            curr.set_end(False)
            curr.decrement_fecuency()
            return not bool(curr.get_children())

        c = word[idx]
        child = curr.get_child(c)
        if child is None:
            return False

        delete_child = self._remove(child, word, idx + 1)

        if delete_child:
            del curr.get_children()[c]
            return not bool(curr.get_children()) and not curr.is_end()

        return False

    def replace(self, word, new_word):
        self.delete(word)
        self.insert(new_word)

    def search(self, word):
        curr = self.root
        for c in word:
            if not curr.has_child(c):
                return None
            curr = curr.get_child(c)
        return word if curr.is_end() else None

    def autocomplete(self, prefix):
        results = []
        node = self._find_node(prefix)
        if node:
            self._collect_words(node, list(prefix), results)
        return results

    def _find_node(self, prefix):
        curr = self.root
        for c in prefix:
            if not curr.has_child(c):
                return None
            curr = curr.get_child(c)
        return curr

    def _collect_words(self, node, prefix, results):
        if node.is_end():
            results.append(''.join(prefix))
        for c, child in node.get_children().items():
            self._collect_words(child, prefix + [c], results)