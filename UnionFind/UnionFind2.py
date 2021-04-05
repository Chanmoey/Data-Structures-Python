from UnionFind.UF import UF


class UnionFind2(UF):

    def __init__(self, size):

        self._parent = [i for i in range(size)]

    def get_size(self):
        return len(self._parent)

    # 查找过程，查找元素p所对应的集合编号
    # O(h)复杂度，h为树的高度
    def _find(self, p):

        if p < 0 or p >= len(self._parent):
            raise ValueError("p is out of bound.")

        while p != self._parent[p]:
            p = self._parent[p]
        return p

    # 查看元素p和元素q是否所属一个集合
    # O(h)复杂度，h为树的高度
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    # 合并元素p和元素q所属的集合
    # O(h)复杂度，h为树的高度
    def union_elements(self, p, q):

        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return

        self._parent[p_root] = q_root
