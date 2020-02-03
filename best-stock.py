def best_stock(a):
    bestStock = ""
    bestStockPrice = 0
    for item in a:
        if a[item] > bestStockPrice:
            bestStockPrice = a[item]
            bestStock = item

    return bestStock


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")




"""best solution

def best_stock(data):
    return max(data, key=data.__getitem__)
"""
