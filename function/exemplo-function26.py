def pessoasDados(nomeDeUsuario, **detalhes):
    print("Nome de Usuário: " + nomeDeUsuario)
    print("Detalhes adicionais: ")
    for chave, valor in detalhes.items():
        print(" ", chave + ":", valor)

pessoasDados("emil123", idade = 25, cidade = "Oslo",  hobby = "Programar")
