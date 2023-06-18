class Solution:
    def list_to_int_plus_one(self, numbers: list[int]) -> int:
        numbers[-1] += 1
        is_plus = True
        counter = 1

        while is_plus:

            if numbers[-counter] is not None and numbers[-counter] >= 10:
                if numbers[-counter - 1] is not None:
                    numbers[-counter - 1] += 1
                    numbers[-counter] = 0
                    counter += 1
                else:
                    numbers.insert(0, 1)
                    break
            else:
                is_plus = False

            result = int(''.join([str(i) for i in numbers]))
            return result


if __name__ == "__main__":
    solution = Solution()
    text = [9, 9]
    print(solution.list_to_int_plus_one(text))
