import numpy as np

class minValor:
  @staticmethod
  def posMenor(lista):
    print(lista)
    posição = np.argmin(lista)
    if lista[posição] >= 0:
      return -1
    return posição

  def MenorDif(lista:np.ndarray):
    nZero = np.where(lista == 0, np.inf, lista)
    posição = np.argmin(nZero)
    return posição
