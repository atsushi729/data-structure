class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []

        for i in range(0, len(temperatures) - 1):

            if temperatures[i] < temperatures[i + 1]:
                answer.append(1)
                continue

            wait_days = 1
            while temperatures[i] >= temperatures[i + wait_days]:

                if temperatures[i] >= temperatures[i + wait_days]:
                    wait_days += 1

                if len(temperatures) <= i + wait_days:
                    answer.append(0)
                    break

                if temperatures[i] < temperatures[i + wait_days]:
                    answer.append(wait_days)
                    break
        answer.append(0)

        return answer


if __name__ == "__main__":
    s = Solution()
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(s.dailyTemperatures(temperatures))
