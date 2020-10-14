#Este ônibus possui um sistema de controle de entrada e saída de passageiros para monitorar o número 
#de ocupantes que transporta e, assim, detectar quando há muitos.
#Em cada parada, a entrada e saída de passageiros são representadas por uma tupla composta por dois números inteiros.

#bus_stop = (in, out)
#A sucessão de paradas é representada por uma lista dessas tuplas.

#stops = [(in1, out1), (in2, out2), (in3, out3), (in4, out4)]

stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

#1. Calcule o número de paradas

print(len(stops))


#2. Atribua a uma variável uma lista cujos elementos são o número de passageiros em cada parada (entrada e saída)
# Cada item depende do item anterior na lista + entrada - saída.

inp = []
out = []
for i in stops:
    inp.append(i[0])
    out.append(i[1])

bus = []
acc = 0
for x in range (len(stops)):
    acc += (inp[x]-out[x])
    bus.append(acc)

#3. Encontre a ocupação máxima do ônibus
print(max(bus))
#4. Calcule a ocupação média. 

occ_mean = sum(bus)/len(bus)
print(occ_mean)

#E o desvio padrão.
print (bus)
calc_desvio = []
for d in range (len(stops)):
    quad = (bus[d]-occ_mean)**2
    calc_desvio.append(quad)

stdev = ((sum(calc_desvio)/len(calc_desvio))**0.5)
print (stdev)



