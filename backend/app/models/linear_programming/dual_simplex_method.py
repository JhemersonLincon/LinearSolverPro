from simplex_method import BaseSimplex
import numpy as np

class DualSimplex(BaseSimplex):

    def variable_in_out(self, table):
        # condição de viabilidade dual
        leave_base = np.min(table[1:, -1])
        if leave_base >= 0: return None, None
        leave_base = np.argmin(table[1:, -1])
        leave_base = leave_base + 1  # Mais 1 devido a exclusão aqui em cima da primeira linha  

        # condição de otimalidade dual ?
        reason = [a/b if b < 0 else np.inf for a, b in zip(table[0, :-1], table[leave_base, :-1])]
        in_base = np.min(reason)
        if in_base == np.inf: return None, None
        in_base = np.argmin(in_base)
        return in_base, leave_base


if __name__ == "__main__":
    objetivo = [5, 4] #Z = 5x1 + 4x2
    coeficiente = [
        [6, 4],
        [1, 2],
        [-1,1],
        [0, 1]
    ]
    restricao = [24, 6, -1, 2]
    tipo_restricao = ["<=", "<=", "<=", "<="]

    dual = DualSimplex()
    solve = dual(objective=objetivo, coefficients=coeficiente, restriction=restricao, type_restriction=tipo_restricao)