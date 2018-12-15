counter = []

def valid(pto1,pto2):
	valid_pos = abs(pto2[1]-pto1[1])!=abs(pto2[0]-pto1[0])
	return valid_pos
	
def show(chosen):
	for x in range(0,len(chosen)):
		print('|',end='')
		for y in range(0,len(chosen)):
			c = [x,y]
			if c in chosen: print('Q',end='|')
			else: print(' ',end='|')
		print()
	print('\n')

def iter_queens(queens):
	for i in range(0,len(queens)-1):
		for k in range(queens.index(queens[i])+1,len(queens)):
			if valid(queens[i],queens[k])==False: return False
	return True
	
def variator(group,root,n):
	for sub in group:
		if len(sub)==n:
			queens = []
			for kss in range(0,n): queens.append([kss,sub[kss]])
			if iter_queens(queens)==True: show(queens); counter.append(0);
			
		else:
			for k in root:
				if k not in sub:
					toadd = []
					for p in sub: toadd.append(p)
					toadd.append(k)
					variator([toadd],root,n)

numberOfqueens = int(input('NxN'))
rows = []
root = []
for i in range(0,numberOfqueens):
	rows.append([i])
	root.append(i)
	
variator(rows,root,numberOfqueens)
print(len(counter))
