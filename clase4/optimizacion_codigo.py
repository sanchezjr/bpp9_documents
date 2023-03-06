#compresión listas
cuadrados = []

for i in range(10):
    cuadrados.append(i**2)
    

cuadrados2 = [i**2 for i in range(10)]

print(cuadrados)
print(cuadrados2)

#lista = [expresión for elemento in iterable]

aux  = [0 for i in range(2)]

def cuadrados_f(i):
    return i**2

cuadrados = [cuadrados_f(i) for i in  range(10)]

#lista = [expresión for elemento in iterable if condición]

texto = "Hola mundo"
letras_o = [i for i in texto if i == 'o']

#compresión set

texto = "Hola mundo"
letras_o = {i for i in texto if i == 'o'}

#compresión dict

l1 = ['a','b','c']
l2 = [1,2,3]

mi_dict = {i:j for i, j in zip(l1,l2)}


#lambda
def suma(a,b):
    return a+b

suma = lambda a,b: a+b
suma(2,3)

#usar una única vez
(lambda a,b: a+b)(2,4)

(lambda a,b,c=3: a+b+c)(2,4)

(lambda a,b,c=3: a+b+c)(b=2,a=4)


#programación funcional
#map
#map(funcionar_a_aplicar, iterable)


aux  = [i for i in range(20)]

def cuadrados_f(i):
    return i**2

# l_aux = []
# for l in aux:
#     l_aux.append(cuadrados_f(l))

l_aux = map(cuadrados_f,aux)

print(list(l_aux))

l1 = map(lambda x: x**2, aux)

#filter
#filter(funcion_filtrar,iterable)

l1 = filter(lambda x: x%2==0, aux)#nos da como resultado la lista filtrada


#reduce
#reduce todos los elementos de la entrada a un único valor
#acumulador -> es el valor devuelto de la iteración anterior y que va acumulando el resultado
#valor -> los valores de la lista
from functools import reduce
suma  = reduce(lambda a, b : a+b, l_aux)

suma = sum(l_aux)
