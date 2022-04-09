class Incrementor:
    def __init__(self, step_size=1, start=0):
        self.step_size=int(step_size)
        self.current=int(start)

    def step(self, step_count=1):
        self.current +=  self.step_size*step_count

    def __repr__(self):
        return f'Incrementor: current={self.current}, step_size={self.step_size}'
    
if __name__=="__main__":
    inc = Incrementor()
    print(inc)
    inc.step()
    print(inc)
