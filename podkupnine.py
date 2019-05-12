# Naloga:
# https://putka-upm.acm.si/tasks/2011/2011_2kolo/podkupnine

def ostanek(birokrati, ponudniki, q, t):
	"""Seznamu podkupnin priredi polinom p in izpiše ostanek pri deljenju p(q) s t."""

	ost = 0
	for i in range(ponudniki):
		a, b, cekini = map(int, input().split(' '))
		vrsta = vsota_vrste(q, b-a+1, t)
		ost += ((vrsta * (cekini % t)) * hitro_potenciranje(q, a-1, t)) % t
		ost %= t
	print(int(ost))
	

def hitro_potenciranje(q, n, t):
	"""Izračuna n-to potenco q po modulu t."""

	rezultat = 1
	while n > 0:
		if n % 2 == 1:
			rezultat = (rezultat * q) % t
		n = n // 2
		q = (q * q) % t
	return rezultat


def vsota_vrste(q, n, t):
	"""Vrne vsoto geometrijske vrste do vključno n-tega člena po modulu t."""

	a = 1
	q = q % t
	vsota = 0
	while n > 0:
		if n % 2 == 1:
			vsota = (q * vsota + a) % t
		a = ((q + 1) * a) % t
		q = (q * q) % t
		n = n // 2
	return vsota


st_primerov = int(input())
for i in range(st_primerov):
	prazna = input()
	birokrati, ponudniki, q, t = map(int, input().split(' '))
	ostanek(birokrati, ponudniki, q, t)