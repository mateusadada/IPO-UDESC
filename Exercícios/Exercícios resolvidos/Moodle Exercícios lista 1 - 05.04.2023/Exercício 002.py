# Receba a temperatura em Celsius de um usuário e converta para Fahrenheit, exibindo o resultado na tela

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (1.8 * celsius) + 32

print(f'\nA temperatura de {celsius:.1f}ºC é equivalente a {fahrenheit:.1f}ºF')
