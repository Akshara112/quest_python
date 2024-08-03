#to process 4 queries
number_of_shoes, pairs_carry = map(int, input().split())
prices = list(map(int, input().split()))


def calculate_earnings(number_of_shoes, pairs_carry, prices):
    negative_prices = [price for price in prices if price < 0]
    negative_prices.sort()
    most_negative_prices = negative_prices[:pairs_carry]
    total_earnings = -sum(most_negative_prices)
    
    return total_earnings

earnings = calculate_earnings(number_of_shoes, pairs_carry, prices)
print(earnings)