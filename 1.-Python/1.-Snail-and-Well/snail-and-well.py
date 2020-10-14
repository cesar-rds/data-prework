import statistics
# O caracol e o poço
# Um caracol cai no fundo de um poço de 125 cm. Cada dia o caracol sobe 30 cm. 
# Mas à noite, durante o sono, desliza 20 cm porque as paredes estão molhadas. 
# Quantos dias o caracol leva para escapar do poço?
# Dica: O caracol sai do poço quando ultrapassa os 125cm de altura.
# Ferramentas
# Loop: enquanto
# Declarações condicionais: if-else
# Função: print ()
# Tarefas

# 1. Atribua os dados de desafio a variáveis ​​com nomes representativos: 
# well_height, daily_distance, nightly_distance e snail_position.

well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = 0
i = 0

while snail_position < well_height:
    snail_position += daily_distance - nightly_distance
    i += 1
print (f"Snail took {i} days to get out of the well")

# Bônus
# A distância percorrida pelo caracol a cada dia é agora definida por uma lista.
# No primeiro dia, o caracol sobe 30 cm, mas à noite desliza 20 cm. 
# No segundo dia, o caracol sobe 21cm, mas à noite desliza 20cm e assim sucessivamente.
# advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
# 1. Quantos dias o caracol leva para escapar do poço?

well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
snail_position = 0
distance_scr = []
i = 0

while snail_position < well_height:
    snail_position += advance_cm[i] - nightly_distance
    distance_scr.append(advance_cm[i] - nightly_distance)
    i += 1
print (f"Snail took {i} days to get out of the well")
media = snail_position/i

print (distance_scr)
# Siga as mesmas orientações do desafio anterior.
# Dica: Lembre-se que o caracol sai do poço quando ultrapassa os 125cm de altura.
# 2. Qual é o seu deslocamento máximo em um dia? E seu mínimo? 


desloc_max = max(advance_cm)-nightly_distance
desloc_min = min(advance_cm)-nightly_distance

print(f"Maximum distance of {desloc_max} and minimum of {desloc_min}")

# Calcule o deslocamento usando apenas a distância percorrida nos dias usados ​​para sair do poço.
# Dica: Lembre-se que deslocamento significa a distância total aumentada levando em consideração
# que o caracol desliza à noite.

# total_distance = snail_position + nightly_distance * i
# print(f"Snail scrolled {total_distance}")

# 3. Qual é o seu progresso médio? Leve em consideração os deslizamentos de caracol à noite.
print(f"Scrolled mean %.2f" %media)
# #or

calc_desvio = []
position = 0
for total in range(0, i):
    quad = (distance_scr[total]-media)**2
    calc_desvio.append(quad)
stdev = (sum(calc_desvio)/(len(calc_desvio)-1))**0.5
print (stdev)


