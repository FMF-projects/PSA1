# Naloga:
# https://putka-upm.acm.si/tasks/2012/2012_1kolo/glasovanje

def pogodba(stranki):
    """Združi dve stranki in njune sodelavce."""
    
    a, b = stranki
    a = poisci_starsa(a)
    b = poisci_starsa(b)

    if a != b:
        if rang[a] < rang[b]:
            starsi[a] = b
            glasovi[b] = glasovi[a] # drugi se prilagaja prvemu
        else:
            starsi[b] = a
            if rang[a] == rang[b]:
                rang[a] += 1


def sprememba_glasovanja(stranke):
    """Mnenje ene izmed treh strank prilagodi mnenju ostalih dveh."""
    
    a,b,c = stranke
    a = poisci_starsa(a)
    b = poisci_starsa(b)
    c = poisci_starsa(c)
    A,B,C = glasovi[a], glasovi[b], glasovi[c]
    if A == B:
        glasovi[c] = A
    elif A == C:
        glasovi[b] = A
    else:
        glasovi[a] = B


def poisci_starsa(stranka):
    """Poišče starša stranke, katerega mnenje predstavlja trenutno mnenje stranke."""

    while stranka != starsi[stranka]:
            stranka = starsi[stranka]
    return stranka


def izpisi_glasove():
    """Izpiše skupno število glasov ZA in PROTI."""

    za = 0
    proti = 0
    for i in range(N):
        stars = poisci_starsa(i)
        glas = glasovi[stars]
        if glas == 1:
            za += clani[i]
        else:
            proti += clani[i]
    print(str(za) + ' ' + str(proti))


N, M = map(int, input().split(' '))
clani = list(map(int, input().split(' ')))
glasovi = list(map(int, input().split(' ')))
starsi = [i for i in range(N)]
rang = [0] * N
for i in range(M):
    sestanek = list(map(int, input().split()))
    st_strank = len(sestanek)

    for i in range(st_strank):
        sestanek[i] -= 1

    if st_strank == 2:
        pogodba(sestanek)
    else:
        sprememba_glasovanja(sestanek)
izpisi_glasove()