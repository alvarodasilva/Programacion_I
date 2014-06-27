cadena= "programarconpython"
alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Simplificar(cadena):
    """En esta funcion saco las letras repetidas de una cadena dada, osea simplifica la cadena"""
    d = {}
    d["Ú"] = "U"
    d["Á"] = "A"
    d["É"] = "E"
    d["Í"] = "I"
    d["Ó"] = "O"
    d["Ñ"] = "N"
    d["Ü"] = "U"
    lista=list(cadena)
    resultado=[]
    for letra in lista:
        letra = letra.upper()
        if letra not in resultado:
            if letra in alfabeto:
                resultado.append(letra)
            elif letra in d:
                resultado.append(d[letra])
    return "".join(resultado)


def purificar(cadena):
    """Esta funcion las letras que contienen tilde las cambia por la misma letra pero sin tilde"""
    d = {}
    d["Ú"] = "U"
    d["Á"] = "A"
    d["É"] = "E"
    d["Í"] = "I"
    d["Ó"] = "O"
    d["Ñ"] = "N"
    d["Ü"] = "U"
    lista=list(cadena)
    resultado=[]
    for letra in lista:
        letra = letra.upper()
        if letra in alfabeto:
            resultado.append(letra)
        elif letra in d:
            resultado.append(d[letra])
    return "".join(resultado)

def generarDiccionario(cadena):
    """Esta funcion me denera un diccionario para el cifrado del texto o archivo"""
    d = {}
    clave = Simplificar (cadena + alfabeto)
    for i in range(len(alfabeto)):
        d[alfabeto[i]] = clave[i]
    return d

def generarDiccionario1(cadena):
    """Esta funcion me genera un diccionario para el desifrado del archivo o texto"""
    d = {}
    clave = Simplificar (cadena + alfabeto)
    for i in range(len(alfabeto)):
        d[clave[i]] = alfabeto[i]
    return d

def cifrarCadenas(d, cadenaParaCifrar):
    """Esta funcion me cifra el archivo, (ya purificado)"""
    cadenaParaCifrar = purificar(cadenaParaCifrar)
    lista=[]
    for i in range(len(cadenaParaCifrar)):
        if cadenaParaCifrar[i] in d:
            lista.append(d[cadenaParaCifrar[i]])
        else:
            print("error", cadenaParaCifrar[i])
    return "".join(lista)

def decifrarCadenas(clave, cadenaParaDecifrar):
    """Esta funcion me decifra el texto ya cifrado"""
    cadenaParaDecifrar = purificar(cadenaParaDecifrar)
    d = generarDiccionario1(clave)
    lista=[]
    for i in range(len(cadenaParaDecifrar)):
        if cadenaParaDecifrar[i] in d:
            lista.append(d[cadenaParaDecifrar[i]])
        else:
            print("error", cadenaParaDecifrar[i])
    return "".join(lista)


def AbrirCifrado(archivo=None, salida=None, clave=None):
    """En esta funcion me abre un archivo y me lo cifra"""
    dic = generarDiccionario(cadena)
    with open(salida,"w") as salida:
        with open(archivo) as entrada:
            for linea in entrada:
                salida.write(cifrarCadenas(dic, linea) + "\n")

def AbrirDesifrado(archivo=None,salida=None):
    """Esta funcion me abre el archivo Cifrado en la funcion anterior y luego me lo desifra y me lo decifra en otro archivo"""
    dic = generarDiccionario1(cadena)
    with open(salida,"w") as salida:
        with open(archivo) as entrada:
            for linea in entrada:
                salida.write(cifrarCadenas(dic, linea) + "\n")

def countLetters():
    """En esta funcion me cuenta la frecuencia de las letras que estan en el archivo, osea me cuenta la cantidad de ocurrencias de una misma letra en el archivo"""
    with open("obligatorio.txt") as programacion:
        diccionario={}
        for line in programacion:
            for letra in line:
                if letra.isalpha():
                    if letra in diccionario:
                        diccionario[letra]=diccionario[letra]+1
                    else:
                        diccionario[letra]=1
    return diccionario





cadena = input("ingrese la cadena a cifrar: ")
clave = input("ingrese la clave a usar: ")
d = generarDiccionario(clave)
cifrado = cifrarCadenas(d, cadena)
print("el resultado es: "+ cifrado)
e = generarDiccionario1(clave)
print(cifrarCadenas(e, cifrado))
AbrirCifrado("chantaje.txt","enblanco.txt",clave)
AbrirDesifrado("enblanco.txt","nuevo.txt")
print(countLetters())
