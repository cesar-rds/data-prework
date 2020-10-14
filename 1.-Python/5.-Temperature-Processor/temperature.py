temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

minimum = min(temperatures_C)
print(minimum)

# 2. Encontre a temperatura máxima do dia e armazene-a em uma variável.
maximum = max(temperatures_C)
print(maximum)

# 3. Crie uma lista com as temperaturas maiores ou iguais a 70ºC. Armazene-o em uma variável.
big = []
for i in range(len(temperatures_C)):
    if temperatures_C[i] >= 70:
        big.append(temperatures_C[i])
print(big)

# 4. Encontre a temperatura média do dia e armazene-a em uma variável. 

mean = sum(temperatures_C)/len(temperatures_C)
print(mean)

new_list = []
# for i in range(len(temperatures_C)):
#     new_list.append(temperatures_C[i])
#     if temperatures_C[i] == 0:
#         new_list.remove(temperatures_C[i])
#         mud = int((temperatures_C[(i-1)]+temperatures_C[(i+1)])/2)
#         new_list.append(mud)
# print(new_list)


temperatures_C.replace(0, int((temperatures_C[(i-1)]+temperatures_C[(i+1)])/2))



temperatures_F = []
for i in range(len(new_list)):
    temperatures_F.append((new_list[i] * 1.8) + 32)
print(temperatures_F)


decision = False
for i in range(len(new_list)):
    if decision == 0:
        if new_list[i] > 80:
            decision = True
        elif mean > 65:
            decision = True
        elif len(big) > 4:
            decision = True
        else:
            decision = False
            print("Exchange not required")
    elif decision == 1:
        print("Exchange required")
        break
# Bonus


# 1. Crie uma lista com as horas em que a temperatura é superior a 70ºC. Armazene-o em uma variável. 
hours_big = []
for i in range(len(temperatures_C)):
    if temperatures_C[i] > 70:
        hours_big.append(i)
print(hours_big)

# 2. Verifique se a lista que você criou na etapa 1 tem mais de 4 horas consecutivas.
hours_c = 0
for i in range(len(hours_big)):
    for x in range(1, len(hours_big)):
        if hours_big[i] - hours_big[x] == 1:
            hours_c += 1
        else:
            hours_c = 0
    if hours_c >= 4:
        print("The temperature is greater than 70ºC during more than 4 consecutive hours")


# 3. Tome a decisão! Para tomar sua decisão, verifique se alguma das três condições é atendida.
# Imprima uma mensagem para mostrar se o sistema de refrigeração precisa ser trocado ou não.
decision = False
for i in range(len(new_list)):
    if decision == 0:
        if (new_list[i] > 80) | (hours_c == 4):
            decision = True
        elif mean > 65:
            decision = True
        else:
            decision = False
    elif decision == 1:
        print("Exchange required")
        break
    else:
        print("Exchange not required")

# 4. Encontre o valor médio das listas de temperatura (ºC e ºF). Qual é a relação entre os dois valores médios? 
mean_C = sum(new_list)/len(new_list)
print(mean_C)

mean_F = sum(temperatures_F)/len(temperatures_F)
print(mean_F)

# 5. Encontre o desvio padrão das listas de temperatura (ºC e ºF). Qual é a relação entre os dois desvios padrão? 

# for x in range(len(new_list)):
#     new_list[x] = (new_list[x] - mean_C)**2
#     temperatures_F[x] = (temperatures_F[x] - mean_F)**2
    
# stdev_C = (sum(new_list)/(len(new_list)-1))**0.5
# stdev_F = (sum(temperatures_F)/(len(temperatures_F)-1))**0.5

# print(stdev_C)
# print(stdev_F)

calc_desvio_C = []
calc_desvio_F = []
for i in range(len(new_list)):
    quad_C = (new_list[i]-mean_C)**2
    quad_F = (temperatures_F[i]-mean_F)**2
    calc_desvio_C.append(quad_C)
    calc_desvio_F.append(quad_F)

stdev_C = ((sum(calc_desvio_C)/len(calc_desvio_C))**0.5)
stdev_F = ((sum(calc_desvio_F)/len(calc_desvio_F))**0.5)
print(stdev_C)
print(stdev_F)

