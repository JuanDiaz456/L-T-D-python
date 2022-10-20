#crear una tupla
tupla = 1, 2, ('a', 'b'), 3
print(tupla)       
print(tupla[2][0]) 

#convertir una lista en tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) 
print(tupla) 

#Se puede iterar una tupla de la misma forma que se hacía con las listas.

tupla = [1, 2, 3]
for t in tupla:
    print(t) #1, 2, 3
