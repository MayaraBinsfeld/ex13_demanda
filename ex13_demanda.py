"""
Programa: 
Descrição: Este programa determina a quantidade demandada de um bem, a partir de seu preço, e da renda do consumidor.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""

# Alocação de memória
renda = 0
preco = 0

# Entrada de dados 
renda = float(input("Qual a renda do consumidor, em reais?"))
preco = float(input("Qual o preço do bem, em reais?"))

# Processamento de dados

q = (renda/preco)*100

# Saída de dados

print(f"A demanda deste bem é de {q}%.")