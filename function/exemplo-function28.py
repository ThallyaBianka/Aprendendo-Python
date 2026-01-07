def funcaoExemplo(titulo, *args, **kwargs):
  print("Título:", titulo)
  print("Argumentos posicionais:", args)
  print("Argumentos de palavra-chave:", kwargs)

funcaoExemplo("Informação do usuário:", "Emil", "Tobias", idade = 25, cidade = "Oslo") 