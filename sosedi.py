# Naloga:
# https://putka-upm.acm.si/tasks/2014/2014_finale/sosedi
  
  
def stevilo_sosedov(prebivalci, lokacije, max_razdalja):
    '''Vrne število sosedskih parov, ki živijo na razdalji manj ali enako max_razdalja.'''
  
    lokacije.sort()
    sosedje = 0
    zadnji_sosed = 0
    for i in range(prebivalci - 1):
        y = lokacije[i]
        sosedje += zadnji_sosed - i
        for j in range(zadnji_sosed + 1, prebivalci):
            z = lokacije[j]
            razdalja = abs(y - z)
            if razdalja <= max_razdalja:
                sosedje += 1
                zadnji_sosed += 1
            else:
                break
    return sosedje
  
  
st_prebivalcev, najvecja_razdalja = input().split(' ')
st_prebivalcev = int(st_prebivalcev)
najvecja_razdalja = int(najvecja_razdalja)
  
hisne_stevilke = input()
hise = [int(i) for i in hisne_stevilke.split(' ')]
  
print(stevilo_sosedov(st_prebivalcev, hise, najvecja_razdalja))