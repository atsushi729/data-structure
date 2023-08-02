class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j

            stack.append(i)

        return answer

    def dailyTemperatures_v2(self, temperatures: list[int]) -> list[int]:
        stack = []
        size = len(temperatures)
        ans = [0] * size

        for i in range(size):
            if not stack or temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
                continue

            while stack and temperatures[i] > stack[-1][0]:
                temp, idx = stack.pop()
                ans[idx] = abs(i - idx)

            stack.append((temperatures[i], i))

        return ans


if __name__ == "__main__":
    s = Solution()
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(s.dailyTemperatures_v2(temperatures))
