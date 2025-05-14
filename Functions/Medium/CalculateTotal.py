def calculate_total(*prices,discount=0):
    total=sum(prices)
    if discount:
        total=total*(discount/100)
    return total

print(calculate_total(10,20,30,discount=10))