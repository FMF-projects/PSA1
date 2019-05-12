# Naloga:
# https://putka-upm.acm.si/tasks/2016/2016_1kolo/go

def igra(poteze):
	"""Prejme seznam potez in izpiše stanje igre po zadnji potezi."""

	plosca = [['.'] * 19 for i in range(19)]
	barvi = ['B','W']
	barva = 1

	for poteza in poteze:
		x, y = poteza[0], poteza[1]
		if veljavna_poteza(plosca, x, y, barvi[barva-1]):
			plosca[y][x] = barvi[barva-1]

			(zajete, skupine) = zajete_skupine(plosca, x, y)
			if zajete: 
			# zajeli smo nasprotnikovo skupino, zato jo počistimo s plošče
				for skupina in skupine:
					pocisti(plosca, skupina)

			barva += 1
			barva %= 2
	prikazi(plosca)


def veljavna_poteza(plosca, x, y, barva):
	"""Preveri ali je poteza za barvo na (x,y) veljavna."""
	
	# preverimo, če je prostor prazen
	if plosca[y][x] != '.':
		return False

	# prostor je prazen, zanima nas še ali je poteza samomorilska
	# raziščemo komponento in preverimo ali je obkoljena z nasprotniko barvo
	obiskani = [[0] * 19 for i in range(19)]
	plosca[y][x] = barva
	if not samomorilska(plosca, x, y, obiskani):
		plosca[y][x] = '.'
		return True
	else:
		# še vedno je možnost da smo zajeli komponento nasprotnika
		(zajete, skupine) = zajete_skupine(plosca, x, y)
		plosca[y][x] = '.'
		if zajete:
			return True
		else:
			return False


def samomorilska(plosca, x, y, obiskani):
	"""Vrne True, če je poteza samomorilska in False sicer."""

	obiskani[y][x] = 1	
	barva = plosca[y][x]
	samomor = True
	for (z,w) in sosedi(x,y):
		if plosca[w][z] == '.':
			samomor = False
			break
		elif plosca[w][z] == barva and obiskani[w][z] == 0:
			samomor = samomor and samomorilska(plosca, z, w, obiskani)
	return samomor


def zajete_skupine(plosca, x, y):
	"""Preveri ali smo zajeli katero od nasprotnikovih skupin."""

	zajete = False
	skupine = []
	for (z,w) in sosedi(x,y):
		if plosca[w][z] == plosca[y][x]:
			continue  # pregledali bomo le nasprotnikove skupine

		obiskani = [[0] * 19 for i in range(19)]
		barva = plosca[y][x]
		samomor = samomorilska(plosca, z, w, obiskani)
		if samomor:
			zajete = True
			skupine.append(obiskani)
	return (zajete, skupine)


def sosedi(x, y):
	"""Vrne seznam sosedov (x,y)."""

	mozni_sosedi = [(x+1,y), (x-1,y), (x,y-1), (x,y+1)]
	sosedi = []
	for (z,w) in mozni_sosedi:
		if 0 <= z <= 18 and 0 <= w <= 18:
			sosedi.append((z,w))
	return sosedi


def prikazi(plosca):
	"""Izpiše vse vrstice igralne plošče."""

	for vrstica in plosca:
		print(''.join(vrstica))


def pocisti(plosca, komponenta):
	"""Počisti vsa polja iz komponente."""

	for x in range(19):
		for y in range(19):
			if komponenta[y][x] == 1:
				plosca[y][x] = '.'


poteze = []
for i in range(1000):
	try:
		poteza = input()
	except:
		break
	x, y = map(int, poteza.split(' '))
	poteze.append((x-1,y-1))
igra(poteze)