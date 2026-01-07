def funcaoKwargs(**explicacao):
    print("Com o kwargs você tem uma tupla, podendo mostrar somente um " + explicacao["definicao"])

funcaoKwargs(apenas = "somente",  artigo = "um", definicao = "elemento")
