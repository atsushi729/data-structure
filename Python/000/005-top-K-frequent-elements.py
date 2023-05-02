class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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