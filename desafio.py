CONSTANTE_BONUS = 1000

# 1 - Solicita ao usuario que digite o seu nome
nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("O nome não deve conter números.")
    exit()
elif len(nome_usuario) == 0:
    print("Voce nao digitou nada.")
    exit()
elif nome_usuario.isspace():
    print("Voce digitou espaco.")
    exit()
else:
    print("Nome valido: ", nome_usuario)

# 2 - Solicita ao usuuario que digite o valor do seu salario
# Converte a entrada para um numero de ponto flutuante

try: 
    salario_usuario = float(input("Digite seu salário: "))
    if salario_usuario < 0:
        print("Digite um valor maior do que 0")
        exit()
except ValueError:
    print("Entrada invalida para o salario, digite um numero")
    exit()

# 3 - Solicita ao usuario que digite o valor do bonus recebido
# Converte a entrada para um numero de ponto flutuante
try:
    bonus_usuario = float(input("Digite o seu bônus: "))
    if bonus_usuario < 0:
        print("Digite um valor maior do que 0")
        exit()
except ValueError:
    print("Entrada invalida para o salario, digite um numero")
    exit()

# 4 - Calcule o valor do bonus final
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5 - Imprime a mensagem personalizada incluindo o nome e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus}")

# Bonus: Quantos bugs e riscos voce consegue identificar nesse programa? 