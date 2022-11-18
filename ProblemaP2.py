
#Función para ordenar las palabras en una lista
#y en una página
import sys
import time
def listaPalabras(lista:list):
    m = len(lista)
    n = len(lista[0])
    #Inicializa la lista ordenada
    listaOrd = list(0 for i in range(0,m))
    palabras = []

    for i in range(0,m):
        #Insertar número de la lista por posición dada
        listaOrd[lista[i][0]] = lista[i][1:n]

    for i in range(0,m):
        #Concatenar páginas ordenadas
        palabras = palabras + listaOrd[i]

#Retorna todas las palabras ordenadas en una lista
    return palabras


class Pandora:

    def ordenar(self, palabras):
        #Inicializar lista de adyacencia como set en Python
        lista_adj = {c: set() for w in palabras for c in w}
        for i in range(len(palabras)-1):
            #Definir palabra actual recorrida y siguiente a recorrer
            actual,siguiente = palabras[i],palabras[i+1]
            #Longitud mínima de la cadena entre las dos palabras
            minLen = min(len(actual),len(siguiente))
            
            #Existe un prefijo de la palabra anterior - es una contradicción por lo tanto no es posible determinar el ordenamiento
            if ((len(actual) > len(siguiente)) and (actual[:minLen] == siguiente[:minLen])):
                return "ERROR"

            for j in range(minLen):
                if actual[j] != siguiente[j]:
                    #Añadir nodo en lista de adyacencia
                    lista_adj[actual[j]].add(siguiente[j])
                    break       

        sol = []
        visitado = {}

        #Usar DFS para detectar ciclos dentro del grafo
        def dfs(l):
            #Inicializar l como el camino a visitar
            if l in visitado:
                return visitado[l]
            visitado[l] = True
            for cond in lista_adj[l]:
                #True si se detecta ciclo
                if dfs(cond):
                    return True
            #Si no hay ciclos, añade la letra en el resultado y 
            #marca el nodo como visitado
            sol.append(l)
            visitado[l] = False

        #Iterar DFS dentro de todos los caracteres diferentes encontrados
        for ciclo in sorted(lista_adj.keys(), reverse = True):
            #Si hay un ciclo detectado, retorna error
            if dfs(ciclo):
                return "ERROR"
        #Invierte el recorrido DFS de las letras, por ordenamiento inverso
        sol.reverse()
        #Concatenar letras en solucion
        return "".join(sol)

s = Pandora()

def main():
    linea = sys.stdin.readline() 
    casos = int(linea)
    linea = sys.stdin.readline()
    sumaT = 0
    for i in range(0,casos):
       numeros = [int(num) for num in linea.split()]
       lista=[]
       start = time.time()
       for i in range (0,numeros[0]):
        linea = sys.stdin.readline()
        pagina=[obj for obj in linea.split()]
        pagina[0]=int(pagina[0])
        lista.append(pagina)
       ordenado= listaPalabras(lista) 
       respuesta = s.ordenar(ordenado)
       end = (time.time())
       sumaT = sumaT + (end - start) #Tiempo acumulado
       print((respuesta))
       linea = sys.stdin.readline()
    print("Time: "+ str(sumaT))    
main()