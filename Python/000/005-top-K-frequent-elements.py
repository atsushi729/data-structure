def topKFrequent(nums: [int], k: int) -> [int]:
    if not nums or not k:
        return 0

    seen = set()
    calc = {}

    for num in nums:
        if num in seen:
            calc[num] += 1
        else:
            seen.add(num)
            calc.setdefault(num, 0)
            calc[num] += 1

    sorted_dict = dict(sorted(calc.items(), key=lambda x: x[1], reverse=True))

    return list(sorted_dict.keys())[:k]


def model_topKFrequent(nums: [int], k: int) -> [int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res
