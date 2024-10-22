import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    for match in re.finditer(r'(?<=\s)(\d+(\.\d+)?)(?=\s)', text):
        yield float(match.group(0))
        
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

text = "The total income of the employee consists of several parts: 1000.00 as the main income, supplemented by additional income of 27.45 and 324 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
