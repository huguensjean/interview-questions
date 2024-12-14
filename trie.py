from typing import Tuple

class TrieNode:
    """
    A Trie node that stores:
    - A character (`char`)
    - A dictionary of children `char -> TrieNode`
    - A boolean flag indicating end of a word
    - A counter of how many words share this prefix
    """
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 1


def add(root: TrieNode, word: str) -> None:
    """
    Add a word to the trie.

    :param root: The root TrieNode of the trie.
    :param word: The word to add.
    """
    node = root
    for char in word:
        if char in node.children:
            node = node.children[char]
            node.counter += 1
        else:
            new_node = TrieNode(char)
            node.children[char] = new_node
            node = new_node
    node.word_finished = True


def find_prefix(root: TrieNode, prefix: str) -> Tuple[bool, int]:
    """
    Check if a prefix exists in the trie.

    :param root: The root TrieNode of the trie.
    :param prefix: The prefix to search for.
    :return: A tuple (exists, count)
             exists: Boolean indicating if prefix is found
             count: Number of words sharing this prefix if found, otherwise 0.
    """
    node = root
    if not root.children:
        # Empty trie
        return False, 0

    for char in prefix:
        if char in node.children:
            node = node.children[char]
        else:
            # Prefix char not found
            return False, 0

    return True, node.counter


if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, "hack")

    print(find_prefix(root, "hac"))       # (True, count of words starting with "hac")
    print(find_prefix(root, "hack"))      # (True, count of words starting with "hack")
    print(find_prefix(root, "hackathon")) # (True, count of words starting with "hackathon")
    print(find_prefix(root, "ha"))        # (True, count of words starting with "ha")
    print(find_prefix(root, "hammer"))    # (False, 0)
