def dicionario(nome, sobrenome):
  print("Olá", nome, sobrenome)

pessoa = {"nome": "Emil", "sobrenome": "Refsnes"}
dicionario(**pessoa)