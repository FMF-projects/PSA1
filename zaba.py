# Naloga:
# https://putka-upm.acm.si/tasks/2015/2015_1kolo/zaba

import sys
sys.setrecursionlimit(100000)
 
def skok(mesto, hitrost):
    """Koliko muh lahko največ poberemo, če smo na neko mesto prišli z
    določeno hitrostjo."""

    if mesto > n: # pristali smo v vodi
        return 0
    elif mesto + hitrost - 1 > n: #zagotovo bomo pristali v vodi
        return muhe[mesto-1]
    elif poti[mesto-k][hitrost-min_h] != -1:
        return poti[mesto-k][hitrost-min_h]
    else:
        if hitrost - 1 > 0:
            s1 = skok(mesto + hitrost - 1, hitrost - 1) 
        else:
            s1 = 0
 
        s2 = skok(mesto + hitrost, hitrost)
        s3 = skok(mesto + hitrost + 1, hitrost + 1)
 
        pojedina = muhe[mesto-1] + max(s1,s2,s3)
        poti[mesto-k][hitrost-min_h] = pojedina
        return pojedina
        

def min_hitrost(n,k):
    """Izračuna minimalno hitrost."""

    min_h = k
    lokvanj = k
    k -= 1
    while min_h-1 > 0 and lokvanj+k < n:
        lokvanj += k
        min_h -= 1
        k -= 1
    return min_h

def max_hitrost(n,k):
    """Izračuna max hitrost."""
    max_h = k
    lokvanj = k
    k += 1
    while max_h+1 < n and lokvanj+k < n:
        lokvanj += k
        max_h += 1
        k += 1
    return max_h
 
 
n, k = map(int, input().split(' '))
muhe = list(map(int, input().split(' ')))

min_h = min_hitrost(n,k)
max_h = max_hitrost(n,k)
M = max_h - min_h + 1
poti = [[-1]*M for i in range(n-k+1)] 

print(skok(k,k))



