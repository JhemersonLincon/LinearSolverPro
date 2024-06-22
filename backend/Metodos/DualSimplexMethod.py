from flask import jsonify
import numpy as np
from Utils import minValor

class DualSimplexMethod:

  pivo = {
      "Coluna": 0,
      "Linha":0
  }

  def __init__(self, ladoE, ladoD, f):
    self.tabelaOriginal = []
    self.z, self.matriz = self.__metodoDualSimplex(ladoE, ladoD, f)


  def __montarTabela (self, ladoE, ladoD, função):
    m,n = ladoE.shape
    tabela = np.zeros((m + 1,m + n + 1), dtype=float)

    tabela[:-1,:n] = ladoE
    for i in range(n):
      tabela[-1,i] = -1 * função[i]

    for i in range(0,m):
      tabela[i,-1] = ladoD[i]

    for i in range(0, m):
      tabela[i,i+n] = 1
    print(f"Matriz do projeto:\n{tabela}")
    self.tabelaOriginal = tabela
    return tabela

  def __metodoDualSimplex(self, ladoE, ladoD, f):
    f = np.array(f, dtype = float)
    ladoE = np.array(ladoE, dtype = float)
    ladoD = np.array(ladoD, dtype = float)

    matriz = self.__montarTabela(ladoE, ladoD, f)

    m,n = ladoE.shape

    for i in range(m):

      self.pivo["Linha"] = minValor.posMenor(matriz[:m, -1]) # Pega o menor valor da do lado direito e colocar a posição da linha do pivo no objeto

      if self.pivo["Linha"] == -1: # getColuna vai retornar -1 se não tiver coluna < 0
        break

      vDivisão = self.__divisor(matriz[-1,:m+n], matriz[self.pivo["Linha"], :m+n])

      self.pivo["Coluna"] = minValor.MenorDif(vDivisão)

      matriz[self.pivo["Linha"]] = matriz[self.pivo["Linha"]] / matriz[self.pivo["Linha"],self.pivo["Coluna"]]

      for i in range(0, len(matriz)):
        if i != self.pivo["Linha"]:
          matriz[i,:] = matriz[i,:] - matriz[i, self.pivo["Coluna"]] * matriz[self.pivo["Linha"], :]
      i+=1
    matriz = np.round(matriz, 2)
    z = matriz[m]
    return  z, matriz

  def __divisor(self, v1, v2):
    result = np.zeros(len(v1), dtype = float)
    for i in range(0, len(v1)):
      result[i] = np.abs(v1[i] / v2[i]) if v2[i] != 0 else 0
    return result

  def verificarMDual(self):

    for i in range(self.m):

      if self.restricoes[i] == ">=":
        self.restricoes[i] = "<="
        self.ladoE[i] *= -1
        self.ladoD[i] *= -1

      elif self.restricoes[i] == "=":
        self.restricoes[i] = "<="
        nLinha = self.ladoE[i]
        self.ladoE = np.insert(self.ladoE, i+1, nLinha, axis=0)
        self.ladoD = np.insert(self.ladoD, i+1, self.ladoD[i], axis=0)

        self.m += 1
        self.restricoes = np.insert(self.restricoes, i+1, ">=", axis=0)

  def toString(self):
    return ""+self.matriz