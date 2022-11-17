

def listaPalabras(lista:list):
    m = len(lista)
    n = len(lista[0])
    listaOrd = list(0 for i in range(0,m))
    palabras = []

    for i in range(0,m):
        listaOrd[lista[i][0]] = lista[i][1:n]

    for i in range(0,m):
        palabras = palabras + listaOrd[i]

    return palabras


class Pandora:

    def ordenar(self, palabras):
        lista_adj = {c: set() for w in palabras for c in w}
        for i in range(len(palabras)-1):
            actual,siguiente = palabras[i],palabras[i+1]
            minLen = min(len(actual),len(siguiente))
            
            if ((len(actual) > len(siguiente)) and (actual[:minLen] == siguiente[:minLen])):
                return "ERROR"

            for j in range(minLen):
                if actual[j] != siguiente[j]:
                    lista_adj[actual[j]].add(siguiente[j])
                    break       

        sol = []
        visitado = {}

        def dfs(c):
            if c in visitado:
                return visitado[c]

            visitado[c] = True
            for cond in lista_adj[c]:
                if dfs(cond):
                    return True
            
            sol.append(c)
            visitado[c] = False

        
        for ciclo in sorted(lista_adj.keys(), reverse = True):
            if dfs(ciclo):
                return "ERROR"
        
        sol.reverse()
        return "".join(sol)



list0 = [[1,'x'],[0,'z'],[2,'z']]
list1 = [[0,'xx','xp','pj','jjj','jjw']]
list2 = [[1,"cc","cb"],[0,"ab","ac"]]
list3 = [[1,'mm','mh','nan','nak'],[0,'ab','ah','an','mb']]



list00 = listaPalabras(list0)
list11 = listaPalabras(list1)
list22 = listaPalabras(list2)
list33 = listaPalabras(list3)



s = Pandora()

#Casos ordenando lista
print(s.ordenar(list00))
print(s.ordenar(list11))
print(s.ordenar(list22))
print(s.ordenar(list33))


"""
#Casos sin ordenar lista
print(s.ordenar(["h","hjh","hjmh","hm","j","jjm","m","mh","mmhj"]))
print(s.ordenar(["xx","xp","pj","jjj","jjw"]))
print(s.ordenar(["ab","ac","cc","cb"]))
print(s.ordenar(["ab","ah","an","mb","mm","mh","nan","nak"]))
"""
