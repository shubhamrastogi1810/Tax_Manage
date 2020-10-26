import inf
import salcomp as sc
import age
import slabs

frmt ='{:25}:{:}'
def showoutput(a):
	print("\n\n",a)
	p1,fname = inf.get_per_info(a)	
	
	ofset,filename = inf.salcalc(p1,fname)
	print("")
	income = sc.incomecalc(p1,filename)
	ofset,filename,ite = inf.deduct(ofset,filename)	
	print(frmt.format("Taxable income is",income))
	
	agee = age.agecal()
	
	tax_payable = slabs.slabfind(agee,income)
	print(frmt.format("Tax to Pay",tax_payable))
	
	inf.get_bank_detail(ofset,filename)
	
	return 0

f = open("fileinfo.txt")
for i in f:
	a = showoutput(i.strip())
	
f.close()
