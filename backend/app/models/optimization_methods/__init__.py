from dual_simplex_method import DualSimplexMethod
from simplex_method import SimplexMethod

class FactoryMethod:    
    def __new__(cls, **kwargs):
        if kwargs['method'] == 'SimplexMethod':
            return SimplexMethod()
        elif kwargs['method'] == 'DualSimplexMethod':
            return DualSimplexMethod()
        
        
if __name__ == '__main__':
    A = FactoryMethod(method='SimplexMethod')   
