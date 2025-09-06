from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update the lowest price seen so far
        if price < min_price:
            min_price = price
        # Else, see if selling today brings higher profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit
# Example test cases
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Expected output: 5
print(maxProfit([7, 6, 4, 3, 1]))     # Expected output: 0