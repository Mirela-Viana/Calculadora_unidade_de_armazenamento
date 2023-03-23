from todas_as_calculadoras import converterStringParaFloat, bitParaByte, ByteParabit
print(' - escreva 1 para bitparaByte \n -Escreva 2 byteparabit')
funcEscolha = input ()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = ByteParabit (entradaDoTecladoValorASerConvertido)
    print(valorConvertido) 

    
