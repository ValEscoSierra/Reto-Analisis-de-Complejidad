import sys
import time
import random
import matplotlib.pyplot as plt


class BuscadorDePares:
    def __init__(self, argv):
        self.argv = argv
        self.ejecutar()

    @staticmethod
    def convertir_lista(lista):
        return list(map(int, lista))

    @staticmethod
    def encontrar_pares_original(arr, suma):
        pares = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == suma:
                    pares.append((arr[i], arr[j]))
        return pares

    @staticmethod
    def encontrar_pares_hash_table(arr, suma):
        hash_table = {}
        pares = []
        for num in arr:
            complemento = suma - num
            if complemento in hash_table:
                pares.append((num, complemento))
            hash_table[num] = True
        return pares

    def encontrar_pares(self, arr, suma):
       
        pares = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == suma:
                    pares.append((arr[i], arr[j]))
        return pares



    def ejecutar(self):
        if len(self.argv) == 1:
            times = []
            tamanios = []
            for i in range(100):
                arreglo_i = []
                for j in range(i + 5):
                    arreglo_i.append(random.randint(1, 100))
                tamanios.append(i + 5)
                inicio = time.perf_counter()
                resultado = self.encontrar_pares(arreglo_i, 0)
                final = time.perf_counter()
                times.append(final - inicio)
            plt.plot(tamanios, times, marker='o', linestyle='-', color='b', label='Datos de ejemplo')
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

        # Obtener tiempos de ejecución para el enfoque original
        times_original = []
        for i in range(5, 105, 5):
            arreglo_i = [random.randint(1, 100) for _ in range(i)]
            inicio = time.perf_counter()
            resultado = self.encontrar_pares_original(arreglo_i, 12)  # Buscar el número 12 como objetivo
            final = time.perf_counter()
            times_original.append(final - inicio)

        # Obtener tiempos de ejecución para el enfoque con tabla de hash
        times_hash_table = []
        for i in range(5, 105, 5):
            arreglo_i = [random.randint(1, 100) for _ in range(i)]
            inicio = time.perf_counter()
            resultado = self.encontrar_pares_hash_table(arreglo_i, 12)  # Buscar el número 12 como objetivo
            final = time.perf_counter()
            times_hash_table.append(final - inicio)

        # Graficar los resultados
        tamanios = list(range(5, 105, 5))
        plt.plot(tamanios, times_original, marker='o', linestyle='-', color='b', label='Enfoque Original')
        plt.plot(tamanios, times_hash_table, marker='o', linestyle='-', color='r', label='Tabla de Hash')

        plt.xlabel('Tamaño de la lista de entrada')
        plt.ylabel('Tiempo de ejecución (segundos)')
        plt.title('Comparación de tiempos de ejecución entre enfoques')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    buscador_de_pares = BuscadorDePares(sys.argv)
