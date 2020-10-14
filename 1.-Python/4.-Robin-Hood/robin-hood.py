# Robin Hood entrou em uma competição para vencer o concurso de tiro com arco em Sherwood. 
# Com seu arco e flechas, ele precisa atirar em um alvo e tentar acertar o mais próximo possível do centro.
# Neste desafio, a posição de aterrissagem das flechas disparadas pelos arqueiros na competição será representada 
# por meio de coordenadas bidimensionais.

# No espaço bidimensional, um ponto pode ser definido por um par de valores que correspondem 
# à coordenada horizontal (x) e à coordenada vertical (y). 
# Por exemplo, em nosso caso, uma flecha que atinge o centro do alvo do tiro com arco cairá na posição (0, 0) 
# nos eixos de coordenadas.

# O espaço pode ser dividido em 4 zonas (quadrantes): Q1, Q2, Q3, Q4. 
# Se um ponto está em Q1, ambas as coordenadas x e y são positivas. 
# Qualquer ponto com uma coordenada x ou y nula é considerado como não pertencente a nenhum quadrante.
# Você não precisa necessariamente usar todas as ferramentas. 
# Talvez você opte por usar alguns deles ou outros completamente diferentes, 
# eles são fornecidos para ajudá-lo a moldar o exercício. 
# Os exercícios de programação podem ser resolvidos de muitas maneiras diferentes.

# Estruturas de dados: listas, conjuntos, tuplas
# Declarações condicionais: if-elif-else
# Loop: enquanto / para
# Mínimo (classificação opcional)
# Robin Hood atingiu os seguintes pontos:


points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
(-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]


# 1. Robin Hood é famoso por acertar uma flecha com outra flecha. 
# Encontre as coordenadas dos pontos onde uma flecha atinge outra flecha.
# print(len(points))

    procura em uma coordenada x, e na proxima coordenada y.
for x in range(len(points)-1):
    for y in range(x+1, len(points)):
        if (points[x] == points[y]):
            print(points[x])

# 2. Calcule quantas flechas caíram em cada quadrante. 
# Nota : as setas que caem no eixo (x = 0 ou y = 0) não pertencem a nenhum quadrante.
x = []
y = []
for i in points:
    x.append(i[0])
    y.append(i[1])
print(x)
print(y)

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

for p in range (len(x)):
    if ((x[p] > 0) & (y[p] > 0)):
        Q1 += 1
    elif ((x[p] < 0) & (y[p]> 0)):
        Q2 += 1
    elif ((x[p] < 0) & (y[p]< 0)):
        Q3 += 1
    elif ((x[p] > 0) & (y[p] < 0)):
        Q4 += 1

# Q1x = >0
# Q1y = >0

# Q2x = <0
# Q2y = >0

# Q3x = <0
# Q3y = <0

# Q4x = >0
# Q4y = <0

# 3. Encontre o ponto mais próximo do centro. Calcule sua distância ao centro. 
# Leve em consideração que pode haver mais de um ponto a uma distância mínima do centro.
# Dica : use a distância euclidiana. Você pode encontrar mais informações sobre isso aqui .
# Dica : definir uma função que calcule a distância ao centro pode ajudar.

distance = []

for x in range(len(points)):
    distance.append(((0 - points[x][0])**2 + (0 - points[x][1])**2)**0.5)
near = min(distance)

for x in range(len(points)):
    if distance[x]==near:
        print(points[x])
        
        
# 4. Se o alvo do tiro com arco tiver um raio de 9, calcule o número de flechas que não acertarão o alvo. 
# Dica : use a função criada na etapa 3.
fault = 0
for x in range(len(points)):
    if((((0 - points[x][0])**2 + (0 - points[x][1])**2)**0.5) > 9):
        fault += 1
print (fault)
