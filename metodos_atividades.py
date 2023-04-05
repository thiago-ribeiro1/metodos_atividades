#Crie um método que receba um valor em reais e converta a dólares

def converterEmDolares(reais):

    dolares = reais / 5.05
    dolares = round(dolares, 2)
    return dolares

valorReais = float(input('Digite o valor em reais: '))
resultado = converterEmDolares(valorReais)
print('O valor em dolares é: ', resultado, ' // Cotação do dólar: 5,05')
print()

#Crie um método que receba 2 parâmetros: um valor em reais e a moeda que deve ser convertida (dólares, euros ou peso argentino).
#E realize a conversão.

def converterMoeda(reais, moeda):
    moedas = {'dolar': 5.05, 'euro': 5.51, 'peso_argentino': 0.024}
    valor_moeda = moedas[moeda]
    moeda_convertida = reais / valor_moeda
    moeda_convertida = round(moeda_convertida, 2)
    resultado = converterMoeda(reais, moeda)
    return resultado

valorReais = float(input('Digite o valor em reais: '))
moeda_convertidaDolar = valorReais / 5.05
moeda_convertidaDolar = round(moeda_convertidaDolar, 2)
moeda_convertidaEuro = valorReais / 5.51
moeda_convertidaEuro = round(moeda_convertidaEuro, 2)
moeda_convertidaPesoArg = valorReais / 0.024
moeda_convertidaPesoArg = round(moeda_convertidaPesoArg, 2)
print('O valor convertido em dólares é: ', moeda_convertidaDolar, ' // Cotação do dólar: 5,05')
print('O valor convertido em euros é: ', moeda_convertidaEuro, ' // Cotação do euro: 5,51')
print('O valor convertido em pesos argentinos é: ', moeda_convertidaPesoArg, ' // Cotação de Pesos Argentinos: 0,024')
print()

#Crie um método que receba o valor do salario e indique a quantidade de imposto a ser
# pago (se ganhar até 2000, 12%. Acima de 2000,25%)

def imposto(salario):
    if salario <= 2000:
        porcentagem = 0.12
    else:
        porcentagem = 0.25
    imposto = salario * porcentagem
    impost = round(imposto, 2)
    return imposto

valorSalario = float(input('Digite o valor do salário: '))
resultado = imposto(valorSalario)
print("O valor do salário: ", valorSalario)

if valorSalario <= 2000:
    print("O valor do imposto a ser pago: ", resultado, ' // Imposto 12%')
else:
    print("O valor do imposto a ser pago: ", resultado, ' // Imposto 25%')
print()

#Crie um método que receba o valor em celsius e converta a farenheit

def converterCelsiusFah(celsius):

    fahrenheit = (1.8 * celsius) + 32
    fahrenheit = round(fahrenheit, 2)
    return fahrenheit


temperaturaCelsius = float(input('digite a temperatura em graus Celsius: '))
resultado = converterCelsiusFah(temperaturaCelsius)
print("A temperatura em graus Fahrenheit é: ", resultado)
print()

#Crie um método que receba as notas e retorne a média de notas do aluno

def mediaNotas(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
notas = [nota1, nota2]
resultado = mediaNotas(notas)
print('A média é: ', resultado)
print()

#Crie um método que receba as notas e retorne a maior nota do aluno

def maiorNota(notas):
    maiorNota = max(notas)
    return maiorNota

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
notas = [nota1, nota2]
resultado = maiorNota(notas)
print('A maior nota é: ', resultado)
