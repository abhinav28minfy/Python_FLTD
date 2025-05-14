def create_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

double = create_multiplier(2)
print(double(5))  