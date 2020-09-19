def maxStockProfit(price):
    '''
        first check max profit from n-1 to i

    '''
    n = len(price)
    profit = [0]*(len(price))

    maxPrice = price[n-1]

    for i in range(n-2, 0, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]

        profit[i] = max(profit[i+1], maxPrice-price[i])
    print(profit)
    minPrice = price[0]
    for i in range(1, n):
        if price[i] < minPrice:
            minPrice = price[i]
        print(minPrice, profit[i-1], profit[i] + (price[i] - minPrice))
        profit[i] = max(profit[i-1], profit[i] + (price[i] - minPrice))
        
    print(profit)
    result = profit[n-1]
    return result
print(maxStockProfit([40, 25, 60, 10, 80, 20]))
print(maxStockProfit([2, 30, 15, 10, 8, 25, 80]))