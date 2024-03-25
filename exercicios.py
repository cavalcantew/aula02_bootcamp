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
# data = input("Digite uma data no formato dd/mm/aaaa: ")
# dia, mes, ano = data.split("/")
# print("Dia:", dia)
# print("Mes:", mes)
# print("Ano:", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# texto_1 = input("Digite o primeiro texto: ")
# texto_2 = input("Digite o segundo texto: ")
# concatena = texto_1 + texto_2
# print("O texto concatenado é:", concatena)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = input("Digite o valor booleano 1: ")
# valor2 = input("Digite o valor booleano 2: ")
# resultado_and = valor1 and valor2
# print("Resultado do AND é", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# valor1 = input("Digite o valor booleano 1: ")
# valor2 = input("Digite o valor booleano 2: ")
# resultado_or = valor1 or valor2
# print("Resultado do AND é", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor1 = input("Digite o valor booleano 1: ")
# resultado_not = not valor1
# print("Resultado do NOT é:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# valor1 = input("Digite o valor 1: ")
# valor2 = input("Digite o valor 2: ")
# resultado_igualdade = valor1 == valor2
# print("Resultado da igualdade é:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1 = input("Digite o valor 1: ")
# valor2 = input("Digite o valor 2: ")
# resultado_diferenca = valor1 != valor2
# print("Resultado da diferenca é:", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input("Digite em graus celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C é igual a {fahrenheit}°F")
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
# texto = input("Digite uma palavra ou frase: ")
# if isinstance(texto, str):
#     formatado = texto.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palindromo.")
#     else:
#         print("Não é um palindromo.")
# else:
#     print("Entrada inválida. Digite uma palavra ou frase.")

# 23: Calculadora Simples
# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operador = input("Digite o operador (+, -, *, ?):")

#     if operador == '+':
#         resultado = num1 + num2 
#     elif operador == '-':
#         resultado = num1 - num2
#     elif operador == '*':
#         resultado = num1 * num2
#     elif operador == '/' and num2 != 0:
#         resultado = num1 / num2
#     else:
#         print("Operador inválido ou divisão por zero.")
#     print("Resultado:", resultado)
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#             print("Positivo")
#     elif numero < 0:
#             print("Negativo")
#     else:
#           print("Zero")
#     if numero % 2 == 0:
#           print("Par")
#     else:
#           print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []

try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)     
except ValueError:
      print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
