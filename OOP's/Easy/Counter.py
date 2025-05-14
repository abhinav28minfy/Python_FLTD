class Counter:
    def __init__(self, init=0):
        self.count=init
        self.init=init
    def increment(self):
        self.count+=1
        return self.count
    def decrement(self):
        self.count-=1
        return self.count
    def reset(self):
        self.count=self.init

c1=Counter(0)
print(c1.increment())
print(c1.increment())
c1.reset()
print(c1.increment())
print(c1.increment())
print(c1.decrement())
print(c1.decrement())



