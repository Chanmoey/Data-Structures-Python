from UnionFind.UF import UF


class UnionFind5(UF):

    def __init__(self, size):

        self._parent = [i for i in range(size)]
        self._rank = [1] * size

    def get_size(self):
        return len(self._parent)

    # 查找过程，查找元素p所对应的集合编号
    # O(h)复杂度，h为树的高度
    def _find(self, p):

        if p < 0 or p >= len(self._parent):
            raise ValueError("p is out of bound.")

        if p != self._parent[p]:
            self._parent[p] = self._find(self._parent[p])
        return self._parent[p]

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

        # 根据两个元素所在树的元素个数不同判断合并方向
        # 将rank低的集合合并到rank高的集合上
        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[q_root] < self._rank[p_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[q_root] = p_root
            self._rank[p_root] += 1
