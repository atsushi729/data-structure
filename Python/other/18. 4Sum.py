class Solution:
    def fourSum(self, a: list[int], b: int) -> list[list[int]]:
        k = []
        u = []
        a.sort()

        def freq(a):
            f = {}
            for i in range(len(a)):
                if a[i] not in f:
                    f[a[i]] = 1
                else:
                    f[a[i]] += 1
            return (f)

        for i in range(len(a)):
            for j in range(i, len(a) - 1):
                l = j + 1
                h = len(a) - 1
                while l < h:
                    res = a[i] + a[j] + a[l] + a[h]
                    if (res == b) and (freq([a[i], a[j], a[l], a[h]]) not in u) and (i != j != l != h):
                        k.append([a[i], a[j], a[l], a[h]])
                        u.append(freq([a[i], a[j], a[l], a[h]]))
                        l = l + 1
                    elif res > b:
                        h = h - 1
                    else:
                        l = l + 1
        return (k)
