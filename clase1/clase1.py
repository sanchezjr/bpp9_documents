#2/0

#7+numero*2

#'3'+2


#excepciones
# try:
#     '3'+2
# except ZeroDivisionError:
#     print("Error1")
# except NameError:
#     print("Error2")
# except Exception as e:
#     print(f"Error ",e)
# else:
#     print("Se ejecuta siempre que no se ejecute el except")
# finally:
#     print("Se ejecuta siempre")


#raise
#nos permite lanzar excepciones
# a=2
# b=0
# try:
#     # if b==0:
#     #     raise ZeroDivisionError("No puede ser cero el divisor")
#     # else:
#     #     a/b
# except ZeroDivisionError:
#     print("Error")


#assert
#nos permite realizar comprobaciones
#comprueba una condición y si es falsa lanza una excepción

assert(4==4)


# if condicion:
#     raise AssertionError()

#assert False, "Mensaje personalizado de Assert"

#assert en testing

def calcular(a,b):
    return a+b

assert(calcular(2,2) == 4)

def suma_enteros(a,b):
    assert type(a)==int , "Mi mensaje" 
    assert type(b)==int
    return a+b

suma_enteros(2,2)

class miExcepcion(Exception):
    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2


try:
    
    raise miExcepcion("Valor param1", "Valor param2")
except Exception as e:
    p1,p2 = e.args
    print(p1,p2)

class miOtraExcepcion(Exception):
    pass

try:
    
    raise miOtraExcepcion({"mensaje":"mensaje de la excepción", "información":"info"})
except Exception as e:
    parametros= e.args[0]
    print(parametros["mensaje"],parametros["información"])