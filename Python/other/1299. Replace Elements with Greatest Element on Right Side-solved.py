class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)  # 入力リストの長さを取得
        max_right = -1  # 右側での最大値を初期化
        ans = [0] * n  # 答えを格納するリストを初期化

        for i in range(n - 1, -1, -1):
            ans[i] = max_right  # 現在の位置に右側の最大値を格納
            max_right = max(max_right, arr[i])  # 右側での最大値を更新

        return ans  # 答えのリストを返す


if __name__ == "__main__":
    s = Solution()
    nums = [17, 18, 5, 4, 6, 1]
    print(s.replaceElements(nums))
