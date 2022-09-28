#Dicionário com a associação de caracteres para usar nas bases 2 à 16
Dic={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G'}

#O método para converter qualquer base para decimal é por meio de uma soma finita, onde cada parcela é um múltiplo de uma potência de mesma base
#Onde os algorismos de representação serão 0 a b-1

#Já método de conversão de decimal para qualquer base por meio do algoritmo de Euclides, onde haverá divisões sucessivas com o intuito de pegarmos
#Os quocientes e restos para montarmos esse número na nova base

#Função para converter os números de uma base X para decimal para então uma base Y, escolhidas pelo usuário
def ConversorBase(num1, bin,bout):
 
  #De qualquer Base para Decimal por meio do Polinômio
  v_conv=0                             
  for i in range(len(num1)):         #Por meio de um for iremos percorrer o número em questão (de trás para frente) para montar o polinômio. 
    for v_dicio in Dic:                 #Que será dessa forma: enquanto estivermos dentro do 'for v_dicio', ele irá percorrer o dicionário procurando por valores
      if Dic[v_dicio]== num1[::-1][i]:  #que estejam no número em questão, quando isso acontece ele irá multiplicar esse valor pela base elevada ao índice i 
            v_conv+= v_dicio * (bin ** i)   #que está no momento (que só irá mudar quando v_dicio for igual a um dos algorismos do numero em questão).
      dec1 = v_conv                         #E então irá somar com outros valores encontrados para então formar o valor em Decimal
  
  #De Decimal para qualquer base por meio do Algoritmo de Euclides
  if num1 == '0':                      
      BN = 0
  else:                                 #Enquanto o valor de conversão (v_conv) estiver maior que 0 (lembrando que ele era o valor em decimal do numero em questão)
      BN = ""                           #ele irá dividir pela base de destino para pegar o resto a fim de montar o novo valor.
      while v_conv > 0:                 #E o valor de conversão irá se alterar pegando a cada atualização o valor inteiro da divisão (quociente)  
          BN += Dic[v_conv % bout]          
          v_conv = int(v_conv / bout)
  res1= BN[::-1]


  #Resultados da Conversão do Número:
  print(" ")
  print("Resultado da Conversão do Numero:")
  print("Na Base ",base1," o valor era de:",numero1)
  print("Em Decimal eh:",dec1)
  print("O Numero na Base ",base2," tem valor de:",res1)
  print(" ")


def Soma(num1_dec,num2_dec,base):
  #Função soma que utiliza a mesma base da outra função, onde irá converter para Decimal, somar e então converter para a base escolhida
  v_conv=0
  for i in range(len(num1_dec)):
    for v_dicio in Dic:
      if Dic[v_dicio]== num1_dec[::-1][i]:    
            v_conv+= v_dicio * (base ** i)
      dec1 = v_conv
    
  v_conv=0
  for i in range(len(num2_dec)):
    for v_dicio in Dic:
      if Dic[v_dicio]== num2_dec[::-1][i]:    
            v_conv+= v_dicio * (base ** i)
      dec2 = v_conv
  soma = dec1+dec2
  
  
  if soma == '0':
      BN = 0
  else:
      BN = ""
      while soma > 0:
          BN += Dic[soma % base]          
          soma = int(soma / base)
  res= BN[::-1]
  #Resultados da Soma dos Números:
  print("O valor em Decimal do 1º Num eh: ", dec1)
  print("O valor em Decimal do 2º Num eh: ", dec2)
  print("O Resultado da Soma na base", base, "é igual a:", res)


def Prod(num1_dec,num2_dec,base):
  #Função Produto que utiliza a mesma base da outra função, onde irá converter para Decimal, multiplicar e então converter para a base escolhida
  v_conv=0
  for i in range(len(num1_dec)):
    for v_dicio in Dic:
      if Dic[v_dicio]== num1_dec[::-1][i]:    
            v_conv+= v_dicio * (base ** i)
      dec1 = v_conv
    
  v_conv=0
  for i in range(len(num2_dec)):
    for v_dicio in Dic:
      if Dic[v_dicio]== num2_dec[::-1][i]:   
            v_conv+= v_dicio * (base ** i)
      dec2 = v_conv
  prod = dec1*dec2
  
  
  if prod == '0':
      BN = 0
  else:
      BN = ""
      while prod > 0:
          BN += Dic[prod % base]          
          prod = int(prod / base)
  res= BN[::-1]
  #Resultados da Produto dos Números:
  print("O valor em Decimal do 1º Num eh: ", dec1)
  print("O valor em Decimal do 2º Num eh: ", dec2)
  print("O Resultado do Produto na base", base, "é igual a:", res)


#Valores dado pelo usuário
print("Olá, qual operação deseja fazer?")
print("1 para Conversão de Bases")
print("2 para Soma na Base Escolhida")
print("3 para Produto na Base Escolhida")
esc=int(input(""))

if esc == 1: 
  numero1=input("Digite o Numero que sera convertido: ")
  base1=int(input("Qual eh a base original: "))
  base2=int(input("E agora para qual base ele ira: "))
  #Chamada da função que converte qualquer base para decimal e depois converte para qualquer base
  ConversorBase(numero1,base1,base2)
elif esc == 2: 
  numero1=input("Digite o Numero 1:")
  numero2=input("Digite o Numero 2:")
  base1=int(input("Qual eh a base:"))  
  #Chamada da função que soma dois valores na mesma base (convertendo para decimal, somando e depois convertendo para a base escolhida)
  Soma(numero1, numero2, base1)
else: 
  numero1=input("Digite o Numero 1:")
  numero2=input("Digite o Numero 2:")
  base1=int(input("Qual eh a base:")) 
  #Chamada da função que multiplica dois valores na mesma base (convertendo para decimal, somando e depois convertendo para a base escolhida)
  Prod(numero1, numero2, base1)
