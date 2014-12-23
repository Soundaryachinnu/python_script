rel = ['F','L','A','M','E','S']

def funrel(rel):
	ch = 4
	for i,j in enumerate(rel):
		if i == ch and len(rel) >1:
			y = rel[i]
			rel.remove(y)
			print imd= int(i)+int(1)
			if rel[imd] != '':
				rel.insert(0,y)
	return rel

print funrel(rel)
