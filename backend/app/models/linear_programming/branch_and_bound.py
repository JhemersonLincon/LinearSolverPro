from simplex_method import BaseSimplex, SimplexMax
from dual_simplex_method import DualSimplex
import numpy as np


class BranchAndBound:
    def __init__(self, max_depth:int=5, method:BaseSimplex=SimplexMax()):
        self.max_depth  = max_depth
        self.method = method

    def __call__(self, objective:list, coefficients:list, restriction:list, type_restriction:list):
        solve = self.search_soluction_interger(objective=objective, coefficients=coefficients, restriction=restriction, type_restriction=type_restriction, max_depth=0)
        return solve

    def search_soluction_interger(self, objective:list, coefficients:list, restriction:list, type_restriction:list, max_depth = 0):
        
        if max_depth  > self.max_depth: raise Exception("Limite máximo de profundidade atingido")
        
        solve = self.method(objective=objective, coefficients=coefficients, restriction=restriction, type_restriction=type_restriction)
        
        if solve[0, -1] - int(solve[0, -1]) == 0.0:
            return solve
        
        non_integers = [value for value in solve[1:, -1] if isinstance(value, float)]
        branch_row_index = np.argmax(non_integers) + 1

        lower_bound = np.floor(solve[branch_row_index, -1])
        upper_bound = np.ceil(solve[branch_row_index, -1])
        row_solve = solve[branch_row_index, :len(coefficients[branch_row_index-1])].tolist()
        #lower
        lower_coefficients, lower_restriction, lower_type_restriction = self.add_restriction(coefficients=coefficients, restriction=restriction, type_restriction=type_restriction, new_bound=lower_bound, row_solve=row_solve)
        down_solve = self.__call__(objective=objective, coefficients=lower_coefficients, restriction=lower_restriction, type_restriction=lower_type_restriction)
        
        if down_solve[0, -1] - int(down_solve[0, -1]) == 0.0:
            return down_solve
        
        #upper
        upper_coefficients, upper_restriction, upper_type_restriction = self.add_restriction(coefficients, restriction, type_restriction=type_restriction, new_bound=upper_bound, row_solve=row_solve)
        upper_solve = self.__call__(objective=objective, coefficients=upper_coefficients, restriction=upper_restriction, type_restriction=upper_type_restriction)

        if upper_solve[0, -1] - int(upper_solve[0, -1]) == 0.0:
            return upper_solve
        
        return  Exception("Inviavel.")
    
    def add_restriction(self, coefficients, restriction, type_restriction, new_bound, row_solve):

        new_type_restriction = type_restriction.copy()
        new_type_restriction.append('<=')

        new_restriction = restriction.copy()
        new_restriction.append(new_bound.tolist())

        new_coefficients = coefficients.copy()
        new_coefficients.append(row_solve)

        return new_coefficients, new_restriction, new_type_restriction
if __name__ == "__main__":

    objetivo = [5, 4] #Z = 5x1 + 4x2
    coeficiente = [
        [1, 1],
        [10,6],

    ]
    restricao = [5, 45]
    tipo_restricao = ["<=", "<="]

    bound = BranchAndBound()
    solve = bound(objective=objetivo, coefficients=coeficiente, restriction=restricao, type_restriction=tipo_restricao)
    print(solve)