import sys
import time
import random
from time import perf_counter
import matplotlib.pyplot as plt


class BuscadorDePares:
  def __init__(self, argv):
    self.argv = argv
    self.ejecutar()

  @staticmethod
  def convertir_lista(lista):
    return list(map(int, lista))

  @staticmethod
  def encontrar_pares(arr, suma):
    pares =[]
    for i in range(len(arr)):
      for j in range(i+1, len (arr)):
        if arr[i]+arr[j] == suma:
          pares.append((arr[i],arr[j]))
    return pares

  @staticmethod
  def leer_archivo(nombre):
    with open(nombre, 'r') as archivo:
      lineas = list(map(str.strip, archivo.readlines()))
    return lineas



  def ejecutar(self):
    if len(self.argv) == 1:
      times = []
      tamanios = []
      for i in range(100):
        arreglo_i = []
        for j in range(i + 5):
          arreglo_i.append(random.randint(1, 100))
        tamanios.append(i+5)
        inicio = time.perf_counter()
        resultado = self.encontrar_pares(arreglo_i, 0)
        final = time.perf_counter()
        times.append(final-inicio)
      plt.plot(tamanios, times)
      plt.title(label="Algoritmo original")
      plt.show()
    elif len(self.argv) == 3:
      lista = self.convertir_lista(self.argv[1].split(','))
      inicio = time.perf_counter()
      resultado = self.encontrar_pares(lista, int(self.argv[2]))
      final = time.perf_counter()
      tiempoCalculado = final - inicio
      print(*resultado, sep='\n')
    elif len(self.argv) == 2:
      tex = self.leer_archivo(self.argv[1])
      for i in range(len(tex)):
        lista = self.convertir_lista(tex[1].split()[0].split(','))
        resultado = self.encontrar_pares(lista, int(tex[i].split()[1]))
        print(*resultado, sep="\n")
    else:
      print("Los datos no son correctos")


if __name__ == '__main__':
  buscador_de_pares = BuscadorDePares(sys.argv)
  