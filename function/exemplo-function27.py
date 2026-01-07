def pessoasDados(**dados):
  print("Tipo:", type(dados))
  print("Nome:", dados["nome"])
  print("Idade:", dados["idade"])
  print("Todos os dados:", dados)

pessoasDados(nome = "Tobias", idade = 30, cidade = "Bergen") 