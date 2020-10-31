import user_info as ui
import calculate_salary as cs
import age
import slabs
import calc_deduct as cd

frmt ='{:25}:{:}'
numfrmt = '{:25}:{:.2f}'
def showoutput(a):
	print("\n\n",a)
	p1,fname = ui.get_per_info(a)	
	
	ofset,filename = ui.salcalc(p1,fname)
	print("")
	income = cs.incomecalc(p1,filename)
	off_p1,filename = ui.deduct(ofset,filename)
	agee = age.agecal(filename)
	deduct_val = cd.deduct_amount(ofset,filename,agee) 	
	print(frmt.format("Gross income is",income))
	ded = income - deduct_val
	print(frmt.format("Income after deduction",ded))	
	
	
	tax_payable = slabs.slabfind(off_p1,filename,agee,ded)
	print(numfrmt.format("Tax to Pay",tax_payable))
	
	ui.get_bank_detail(off_p1,filename)
	
	return 0

f = open("fileinfo.txt","r")
for i in f:
	a = showoutput(i.strip())
	
f.close()
