# 我们的第一版Union-Find
from UnionFind.UF import UF


class UnionFind1(UF):

    def __init__(self, size):
        self._id = [i for i in range(size)]

    def get_size(self):
        return len(self._id)

    # 查找元素p所对应的集合编号
    def _find(self, p):
        if p <0 or p >= len(self._id):
            raise ValueError('p is out of bound')
        return self._id[p]

    # 查看元素p和元素q是否所属一个集合
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    # 合并元素p和元素q所属的集合
    def union_elements(self, p, q):

        p_id = self._find(p)
        q_id = self._find(q)

        if p_id == q_id:
            return

        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
