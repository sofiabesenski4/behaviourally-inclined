class IncrementFunc:
    def __init__(self, step_size):
        self.step_size = step_size

    def call(self, current, count=1):
        return current + (self.step_size * count)

    def __repr__(self):
        return f'Adder Function: step_size:{self.step_size}'


class Counter:
    def __init__(self, start=0, step_size=None, step_func=None):
        if step_func:
            self.step_func = step_func
        elif step_size:
            self.step_func = IncrementFunc(step_size)
        else:
            raise "Need to provide either step size or step func"
        self.current = start

    def step(self, count=1):
        self.current = self.step_func.call(self.current, count=count)

    def __repr__(self):
        return f'Incrementor: current={self.current}, \
            step_func={self.step_func}'


if __name__ == "__main__":
    inc = Counter(start=0, step_size=1)
    print(inc)
    inc.step()
    print(inc)
    inc = Counter(start=0, step_size=3)
    print(inc)
    inc.step()
    print(inc)
