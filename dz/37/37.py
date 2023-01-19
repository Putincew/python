class Power:
    def __init__(self, step):
        self.step = step


    def __call__(self, fn):
        def wrap(a, b):
            return f'Результат ({a} + {b}) **{self.step}: {fn(a, b) **self.step}'

        return wrap


@Power(3)
def funk(a, b):
    return a + b


print(funk(2, 2))