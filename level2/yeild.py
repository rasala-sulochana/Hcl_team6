
def demo():
    yield "a"
    yield "b"
    yield "c"
    yield "d"
    yield "e"
x=demo()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


num= (x*x for i in range(10000))
print(num)
list=[x for i in range(10)]
print(list)