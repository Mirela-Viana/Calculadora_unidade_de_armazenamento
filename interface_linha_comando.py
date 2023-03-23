from todas_as_calculadoras import converterStringParaFloat, bitParaByte, byteParaBit, byteparakilobyte,Kilobyteparamegabyte, kylobyteParabyte, megabyteParakilobyte, MegabyteParagigabyte, GigabyteParaMegabyte, terabyteparapetabyte, petabyteParaterabyte 

print(' - escreva 1 para bitparaByte \n -Escreva 2 byteparabit')
funcEscolha = input ()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = byteParaBit (entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = byteparakilobyte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = kylobyteParabyte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 


elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = Kilobyteparamegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = megabyteParakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = MegabyteParagigabyte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = GigabyteParaMegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = terabyteparapetabyte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = petabyteParaterabyte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)






    
