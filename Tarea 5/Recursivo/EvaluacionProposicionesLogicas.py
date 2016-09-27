#Manual de uso
#Nombres
print "-----------NOTACION DE LAS CONECTIVAS LOGICAS----------|"
print "Negacion                                             --|"
print "Conjuncion v                                         --|"
print "Disyuncion ^                                         --|"
print "Condicional =>                                       --|"
print "Bicondicional <=>                                    --|"
print "Ejemplo:                                             --|"
print "Premisas: p q r                                      --|"
print "Valores: True True False                             --|"
print "Proposicion logica: (  p ^ ( r v (  q <=> ( ~ p <=> q ) ) => r  ) )"
print "-------------------------------------------------------|\n"

#Funcion que recibe:
#Una lista que contiene los elementos de una proposicionlogica
#ElemenTos que debe de sacar de esa lista, segun la operacion realizada
#Resultado obtenido de la operacion, para poder insertarlo sustituyendo las premisas evaluadas
#Tipo de conectiva logica que se opero, este se utiliza por que para la negacion se opera de diferente manera
#Regresa en una lista la proposicion logica modificada y la lista de elementos a sacar

def insertResult(expresion, elementosASacar, resultado, tipo):
    if (tipo == "v" or tipo == "^" or tipo == "=>" or tipo == "<=>"):
#Por medio del for sacara la cantidad de elementos que se deben de eliminar
        for i in range(0,3):
            expresion.pop(elementosASacar[0])
#Una vez eliminados los elementos evaluados se inserta el resultado
        expresion.insert(elementosASacar[0],resultado)
#Si existen parentesis en los extremos de la proposicion logica se eliminan
        if ( (expresion[elementosASacar[0]-1] == "(") and (expresion[elementosASacar[0]+1] == ")") ):
            expresion.pop(elementosASacar[0]-1)
            expresion.pop(elementosASacar[0])
    elif (tipo == "~"):
#Se eliminaran los simbolos utilizados para la negacion)
        expresion.pop(elementosASacar[0])
        expresion.pop(elementosASacar[0])
#Se inserta el resultado obtenido de los elementos de la negacion
        expresion.insert(elementosASacar[0],resultado)
#Si existen parentesis en los extremos de la proposicion logica se eliminan
        if ( (expresion[elementosASacar[0]-1] == "(") and (expresion[elementosASacar[0]+1] == ")") ):
            expresion.pop(elementosASacar[0]-1)
            expresion.pop(elementosASacar[0])
            
#Al acabar de hacer las operaciones se limpia la lista que contenia los indices de los elementos a sacar
    del elementosASacar[:]  
    return expresion, elementosASacar   

#Funcion que verifica si ya no existen parentesis en los extremos de la proposicion logica
#Si aun hay parentesis, significa que se necesita seguir procesando para obtener el resultado final
#Regresa un booleano para controlar el flujo del while
def verifyKeepProcessing(expresion, keepProcessing,simb):
    if ((expresion[0] not in simb)):
        keepProcessing = False
    return keepProcessing

#Esta funcion cambiara cada simbolo de las premisas (p,q,r...) por sus respectivos valores (True, False, False...)
def setValues(expresion, premisas, valores):
    longValores = len(valores)
    for i in range (0, len(expresion)):
        if (expresion[i] in premisas):
            for j in range (0, len(premisas)):
                if (expresion[i] == premisas[j]):
                    expresion[i] = valores[j]
                    
#Funcion que verifica si se podra evaluar el elemento encontrado (se podra evaluar siempre y cuando en los extremos no tenga parentesis)
#Regresara True si no encuentra parentesis en los extremos
def checkIfProced( expresion, simb ):
    if ((expresion[i-1] not in simb) and (expresion[i+1] not in simb)):
        return True
#Funcion bicondicional, recibe la expresion y por medio del  indice de la conectiva logica evalua las premisas
#Regresa:
#La proposicion logica
#PopElements -> Indices de los elementos que se deben sacar
#Resultado que se obtiene de evaluar las premisas con la conectiva logica indicada
#Tipo de conectiva que se uso
def Biconditional(expresion):
    tipo = "<=>"
    if ((expresion[i-1] == True and expresion[i+1] == False) or (expresion[i-1] == False and expresion[i+1] == True)):
        resultado = False
    else:
        resultado = True
        popElements.append(i-1)
        
    return expresion, popElements, resultado, tipo
#Funcion Condicional, recibe la expresion y por medio del  indice de la conectiva logica evalua las premisas
#Regresa:
#La proposicion logica
#PopElements -> Indices de los elementos que se deben sacar
#Resultado que se obtiene de evaluar las premisas con la conectiva logica indicada
#Tipo de conectiva que se uso
def Conditional (expresion):
    if (expresion[i-1] == True and expresion[i+1] == False):
        resultado = False
    else:
        resultado = True
    popElements.append(i-1)
    tipo = "=>"
    return expresion, popElements, resultado, tipo
#Funcion disjuncion y conjuncion, recibe la expresion, tipo de operacionn a realizar y por medio del indice de la conectiva logica evalua las premisas
#Regresa:
#La proposicion logica
#PopElements -> Indices de los elementos que se deben sacar
#Resultado que se obtiene de evaluar las premisas con la conectiva logica indicada
#Tipo de conectiva que se uso
def ConDisJunction(expresion, conectiva):
    if (conectiva == "v"):
        resultado = bool(expresion[i-1]) or bool(expresion[i+1])
        tipo = "v"
    else:
        resultado = bool(expresion[i-1]) and bool(expresion[i+1])
        tipo = "^"
    popElements.append(i-1)
    return expresion, popElements, resultado, tipo


premisas = raw_input("Ingrese las premisas separadas por un espacio: ")

valores = raw_input ("Ingrese los valores de cada premisa separados por un espacio: ")

expresion = raw_input("Ingrese la proposicion logica a evaluar\nNOTA: Cada elemento debe ir separado por espacio (excepto implicacion y bicondicional, esas van juntas): ")

"""
#######SI NO DESEA INGRESAR MANUALMENTE LOS DATOS, PUEDE INGRESAR LAS OPCIONES EN LAS SIGUIENTES LINEAS (QUITANDO LOS #)########
#ELIJA UNA O SUSTITUYELA POR ALGUNA OTRA
#expresion = "( ( ( ~ p v ~ q ) ^  ~ r )  v ~ p )"
#expresion = "( ( p ^ q ) ^  q )"
#expresion = "( ( ( ( p ^ q ) ^ q )  ^ r ) ^ q )"
#expresion = "( ( ( p v q ) v r ) ^ p )"
#expresion = "( ( p => q ) =>  ~ p )"
expresion = "(  p ^ ( r v (  q <=> ( ~ p <=> q ) ) => r  ) )"
#expresion = "( p v q )"
expresion = expresion.split()
premisas = ["p","q","r"]
valores = [False, True, True]
"""
#Impresion de los elementos entrantes

print "\nProposicion " + str(expresion)
valores = valores.split()
premisas = premisas.split()
print "Premisas " + str(premisas)
print "Valores " + str(valores)
expresion = expresion.split()
#Variables que se usaran dentro del programa
popElements = []        # Lista donde se guardaran los indices de los elementos que ya se operaron
keepProcessing = True   # Bandera que le indicara al programa cuando esta completamente evaluada la proposicion logica
tipo = ""               # Bandera que indicara al programa que tipo de conectiva se esta trabajando

#Lista de simbolos quen usaremos para identificar a los parentesis

simb = ["(",")"]

#Asignar los valores a la proposicion logica
setValues(expresion, premisas, valores)

#Ciclo infinito para el procesamiento de la proposicion logica, hasta que se cumpla que la bandera keepProcessing sea Falsa (cuando ya acabo)
while (keepProcessing == True):
#Evaluara continuamente hasta que se hayan sustituido todas las conectivas not
    while ( "~" in expresion ):
        for i in range (0,len(expresion)):
            if (expresion[i] == "~" and expresion[i+1] in valores):
                popElements.append(i)
                resultado = not(bool(expresion[i+1]))
                tipo = "~"
                expresion, popElements = insertResult(expresion, popElements, resultado, tipo)
                break
#A partir de este for evaluaremos la proposicion logica con respecto a las demas conectivas logicas        
    for i in range (0,len(expresion)):
#Cuando detecte alguna conectiva mandara a llamar a la funcion y esta regresara los valores necesarios para la evaluacion
        if (expresion[i] == "^"):
            if ( checkIfProced( expresion, simb ) ):
#Se manda a llamar a la funcion ConDisJunction, posteriormente en la funcion se opera con respecto a "^"
                expresion, popElements, resultado, tipo = ConDisJunction(expresion, "^")
#Por medio de la siguiente linea se usan los valores retornados de la funcion de la
#conectiva y se insertan y eliminan los elementos necesarios de la expresion.
                expresion, popElements = insertResult(expresion, popElements, resultado, tipo)
                break
        elif (expresion[i] == "v"):
            if ( checkIfProced( expresion, simb ) ):
#Se manda a llamar a la funcion ConDisJunction, posteriormente en la funcion se opera con respecto a "v"
                expresion, popElements, resultado, tipo = ConDisJunction(expresion, "v")
#Por medio de la siguiente linea se usan los valores retornados de la funcion de la
#conectiva y se insertan y eliminan los elementos necesarios de la expresion.
                expresion, popElements = insertResult(expresion, popElements, resultado, tipo)
                break
        if (expresion[i]=="=>"):
            if ( checkIfProced( expresion, simb ) ):
#Se manda a llamar a la funcion Conditional y regresa los valores necesarios para la evaluacionn de la expresion
                expresion, popElements, resultado, tipo = Conditional(expresion)
#Por medio de la siguiente linea se usan los valores retornados de la funcion de la
#conectiva y se insertan y eliminan los elementos necesarios de la expresion.
                expresion, popElements = insertResult(expresion, popElements, resultado, tipo)
                break
        if (expresion[i]=="<=>"):
            if ( checkIfProced( expresion, simb ) ):
#Se manda a llamar a la funcion Biconditional y regresa los valores necesarios para la evaluacionn de la expresion
                expresion, popElements, resultado, tipo = Biconditional(expresion)
#Por medio de la siguiente linea se usan los valores retornados de la funcion de la
#conectiva y se insertan y eliminan los elementos necesarios de la expresion.
                expresion, popElements = insertResult(expresion, popElements, resultado, tipo)
                break
#Mientras existan parentesis en los extremos se continuara evaluado la proposicion logica
    keepProcessing = verifyKeepProcessing(expresion,keepProcessing,simb)
#Imprime el resultado de la proposicion logica
print "\nEl resultado de la evaluacion de la proposicion logica es: " + str(expresion)



