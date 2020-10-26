frmt ='{:25}:{:}'
def incomecalc(p1,fname):
	f = open(fname,"r")
	item =[]
	f.seek(p1)
	a=0
	
	for line in f:
		key,val = line.split(":")
		item.append(int(val.strip()))
		a+=1
		if a == 30:
			break	
	f.close()
	
	t_sal=0
	d_sal=0
	for i in range(0,3):
		t_sal = t_sal + item[i]
		n_sal = t_sal - item[3]
	print(frmt.format("Gross Salary",t_sal))
	print(frmt.format("Net Salary",n_sal))
	for i in range(4,7):
		d_sal = d_sal + item[i]
		b1=n_sal - d_sal
	print(frmt.format("Total Deduction",d_sal))
	print(frmt.format("Total Salary",b1))
	ren = item[7]
	print(frmt.format("rent received",ren))
	tp= item[8]
	b23 = ren - tp
	print(frmt.format("Annual value",b23))
	b24 = b23 * 0.3
	b2 = (b23 - b24 - item[9]) + item[10]
	print(frmt.format("Income Head of Sal",b2))
	b3 = item[11]
	print(frmt.format("Other sources Income",b3))
	b = b1 + b2 + b3
	print(frmt.format("Gross Total Income",b))
	c1=0
	for i in range(12,len(item)):
		c1=c1 + item[i]
		c2 = b - c1
	
	return c2
