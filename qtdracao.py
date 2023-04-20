print ("Digite a quantidade, em gramas, por porção, que seu cachorro come:")
porcaoRacao = int (input())
print ("Insira a quantidade, em gramas, que ele come por dia:")
porcaoDia = int(input())
totalRacao = porcaoRacao * porcaoDia * 30
print (f"A quantidade total de ração consumida em um mês é {totalRacao}g")
