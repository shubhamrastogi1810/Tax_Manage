import user_info as ui
import calculate_salary as cs
import age
import slabs

frmt ='{:25}:{:}'
def showoutput(a):
	print("\n\n",a)
	p1,fname = ui.get_per_info(a)	
	
	ofset,filename = ui.salcalc(p1,fname)
	print("")
	income = cs.incomecalc(p1,filename)
	ofset,filename,ite = ui.deduct(ofset,filename)	
	print(frmt.format("Taxable income is",income))
	
	agee = age.agecal(filename)
	
	tax_payable = slabs.slabfind(agee,income)
	print(frmt.format("Tax to Pay",tax_payable))
	
	ui.get_bank_detail(ofset,filename)
	
	return 0

f = open("fileinfo.txt")
for i in f:
	a = showoutput(i.strip())
	
f.close()
