from functools import reduce
from typing import List


def sales_with_tax(sales: List[float], tax_rate: float, threshold: float = 300) -> List[float]:
    return list(map(lambda x: x * (1 + tax_rate), filter(lambda x: x > threshold, sales)))


def sum_sales(sales: List[float], threshold: float = 300) -> float:
    filtered_sales = list(filter(lambda x: x > threshold, sales))
    return reduce(lambda x, y: x + y, filtered_sales)


def average_age(ages: List[int], threshold: int = 30) -> float:
    filtered_ages = list(filter(lambda x: x > threshold, ages))
    return reduce(lambda x, y: x + y, filtered_ages) / len(filtered_ages)


def increased_prices(prices: List[float], increase_rate: float = 0.2, threshold: float = 300) -> List[float]:
    return list(filter(lambda x: x > threshold, map(lambda x: x * (1 + increase_rate), prices)))


def weighted_sale_price(sales: List[float]) -> float:
    total_cost = reduce(lambda x, y: x + y[0] * y[1], sales, 0)
    total_sales = reduce(lambda x, y: x + y[1], sales, 0)
    return total_cost / total_sales
