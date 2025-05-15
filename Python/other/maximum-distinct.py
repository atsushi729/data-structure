def maxDistinctAfterSwap(A, B, K):
    a_set = set(A)
    b_set = set(B)

    candidates = [num for num in b_set if num not in a_set]

    current_distinct = len(a_set)
    max_possible = min(len(A), current_distinct + min(K, len(candidates)))

    return max_possible


# テスト例
A = [1, 2, 3]
B = [4, 5, 6]
K = 5

print(maxDistinctAfterSwap(A, B, K))  # 出力: 3
