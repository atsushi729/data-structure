def permutation(elements: list[int]) -> list[list[int]]:
    result = []

    if len(elements) <= 1:
        return [elements]

    for perm in permutation(elements[1:]):
        for i in range(len(elements)):
            ## 両端の数字がindex番号に応じて増減するイメージ。elements[0:1]は常に中央配置だが、両端が0になることで結果的に端に配置される
            result.append((perm[:i] + elements[0:1] + perm[i:]))

    return result


if __name__ == "__main__":
    for p in permutation([1, 2, 3]):
        print(p)
