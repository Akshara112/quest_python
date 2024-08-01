#to find the sum of series
n = int(input('Enter the value of n: '))
m = int(input('Enter the number of terms (m): '))
def sum_of_series(n, m):
    # Initialize
    series_sum = 0
    
    # Calculate the sum of the series
    for i in range(0,m):
        # Calculate the term value: n^i (with sign alternation)
        term = (n) ** i * ((-1) ** i+2)
        # Add the term to the series_sum
        series_sum += term
    
    return series_sum

result = sum_of_series(n, m)
print(f'The sum of the series is: {result}')

