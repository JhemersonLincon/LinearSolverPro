import sys
print(sys.path.append("../"))
from model import LinearProgramming

class DualSimplexMethod(LinearProgramming):
    def __init__(self):
        print("Método Dual Simplex")  
        
if __name__ == '__main__':
    DualSimplexMethod()