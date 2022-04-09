import models

if __name__ == "__main__":
    inc  = models.Incrementor()
    print (f"initial state: {inc}")
    inc.step
    print(f"after a step: {inc}")
