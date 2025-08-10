def portfolio_input():
    while True:
        portfolio_size = input('Enter the value of your portfolio: ')
        try:
            return float(portfolio_size)
        except ValueError:
            print('Please enter a valid number!')

def num_stocks_input():
    while True:
        num = input('Enter the number of stocks you want: ')
        try:
            return int(num)
        except ValueError:
            print('Please enter a valid integer!')