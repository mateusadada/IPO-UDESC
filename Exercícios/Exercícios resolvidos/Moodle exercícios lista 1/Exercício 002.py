# Receba a temperatura em Celsius de um usuário e converta para Fahrenheit, exibindo o resultado na tela

print('Bem vindo! Este programa converte a temperatura em celsius para fahrenheit.')

celsius = float(input('Digite a temperatura em celsius: '))
fahrenheit = (1.8 * celsius) + 32

print(f'\nA temperatura de {celsius:.1f}ºC é equivalente a {fahrenheit:.1f}ºF')
