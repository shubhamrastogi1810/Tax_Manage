from datetime import datetime,date
frmt = '{:25}:{:}'
def Slab0(age,income):
	d1 = 0
	d2 = 0
	return d1,d2
 
def Slab1(age,income):
	if age> 18 and age <= 60:
		inc = income - 250000
		d1 = inc * 0.05
		if income > 250000 and income <= 300000:
			d2 = min(d1,2500)
		elif income > 300000 and income <= 500000:
			d2 = 2500

	elif age >=61 and age <=80: 
		inc = income - 250000
		if income > 250000 and income <=300000:
			d1 = 0
			d2 = min(2500,d1)

		elif income > 300000 and income <= 500000:
			d1 = inc * 0.05
			d2 = 2500
	else:
		d1 = 0
		d2 = 0
	return d1,d2




def Slab2(age,income):
	
	if age > 1 and age <= 60:
		inc = income - 500000
		d1 = (inc * 0.2) + 12500
		d2 = 0
	elif age>60 and age <=80:
		inc = income - 1000000
		d1 = (inc * 0.2) + 10000
		d2 = 0
	else:
		inc = income - 1000000
		d1 = (inc * 0.2)
		d2 = 0
	return d1,d2

def Slab3(age,income):
	if age>1 and age<=60:
		inc = income - 1000000
		d1 = (inc * 0.3) + 112500
		d2 = 0
	elif age>60 and age<=80:
		inc = income - 1000000
		d1 = (inc * 0.3) + 110000
		d2 = 0
	else:
		inc = income - 1000000
		d1 = (inc * 0.3) + 100000
		d2 = 0
	return d1,d2

	
numfrmt ='{:25}:{:.2f}'		

def taxcomp(off_p1,filename,d1,d2):
	
	print("")
	
	print(frmt.format("Tax payable on inc.",d1))
	print(frmt.format("Rebate u/s 87A",d2))
	d3 = d1 - d2
	print(frmt.format("Tax after Rebate ",d3))
	d4 = d3 * 0.04
	print(numfrmt.format("Health Education cess ",d4))
	d5 = d3 + d4
	print(frmt.format("Total tax and cess ",d5))
	d6 = 0
	print(frmt.format("Relif u/s 89",d6))
	f = open(filename,"r")
	f.seek(off_p1)
	b,a = f.readline().split(":")
	f1,f2 = f.readline().split(":")
	dat,mon,year =map(int, a.split("-"))
	x = date(year,mon,dat)#date_deposit
	y = date(2021,3,31)#date_termend
	z = date(2021,4,13)#today's date 	
	amt = d5
	adv_tax = int(f2.strip())
	if x <= y and  z <= y :
        	d7 = 0
	else:
		yrtm = ((x.year - y.year) * 12) + (x.month - y.month)
		if adv_tax >= amt:
			amt = 0
		else:
        		amt = (amt - adv_tax) // 100
		d7 = amt * yrtm
	print(frmt.format("Intrest u/s 234A ",d7))
	
	tax_liablity = d5 - adv_tax
	yrmt = ((z.year - y.year) * 12) + (z.month - y.month)
	
	if tax_liablity >= 10000:
		if adv_tax >= (0.9 * d5):
			d8 = 0
		else:
			if z <= y:
				d8 = 0
			else:
				amt = (tax_liablity)// 100 
				d8 = amt * yrmt
	else:
		d8 = 0

	f.close()
	print(frmt.format("Intrest u/s 234B ",d8))
	d9 = 0
	print(frmt.format("Intrest u/s 234C ",d9))
	d10 = 0
	print(frmt.format("Intrest u/s 234F ",d10))
	d11 = d5+ d7 + d8 + d9 + d10 - d6
	
	return d11


def slabfind(off_p1,filename,age,income):
	if income> 0 and income <=250000:
		d1,d2 = Slab0(age,income)
		a = taxcomp(off_p1,filename,d1,d2)	
	elif income>250000 and income<=500000:
		d1,d2 = Slab1(age,income)
		a = taxcomp(off_p1,filename,d1,d2)
		
	elif income>500000 and income <=1000000:
		d1,d2 = Slab2(age,income)
		a = taxcomp(off_p1,filename,d1,d2)
		
	elif income>1000000 and income<=5000000:
		d1,d2 = Slab3(age,income)
		a = taxcomp(off_p1,filename,d1,d2)
		
	else:
		a = "Invalid Input"
	return a

