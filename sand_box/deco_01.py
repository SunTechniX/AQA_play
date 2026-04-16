from typing import Callable

def deco(f_: Callable):
    def wrap():
        print("Starting...")
        res = f_()
        print(res)
        print("Stopping!")
        return res
    return wrap

@deco
def f():
    return 12

print(f())

