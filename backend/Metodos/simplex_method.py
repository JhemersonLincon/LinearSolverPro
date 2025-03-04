import sys
print(sys.path.append("../"))
from model import LinearProgramming
import numpy as np

class SimplexMethod(LinearProgramming):
    def __init__(self, type_objetive, objective, coefficient, restriction):
        self.type_objetive = type_objetive
        self.objective        = np.array(objective)
        self.coefficients     = np.array(coefficient)
        self.restriction      = np.array(restriction)   
        
    def create_table(self) -> np.ndarray:
        n_variable = self.objective.shape[0]
        n_restriction = self.coefficients.shape[0]
        table = np.zeros((n_restriction + 1, n_variable + 1))
        table[0, :-1] = self.objective
        table[1:, :n_variable] = self.coefficients
        table[:, n_variable] = self.restriction 
        return table
    
    def variable_in_out(self, table: np.ndarray):
        
        # condição de otimalidade
        if self.type_objetive == "max":
            in_base = np.min(table[0, :])
            if in_base >= 0: return None, None
            in_base = np.argmin(table[0, :])
        elif self.type_objetive == "min":
            in_base = np.max(table[0, :])
            if in_base <= 0: return None, None    
            
            # condição de viabilidade
        reason = [a / b if b != 0 and a / b > 0  else np.inf for a, b in zip(table[1:, -1], table[1:, in_base])]
        leave_base = np.argmin(reason) + 1 # Mais 1 devido a exclusão aqui em cima da primeira linha
        return in_base, leave_base
    
        
    def solve_table(self, table:np.ndarray, in_base, leave_base):
        table[leave_base, :] = table[leave_base, :] / table[leave_base, in_base]
        for i in range(table.shape[0]):
            if i!= leave_base:
                multiplier = table[i, in_base]
                table[i, :] = table[i, :] - multiplier * table[leave_base, :]
            

if __name__ == '__main__':
    import numpy as np  
    
    objetivo = np.array([-5, -4, 0, 0, 0, 0]) #Z = 3w + 4x + 6y 
    coeficiente = [
        [6, 4, 1, 0, 0, 0],
        [1, 2, 0, 1, 0, 0],
        [-1,1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1]
    ] 
    restricao = [0, 24, 6, 1, 2]
    
    simplex = SimplexMethod("max", objetivo, coeficiente, restricao)
    print(np.argmax(np.where((objetivo < 0), objetivo, -np.inf)))
    table = simplex.create_table()
    # print(table[1:, 0])
    # n,m = simplex.variable_in_out(table)
    # simplex.solve_table(table, n, m)
    # print(table)
    
    # n,m = simplex.variable_in_out(table)
    # simplex.solve_table(table, n, m)
    # print(table)