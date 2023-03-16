def maxProfit(prices: list[int]):
    current_max = 0
    income_list = []

    for i in prices:

        for j in range(1, len(prices)):
            if i > j:
                continue

            income = j - i

            if income > current_max:
                current_max = income

    income_list.append(current_max)
    return income_list


target = list(map(int,input().split()))

if maxProfit(target):
    print('OK')
