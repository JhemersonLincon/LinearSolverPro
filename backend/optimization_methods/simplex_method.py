import numpy as np
class BaseSimplex:
    def __call__(self, objective:list, coefficients:list, restriction:list, type_restriction:list):
        objective, coefficients, restriction = self.adjust_tableau(type_restrictions=type_restriction, objective=objective, coefficients=coefficients, restriction=restriction)
        table = self.get_tableau(objective, coefficients, restriction)
        while True:
            n,m = self.variable_in_out(table)
            if n == None:
                break
            self.solve_table(table = table, in_base=n, leave_base=m)
        return table 
    
    def adjust_tableau(self, type_restrictions, objective, coefficients, restriction):
        for i, type_restriction in enumerate(type_restrictions):
            if type_restriction == "<=":
                objective.append(0)
                coefficients = [row + [0] if i!=j else row + [1] for j, row in enumerate(coefficients)]
            elif type_restriction == ">=":
                pass
            
        objective = -np.array(objective)
        restriction = np.array([0] + restriction)
        return objective, np.array(coefficients), restriction
    
    def get_tableau(self, objective:np.ndarray, coefficients:np.ndarray, restriction:np.ndarray) -> np.ndarray:
        n_variable = objective.shape[0]
        n_restriction = coefficients.shape[0]
        table = np.zeros((n_restriction + 1, n_variable + 1))
        
        table[0, :-1] = objective
        table[1:, :n_variable] = coefficients
        table[:, n_variable] = restriction 
        return table
    
    def variable_in_out(self, table: np.ndarray):
        return NotImplementedError()
        
    def solve_table(self, table:np.ndarray, in_base:int, leave_base:int):
        table[leave_base, :] = table[leave_base, :] / table[leave_base, in_base]
        row_pivot = table[leave_base, :].copy()
        table[:] = table[:] - (table[:, in_base].reshape(table.shape[0], 1) * table[leave_base, :])
        table[leave_base, :] = row_pivot
                                                 
class SimplexMax(BaseSimplex):  
    def variable_in_out(self, table):
        # condição de otimalidade
        in_base = np.min(table[0, :])
        if in_base >= 0: return None, None
        in_base = np.argmin(table[0, :])
        
        # condição de viabilidade
        reason = [a / b if b != 0 and a / b > 0  else np.inf for a, b in zip(table[1:, -1], table[1:, in_base])]
        leave_base = np.argmin(reason) + 1 # Mais 1 devido a exclusão aqui em cima da primeira linha    
        return in_base, leave_base   

class SimplexMin(BaseSimplex):  
    def adjust_tableau(self, type_restrictions, objective, coefficients, restriction):
        objective, coefficients, restriction = super().adjust_tableau(type_restrictions, objective, coefficients, restriction)
        return objective * -1, coefficients, restriction 
         
    def variable_in_out(self, table):
        # condição de otimalidade
        in_base = np.max(table[0, :])
        if in_base <= 0: return None, None
        in_base = np.argmax(table[0, :])
        
        # condição de viabilidade
        reason = [a / b if b != 0 and a / b > 0  else np.inf for a, b in zip(table[1:, -1], table[1:, in_base])]
        leave_base = np.argmin(reason) + 1 # Mais 1 devido a exclusão aqui em cima da primeira linha    
        return in_base, leave_base   
    
if __name__ == '__main__':

    objetivo = [5, 4] #Z = 5x1 + 4x2
    coeficiente = [
        [6, 4],
        [1, 2],
        [-1,1],
        [0, 1]
    ]
    restricao = [24, 6, 1, 2]
    tipo_restricao = ["<=", "<=", "<=", "<="]
    simplex = SimplexMin()
    solve = simplex(objective=objetivo, coefficients=coeficiente, restriction=restricao, type_restriction=tipo_restricao)