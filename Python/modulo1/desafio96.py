'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

'''
def area(largura,comprimento):
    area = largura * comprimento
    print(f'{area}m2')
area(10,2)
