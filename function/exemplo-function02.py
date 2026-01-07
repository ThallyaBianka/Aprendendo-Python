v = "variável"

def globalDentroDaFunção():
    global v
    v = "função global"

globalDentroDaFunção()
print("Está é uma " + v)
print("Testing functions")