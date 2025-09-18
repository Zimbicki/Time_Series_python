# aqui fica toda a logica de negócio do sistema
# ou seja, o que o sistema realmente faz
# essa logica deve ser independente de qualquer framework
# ou seja, não deve ter nada de flask, fastapi, django, etc
# essa logica deve ser testavel de forma isolada
# ou seja, deve ser possivel testar essa logica sem rodar o servidor web
# ou seja, deve ser possivel testar essa logica sem depender de banco de dados
# ou seja, deve ser possivel testar essa logica sem depender de qualquer coisa externa
# para isso, use injeção de dependência
