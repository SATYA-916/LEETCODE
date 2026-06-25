class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, l, r, idx):
        if l == r:
            self.tree[node] += 1
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx)

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        return (
            self.query(node * 2, l, mid, ql, qr)
            + self.query(node * 2 + 1, mid + 1, r, ql, qr)
        )


class Solution:
    def countMajoritySubarrays(self, nums, target):
        arr = [1 if x == target else -1 for x in nums]

        pref = [0]
        s = 0

        for x in arr:
            s += x
            pref.append(s)

        vals = sorted(set(pref))
        mp = {v: i for i, v in enumerate(vals)}

        st = SegmentTree(len(vals))

        ans = 0

        st.update(1, 0, len(vals) - 1, mp[pref[0]])

        for x in pref[1:]:
            idx = mp[x]

            if idx > 0:
                ans += st.query(1, 0, len(vals) - 1, 0, idx - 1)

            st.update(1, 0, len(vals) - 1, idx)

        return ans