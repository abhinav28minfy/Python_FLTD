def compose(x,*functions):
    for f in functions:
        x=f(x)
    return x

def add_one(x):
    return x+1
def double(x):
    return x*2
def square(x):
    return x**2

print(compose(3,add_one,double,square)) # 64  