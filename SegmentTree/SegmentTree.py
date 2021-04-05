class SegmentTree:

    def __init__(self, arr, merger):

        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)
        self._merger = merger
        self._build_segment_tree(0, 0, len(self._data) - 1)

    # 在tree_index的位置创建表示区间[l...r]的线段树
    def _build_segment_tree(self, tree_index, l, r):

        if l == r:
            self._tree[tree_index] = self._data[l]
            return

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        mid = l + (r - l) // 2
        self._build_segment_tree(left_tree_index, l, mid)
        self._build_segment_tree(right_tree_index, mid + 1, r)
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index],
            self._tree[right_tree_index],
        )

    def get_size(self):
        return len(self._data)

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise ValueError('Index is illegal.')
        return self._data[index]

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    def _left_child(self, index):
        return 2 * index + 1

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    def _right_child(self, index):
        return 2 * index + 2

    # 返回区间[query_l, query_r]的值
    def query(self, query_l, query_r):

        if query_l < 0 or query_l >= len(self._data) or \
                query_r < 0 or query_r >= len(self._data) or \
                query_l > query_r:
            raise ValueError('Index is illegal.')

        return self._query(0, 0, len(self._data) - 1, query_l, query_r)

    # 在treeID为根的线段树中[l...r]的范围里，搜索区间[query_l...query_r]
    def _query(self, tree_index, l, r, query_l, query_r):

        if l == query_l and r == query_r:
            return self._tree[tree_index]

        mid = l + (r - l) // 2
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        if query_l >= mid + 1:
            return self._query(right_tree_index, mid + 1, r, query_l, query_r)
        elif query_r <= mid:
            return self._query(left_tree_index, l, mid, query_l, query_r)

        left_result = self._query(left_tree_index, l, mid, query_l, mid)
        right_result = self._query(right_tree_index, mid + 1, r, mid + 1, query_r)

        return self._merger(left_result, right_result)

    # 将index位置的值，更新为e
    def set(self, index, e):

        if index < 0 or index >= len(self._data):
            raise ValueError("Index is illegal")

        self._data[index] = e
        self._set(0, 0, len(self._data) - 1, index, e)

    def _set(self, tree_index, l, r, index, e):
        if l == r:
            self._tree[tree_index] = e
            return

        mid = l + (r - l) // 2
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        if index >= mid + 1:
            self._set(right_tree_index, mid + 1, r, index, e)
        else:
            self._set(left_tree_index, l, mid, index, e)

        self._tree[tree_index] = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])

    def __str__(self):
        res = ['[']

        for i in range(len(self._tree)):
            res.append(str(self._tree[i]))
            if i != len(self._tree) - 1:
                res.append(', ')
        res.append(']')

        res = ''.join(res)
        return res


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    seg_tree = SegmentTree(nums, lambda a, b: a + b)
    print(seg_tree.query(0, 2))
    print(seg_tree.query(2, 5))
    print(seg_tree.query(0, 5))
