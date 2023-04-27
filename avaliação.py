print( 'Valor padrão de conversão: 1024')
valor1 = 1024 
Unidade1 = ['Bit', 'Byte', 'KB', 'MB', 'GB', 'TB', 'PB']
valorinicial = int(input('insira um valor:'))  

uni1 =(input(f'insira a unidade de armazenamento 1 {Unidade1}:'))
while not uni1 in Unidade1:
    uni1 = (input('insira a unidade de armazenamento 1:'))
uni2 = (input(f'insira a unidade de armazenamento 2 {Unidade1}:'))
while not uni2 in Unidade1:
    uni2 = (input('insira a unidade de armazenamento 2:'))

#interface
def calculo (valorinicial, uni1, uni2):
    valorFinal = valorinicial
    if(uni1 =='Bit'):
        valorFinal = valorFinal/8
        uni1 = 'Byte'

    if(Unidade1.index(uni1) > Unidade1.index(uni2)):
        for i in range(Unidade1.index(uni1), Unidade1.index(uni2)):
            valorFinal = valorFinal / valor1

        else:
            for i in range(Unidade1.index(uni1), Unidade1.index(uni2),-1):
                valorFinal = valorFinal * valor1
        if(uni2 == "Bit"):
            valorFinal = (valorFinal / valor1) * 8
    return print(valorFinal)

print('Resultado da conversão:')
calculo(valorinicial,uni1,uni2)






