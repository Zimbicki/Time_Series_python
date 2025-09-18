#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nome do Arquivo: ALFACE_ROXO.py
Autor: Kaique Zimbicki
Data: 2023-10-01
Descrição: Programa que informa o preço do alface roxo.
Licença: MIT
"""

# Importa os modulos se necessario 

# import sys

# Função principal do programa


# Garante que a função principal seja chamada quando o script for executado


# escolha uma forma de previsão p/ series temporais e implemente 
# receba uma lista Float  e a partir dessa lista traga uma previsão em periodos que o usuario
#escolher exemplo tres, cinco, sete 

# depois faça um docsthink

import time
from typing import List, Dict, Any

#a diferenca entre classe e funcao é que classe é um molde, uma estrutura que define um objeto, enquanto funcao é um bloco de codigo que realiza uma tarefa especifica

def prever_media(valores: List[float], periodos: int) -> List[float]:
    if not valores:
        raise ValueError("a lista de valores nao pode estar vazia")
    
    media = sum(valores) / len(valores)
    return [media] * periodos


if __name__ == "__main__":

    print("iniciando previsao de media")
    time.sleep(1)  # simulando processamento lento
    print("processamento concluido")

    dados_historicos = [7.5, 111.002, 1000.8, 1351.2, 3.141359]

    periodos_para_prever = int(input("digite o numero de periodos para prever 3 5 7 "))

    previsoes = prever_media(dados_historicos, periodos_para_prever)

    print("previsao para os proximos", periodos_para_prever, "periodos")

    for i, valor in enumerate(previsoes, start=1):
        print(f"periodo {i}: {valor:.2f}")

    print("previsao de media concluida")

    '''
    docstring think:
    import time para realizar pausas que simulam processamento
    from typing import List, Dict, Any para anotacoes de tipos
    def prever_media(valores: List[float], periodos: int) -> List[float]: define a funcao que calcula a media
    if not valores: verifica se a lista esta vazia e gera erro
    media = sum(valores) / len(valores) calcula a media dos valores
    return [media] * periodos retorna a media repetida para cada periodo solicitado

    '''
