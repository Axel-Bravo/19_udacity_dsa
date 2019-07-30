#%% Imports and functions declaration
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """

        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char] = TrieNode()
                node = node.children[char]
                node.is_word = True
            else:
                node.children[char] = TrieNode()
                node = node.children[char]

        pass

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                try:
                    node = node.children[char]
                    return node.is_word
                except KeyError:
                    return False
            else:
                try:
                    node = node.children[char]
                except KeyError:
                    return False

#%% Testing

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))