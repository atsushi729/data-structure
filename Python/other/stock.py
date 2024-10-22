"""
Coding challenge:
given a 2d array of prices of stocks of different company over 7 days. Find the 3 top company with the highest averages.

Example:
stocks = [
    [100, 180, 260, 310, 40, 535, 695],
    [40, 20, 30, 400, 50, 155, 380],
    [200, 100, 140, 200, 50, 150, 350],
    [100, 180, 260, 310, 40, 535, 695],
    [40, 20, 30, 400, 50, 155, 380],
    [200, 100, 140, 200, 50, 150, 350],
    [100, 180, 260, 310, 40, 535, 695],
    [40, 20, 30, 400, 50, 155, 380],
    [200, 100, 140, 200, 50, 150, 350],
]

Output:
Top company: 1
Average: 345.57
Top company: 3
Average: 345.57
Top company: 7
Average: 345.57

Explanation:
The average of the first company is (100+180+260+310+40+535+695)/7 = 345.57
The average of the third company is (200+100+140+200+50+150+350)/7 = 345.57
The average of the seventh company is (100+180+260+310+40+535+695)/7 = 345.57

Note:
- The output should be sorted in descending order of averages.
- If two companies have the same average, the company which comes first should be placed first.
- The average should be rounded to 2 decimal places.
- The output should be in the format given in the example.
- The input will always have at least 3 companies.
- The input will always have 7 days.
- The input will always have positive integers.
"""

# Design docs
# 1. Calculate the average of each company. -> DONE
# 2. Sort the companies based on the average stock price. -> WIP
# 3. Print the top 3 companies with their average stock price.

stocks = [
    [100, 180, 260, 310, 40, 535, 695],
    [40, 20, 30, 400, 50, 155, 380],
    [200, 100, 140, 200, 50, 150, 350],
    [100, 180, 260, 310, 40, 535, 695],
    [40, 20, 30, 400, 50, 155, 380],
    [200, 100, 140, 200, 50, 150, 350],
    [100, 180, 260, 310, 40, 535, 695],
    [40, 20, 30, 400, 50, 155, 380],
    [200, 100, 140, 200, 50, 150, 350],
]


def top_k_companies_with_average_stock_price(stocks: list[list[int]]) -> list[tuple[int, float]]:
    average = []
    week = 7
    message = "Top company: {}\nAverage: {:.2f}"

    # Calculate the average of stock prices for each company
    for i, stock in enumerate(stocks):
        average.append((i, sum(stock) / week))
        print(message.format(i, sum(stock) / week))

    # Sort the companies based on the average stock price
    average.sort(key=lambda x: x[1], reverse=True)

    return average[:3]


top_3_companies = top_k_companies_with_average_stock_price(stocks)

print("\nOutput:")
for company_id, average_stock_price in top_3_companies:
    print(f"Top company: {company_id} Average: {average_stock_price:.2f}")
