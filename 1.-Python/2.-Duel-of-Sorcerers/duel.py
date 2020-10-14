
POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}
gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']

saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

spells = 0
gandalf_wins = 0
saruman_wins = 0

gandalf_power = []
saruman_power = []

i = 0
while (gandalf_wins < 3) & (saruman_wins < 3) & (i < len(gandalf)) & (i < len(saruman)):
    if POWER[gandalf[i]] > POWER[saruman[i]]:
        gandalf_wins += 1
        saruman_wins = 0
    elif POWER[gandalf[i]] < POWER[saruman[i]]:
        saruman_wins += 1
        gandalf_wins = 0
    gandalf_power.append(POWER[gandalf[i]])
    saruman_power.append(POWER[saruman[i]])
    i += 1

if gandalf_wins == 3:
    print(f"Gandalf winner")
elif saruman_wins == 3:
    print(f"Saruman winner")
else:
    print(f"No have winner")
    

mean_g = sum(gandalf_power)/len(gandalf_power)
print (f"Average Gandalf {mean_g}")
mean_s = sum(saruman_power)/len(saruman_power)
print (f"Average Saruman {mean_s}")

desv_gan = []
desv_sar = []

for n in range (len(gandalf_power)):
    quad1 = (gandalf_power[n]-mean_g)**2
    quad2 = (saruman_power[n]-mean_s)**2
    desv_gan.append(quad1)
    desv_sar.append(quad2)
stdesv_gan = (sum(desv_gan)/(len(desv_gan)-1))**0.5
stdesv_sar = (sum(desv_sar)/(len(desv_sar)-1))**0.5

print(f"Standard deviation Gandalf %.2f" %stdesv_gan)
print(f"Standard deviation Saruman %.2f" %stdesv_sar)