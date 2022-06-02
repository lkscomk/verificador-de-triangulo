#esse codigo servira para usarmos o metodo .sqrt()
import math

#tres comandos de entrada para aramazenar os tres lados de um triangulo
catetoA = float(input('Digite o valor do primeiro cateto: ').replace(',', '.'))
catetoB = float(input('Digite o valor do segundo cateto: ').replace(',', '.'))
hipotenusaC = float(input('Digite o valor da hipotenusa: ').replace(',', '.'))

perimetro = catetoA + catetoB + hipotenusaC 
#o perimetro será feito do lado de fora da condição, pois o ele será o mesmo para todas os tipos de triangulos

#estrutura de condiçao - servira para verificarmos as diferentes classsificações de um triangulo equilátero, isóscele ou escaleno.
if (catetoA != catetoB) and (catetoB != hipotenusaC) and (catetoA != hipotenusaC):
  #todos os lados diferentes
  #qunado verificado a ocorrencia de um triangulo escaleno fazer o seguinte calculo para area;
  p = perimetro / 2
  area = math.sqrt(p * (p - catetoA) * (p - catetoB) * (p - hipotenusaC))

  #comando de saida concatenando as informações processadas
  print('Todos os lados são diferentes, portanto, trata-se de um triângulo escaleno tendo as seguindes caracteristicas: Área: {} cm² Perímetro: {}'.format(str(round(area,2)).replace('.', ',').replace('.', ','), str(perimetro)).replace('.', ','))

elif catetoA == catetoB == hipotenusaC:
  #todos os lados iguai
  #qunado verificado a ocorrencia de um triangulo equilátero fazer o seguinte calculo para area;
  area = (catetoA * catetoA * math.sqrt(3)) / 4
  print('Todos os lados são iguais, portanto, trata-se de um triângulo equilátero tendo as seguindes caracteristicas: Área: {} cm² Perímetro: {}'.format(str(round(area,2)).replace('.', ','), str(perimetro)).replace('.', ','))

else:
  #apenas dois lados sao iguais
  if catetoA == catetoB:
    base = hipotenusaC
    lado = catetoA
  elif catetoB == hipotenusaC:
    base = catetoA
    lado = hipotenusaC
  else:
    base = catetoB
    lado = hipotenusaC
  #qunado verificado a ocorrencia de um triangulo equilátero fazer o seguinte calculo para area;
  altura = math.sqrt((lado * lado) - ((base/2) * (base/2)))  
  area = (altura*base)/2

  #comando de saida concatenando as informações processadas
  print('Todos os lados são diferentes, portanto, trata-se de um triângulo isósceles tendo as seguindes caracteristicas: Área: {} cm² Perímetro: {}'.format(str(round(area,2)).replace('.', ','), str(perimetro)).replace('.', ','))
