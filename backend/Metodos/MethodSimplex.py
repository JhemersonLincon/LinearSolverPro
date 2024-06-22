import numpy as np
from numpy.linalg import LinAlgError
from itertools import combinations

class minValor:
    @staticmethod
    def posMenor(arr):
        # Substitui zeros por infinito
        arr = np.where(arr[:-1] == 0, np.inf, arr[:-1])
        # Encontra o menor valor no array modificado
        min_val = np.min(arr)
        if min_val > 0:  # Se o menor valor é infinito, não há valores válidos
            return -1
        return np.argmin(arr)

    @staticmethod
    def MenorDif(arr):
        arr = np.where(arr <= 0, np.inf, arr)
        return np.argmin(arr)

class MethodSimplex:
    pivo = {
        "Coluna": None,
        "Linha": None
    }

    def __init__(self, ladoE, restricoes, ladoD,  funcao):
        
        self.ladoE = ladoE
        self.restricoes = restricoes
        self.ladoD = ladoD
        self.funcao = funcao


    def __montarTabela(self, ladoE, restricoes, ladoD, funcao):
        print(f"Lado esquerdo:\n {self.ladoE}")
        
        print(f"Lado direito:\n{self.ladoD}")
        m, n = self.ladoE.shape
        artificial_count = 0
        artificial_pos = []
        excess_count = 0
        for i in range(m):
            if self.ladoD[i] < 0:
                self.ladoE[i, :] *= -1
                self.ladoD[i] *= -1
                if self.restricoes[i] == "<=":
                    self.restricoes[i] = ">="
                else:
                    self.restricoes[i] = "<="
        
        for restricao in self.restricoes:
            if restricao == ">=":
                artificial_count += 1
                excess_count += 1
            elif restricao == "=":
                artificial_count += 1

        total_vars = n + m + artificial_count
        tabela = np.zeros((m + 1, total_vars + 1), dtype=float)
        artificial_index = 0

        for i in range(m):
            if self.restricoes[i] == "<=":
                tabela[i, :n] = self.ladoE[i]
                tabela[i, n + i] = 1
                
            elif self.restricoes[i] == ">=":
                tabela[i, :n] = self.ladoE[i]
                tabela[i, n + i] = -1
                tabela[i, n + m + artificial_index] = 1
                tabela[-1, n + m + artificial_index] = -1
                artificial_pos.append([i, n+m+artificial_index])
                artificial_index += 1
            elif self.restricoes[i] == "=":
                tabela[i, :n] = self.ladoE[i]
                tabela[i, n + m + artificial_index] = 1
                artificial_index += 1

        tabela[:-1, -1] = self.ladoD

        for i in range(n):
            tabela[-1, i] = -1 * self.funcao[i]

        return artificial_pos, tabela
    
    def __divisor(self, v1, v2):
        result = np.zeros(len(v1), dtype=float)
        for i in range(len(v1)):
            if v2[i] != 0:
                result[i] = v1[i] / v2[i]
            else:
                result[i] = 0  # Define como infinito se houver divisão por zero
        return result

        
    def metodoSimplex(self):
        f = np.array(self.funcao, dtype=float)
        self.ladoE = np.array(self.ladoE, dtype=float)
        self.ladoD = np.array(self.ladoD, dtype=float)

        artificial, matriz = self.__montarTabela(self.ladoE, self.restricoes, self.ladoD, f)
        print(f"Matriz Inicial:\n{matriz}")
        m, n = self.ladoE.shape
        interações = []
        
        if artificial:
            art = matriz[artificial[0][0]].copy()
            for i in range(1, len(artificial)):
                art += matriz[artificial[i][0]].copy()
            art *= -1  
                
            matriz = np.vstack([matriz, art]) 
            totalInterações = 0
            while totalInterações != 5:
                self.pivo["Coluna"] = minValor.posMenor(matriz[-1])
                
                if self.pivo["Coluna"] == -1:
                    break
                vDivisao = self.__divisor(matriz[:m, -1], matriz[:m, self.pivo["Coluna"]])
                self.pivo["Linha"] = minValor.MenorDif(vDivisao)

                matriz[self.pivo["Linha"]] = matriz[self.pivo["Linha"]] / matriz[self.pivo["Linha"], self.pivo["Coluna"]]

                for i in range(len(matriz)):
                    if i != self.pivo["Linha"]:
                        multiplicador = matriz[i, self.pivo["Coluna"]]
                        linha_pivo = matriz[self.pivo["Linha"], :]
                        print(f"{matriz[i, :]} - {multiplicador} * {linha_pivo} = {matriz[i,:] - multiplicador * linha_pivo}" )

                        matriz[i, :] = matriz[i, :] - multiplicador * linha_pivo
                        
            print(f"Matriz relaxada final:\n {matriz}")
            matriz = np.round(matriz, 2)
            matriz = np.delete(matriz, -1, axis=0)
              
            for i in range(len(artificial)):
                matriz = np.delete(matriz, artificial[i][1] - i, axis=1)
                
        print(f"Removido\n{matriz}")
        totalInterações = 0
        while totalInterações != 5:
            totalInterações += 1
            interações.append(matriz.copy())
            self.pivo["Coluna"] = minValor.posMenor(matriz[-1])
            
            if self.pivo["Coluna"] == -1:
                break
            vDivisao = self.__divisor(matriz[:m, -1], matriz[:m, self.pivo["Coluna"]])
            self.pivo["Linha"] = minValor.MenorDif(vDivisao)

            matriz[self.pivo["Linha"]] = matriz[self.pivo["Linha"]] / matriz[self.pivo["Linha"], self.pivo["Coluna"]]

            for i in range(len(matriz)):
                if i != self.pivo["Linha"]:
                    multiplicador = matriz[i, self.pivo["Coluna"]]
                    linha_pivo = matriz[self.pivo["Linha"], :]
                    matriz[i, :] = matriz[i, :] - multiplicador * linha_pivo
                    

            matriz = np.round(matriz, 2)
        print(f"Matriz final:\n {matriz}")
        interações.append(matriz.copy())
        interações = np.array(interações, dtype=np.float64)
        resultado = np.zeros(matriz.shape[1])
        
        for i in range(0, len(matriz[-1, :-1])):
            for j in range(0, len(matriz[:-1, 1])):
                
                print(matriz[j, i])
                if matriz[j, i] == 1:
                    vali = True
                    for k in range(0, j):
                        if matriz[j, k] == matriz[j, i]:
                            vali = False
                    if vali: 
                        resultado[i] = matriz[j, -1]
        resultado[-1] = matriz[-1, -1]     
        print(f"Resultado: {resultado}")
        
        z = matriz[-1]
        
        print(f"Verificação: {z[:-1]}")
        if np.min(resultado) >= 0:
            print("Tudo certo por aqui")
            return {"Iteracoes": interações.tolist(), "resultado": np.array(resultado).tolist(), "matriz": matriz.tolist()}
        raise ValueError("Existem valores infinitos para o valor ótimo.")
    

    def is_integer_solution(self, solution):
        return np.all(np.floor(solution) == solution)
    
    def branch_and_bound(self):
        best_solution = None
        best_value = float('-inf')
        
        stack = [(self.ladoE, self.restricoes, self.ladoD, self.funcao)]
        
        while stack:
            ladoE, restricoes, ladoD, funcao = stack.pop()
            
            simplex = MethodSimplex(ladoE, restricoes, ladoD, funcao)
            try:
                result = simplex.metodoSimplex()
                solution = np.array(result["resultado"][:-1])
                value = result["resultado"][-1]
                iterações = np.array(result["Iteracoes"])
                if self.is_integer_solution(solution):
                    if value > best_value:
                        best_value = value
                        best_solution = solution
                else:
                    for i in range(len(solution)):
                        if not solution[i].is_integer():
                            lower_bound = np.floor(solution[i])
                            upper_bound = np.ceil(solution[i])
                            
                            new_ladoE1 = np.vstack([ladoE, np.eye(1, ladoE.shape[1], i)])
                            new_restricoes1 = restricoes + ["<="]
                            new_ladoD1 = np.append(ladoD, lower_bound)
                            
                            new_ladoE2 = np.vstack([ladoE, np.eye(1, ladoE.shape[1], i)])
                            new_restricoes2 = restricoes + [">="]
                            new_ladoD2 = np.append(ladoD, upper_bound)
                            
                            stack.append((new_ladoE1, new_restricoes1, new_ladoD1, funcao))
                            stack.append((new_ladoE2, new_restricoes2, new_ladoD2, funcao))
                            break
            except ValueError as e:
                pass
        
        if best_solution is None:
            raise ValueError("Não foi encontrada uma solução inteira.")
        
        return {"resultado":best_solution.tolist(),"Iteracoes":iterações.tolist()}

# # Exemplo de uso
# ladoE = np.array([[2, 1], [1, 2]])
# restricoes = ["<=", "<="]
# ladoD = np.array([15, 20])
# funcao = [3, 2]

# method = MethodSimplex(ladoE, restricoes, ladoD, funcao)
# best_solution, best_value = method.branch_and_bound()
# print(f"Melhor solução inteira: {best_solution}, com valor: {best_value}")
