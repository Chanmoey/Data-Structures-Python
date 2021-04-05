from Map.BSTMap import BSTMap


class BSTMapTrie:

    class _Node:

        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = BSTMap()

    def __init__(self):
        self._root = self._Node()
        self._size = 0

    # 获得Trie中存储的单词数量
    def get_size(self):
        return self._size

    # 向Trie中添加一个新的单词word
    def add(self, word):

        cur = self._root
        for i in range(len(word)):
            c = word[i]
            if cur.next.get(c) is None:
                cur.next.add(c, self._Node())
            cur = cur.next.get(c)

        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    # 查询单词word是否再Trie中
    def contains(self, word):

        cur = self._root
        for i in range(len(word)):
            c = word[i]
            if cur.next.get(c) is None:
                return False
            cur = cur.next.get(c)

        return cur.is_word

    # 查询是否在Trie中有单词以prefix为前缀
    def is_prefix(self, prefix):

        cur = self._root
        for i in range(len(prefix)):
            c = prefix[i]
            if cur.next.get(c) is None:
                return False
            cur = cur.next.get(c)

        return True


if __name__ == '__main__':
    trie = BSTMapTrie()
    words = ['panda', 'pandas', 'apple', 'app', 'banana']
    for word in words:
        trie.add(word)

    print('panda', trie.contains('panda'))
    print('pan', trie.contains('pan'))
    print('zzz', trie.contains('zzz'))
