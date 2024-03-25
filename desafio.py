CONSTANTE_BONUS = 1000

# 1 - Solicita ao usuario que digite o seu nome
nome_usuario = input("Digite o seu nome: ")

# 2 - Solicita ao usuuario que digite o valor do seu salario
# Converte a entrada para um numero de ponto flutuante
salario_usuario = float(input("Digite seu salário: "))

# 3 - Solicita ao usuario que digite o valor do bonus recebido
# Converte a entrada para um numero de ponto flutuante
bonus_usuario = float(input("Digite o seu bônus: "))

# 4 - Calcule o valor do bonus final
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5 - Imprime a mensagem personalizada incluindo o nome e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus}")

# Bonus: Quantos bugs e riscos voce consegue identificar nesse programa? 