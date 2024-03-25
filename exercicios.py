import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_1 = int(input("Numero 1: "))
# numero_2 = int(input("Numero 2: "))
# soma = numero_1 + numero_2
# print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero_usuario = int(input("Digite um numero: "))
# div_resto = numero_usuario % 5
# print(f"O resto da divisao de {numero_usuario} por 5 é {div_resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num_1 = int(input("Digite o primeiro numero: "))
# num_2 = int(input("Digite o segundo numero: "))
# result = num_1 * num_2
# print("O resultado da multiplicação é:", result)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num_1 = int(input("Digite o primeiro numero: "))
# num_2 = int(input("Digite o segundo numero: "))
# try:
#     result = num_1 // num_2
#     print("O resultado da divisão inteira é:", result)
# except ZeroDivisionError:
#     print("Erro: divisão por zero não é permitida.")
#     exit()

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num = int(input("Digite um numero: "))
# resultado_quadrado = num ** 2
# print(f"O quadrado de {num} é:, {resultado_quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_1 = float(input("Numero 1: "))
# numero_2 = float(input("Numero 2: "))
# soma = numero_1 + numero_2
# print(soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_1 = float(input("Numero 1: "))
# numero_2 = float(input("Numero 2: "))
# media = (numero_1 + numero_2)/2
# print(f"A media entre {numero_1} e {numero_2} é: {media}" )

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
# potencia = base ** expoente
# print(f"O resultado da pontencia é: {potencia}" )

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite em graus celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o raio do circulo: "))
# area_circulo = math.pi * raio ** 2
# print(f"A area do circulo com raio de: {raio} é: {area_circulo}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = input("Digite um texto: ")
# texto_maisculo = texto.upper()
# print("Texto em maiúsculas:", texto_maisculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# texto = input("Digite seu nome completo: ")
# texto_minusculo = texto.lower()
# print("Nome em minúsculas:", texto_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# texto = input("Digite uma frase: ")
# frase = texto.strip()
# print("A frase sem espaços no inicio e no final é:", frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mes:", mes)
print("Ano:", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação