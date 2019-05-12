# Naloga:
# https://putka-upm.acm.si/tasks/2012/2012_3kolo/zakladi

import sys

def tarjan(graph):
    """Sprejme graf in vrne stevilo komponent ter seznam s številko komponente 
    za posamezno vozlisce."""

    n = len(graph)
    index_counter = 0
    stack = []
    in_stack = [False]*n
    lowlinks = [n+1]*n
    index = [-1]*n
    result = []
    components = [-1]*n
    comp = 0

    def strongconnect(node):
        nonlocal index_counter
        nonlocal comp
        sys.setrecursionlimit(100000)

        index[node] = index_counter
        lowlinks[node] = index_counter
        index_counter += 1
        stack.append(node)
        in_stack[node] = True

        for v, w in graph[node]:
            if index[v] == -1:
                strongconnect(v)
                lowlinks[node] = min(lowlinks[node], lowlinks[v])
            elif in_stack[v]:
                lowlinks[node] = min(lowlinks[node], index[v])

        if lowlinks[node] == index[node]:
            #component = []
            while True:
                v = stack.pop()
                in_stack[v] = False
                #component.append(v)
                components[v] = comp
                if v == node: 
                    break
            #result.append(component)
            comp += 1

    for i in range(n):
        if index[i] == -1:
            strongconnect(i)

    #return result
    return (components, comp)


def konstruiraj_graf(povezave, n):
    """Prejme seznam povezav in njihovih vrednosti ter vrne utežen graf."""
    
    graf = [[] for i in range(n)]
    for povezava in povezave:
        a, b, c = povezava
        graf[a].append((b, c))
    return graf


def kvocientni_graf(komponente_vozlisc, st_komp, graf):
    """
    input: 
    komponente_vozlisc: seznam vozlisc in njihovih komponent
                        (npr: [4,2,5] vozlisce 0 se nahaja v 4 komponenti)
    st_komp: stevilo vseh komponent v grafu
    graf: seznam povezav v prvotnem grafu

    output:
    vrednosti_komponent: seznam cekinom, ki jih poberemo znotraj posamezne komponete
    povezave_komponent: seznam povezav med komponentami
    """

    povezave_komponent = [[] for i in range(st_komp)]
    vrednosti_komponent = [0] * st_komp

    for povezava in graf:
        a, b, c = povezava
        k1 = komponente_vozlisc[a]
        k2 = komponente_vozlisc[b]
        if k1 != k2:
            povezave_komponent[k1].append((k2, c))
        elif k1 == k2:
            vrednosti_komponent[k1] += c
    return (vrednosti_komponent, povezave_komponent)


def najboljsi_sosed(komponenta, st_komp, vrednosti, povezave):
    """Prejme komponento in vrne soseda, ki ima pod seboj največ cekinov"""

    sosedi = povezave[komponenta]
    st_sosed = len(sosedi)
    vrednosti_sosedov = [0] * st_sosed
    for i in range(st_sosed):
        sosed, c = sosedi[i]
        vrednosti_sosedov[i] += vrednosti[sosed]
        vrednosti_sosedov[i] += c
    return max(vrednosti_sosedov)


def vrednosti_komponent(st_komp, vrednosti, povezave):
    """Vrne zneske cekinov, ki jih lahko dosezemo iz posamezne komponente."""

    for i in range(st_komp):
        sosedi = povezave[i]
        if sosedi == []:
            continue
        else:
            vrednost = najboljsi_sosed(i, st_komp, vrednosti, povezave)
            vrednosti[i] += vrednost
    return vrednosti


def vrednosti_vozlisc(vrednosti_komponent, komponente, st_vozl):
    """Izpiše znesek cekinov, ki ga dobimo pri lovu na zaklad z začetkom 
    v posameznem vozliscu prvotnega grafa."""

    for vozlisce in range(st_vozl):
        print(vrednosti_komponent[komponente[vozlisce]])


def cekini(n,povezave):

    graf = konstruiraj_graf(povezave, n)
    komponente, st_komp = tarjan(graf)
    vrednosti, povezave_komponent = kvocientni_graf(komponente, st_komp, povezave)
    vrednosti_k = vrednosti_komponent(st_komp, vrednosti, povezave_komponent)
    vrednosti_vozlisc(vrednosti_k, komponente, n)


n, m = map(int, input().split(' '))
povezave = []
for i in range(m):
    a,b,c = map(int, input().split(' '))
    povezave.append((a-1,b-1,c))
cekini(n,povezave)       