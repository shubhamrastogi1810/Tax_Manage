""" this module will calculate the tax by finding the correct slabs. """
from datetime import date
FRMT = '{:25}:{:}'
NUMFRMT = '{:25}:{:.2f}'

def slab_zero():
    """ income < 2.5 lakh """
    tax_inc = 0
    rebate = 0
    return tax_inc,rebate

def slab_one(age,income):
    """ income >2.5 lakh and < 5lakh """
    if 18 < age <= 60:
        inc = income - 250000
        tax_inc = inc * 0.05
        if 250000 < income <= 300000:
            rebate = min(tax_inc,2500)
        elif 300000 < income <= 500000:
            rebate = 2500

    elif 61 <= age <=80:
        inc = income - 250000
        if 250000 < income <=300000:
            tax_inc = 0
            rebate = min(2500,tax_inc)

        elif 300000 < income <= 500000:
            tax_inc = inc * 0.05
            rebate = 2500
    else:
        tax_inc = 0
        rebate = 0
    return tax_inc,rebate


def slab_two(age,income):
    """ for income > 5 lakh and  < 10 lakh """
    if 18 <= age <= 60:
        inc = income - 500000
        tax_inc = (inc * 0.2) + 12500
        rebate = 0
    elif 60 < age <=80:
        inc = income - 1000000
        tax_inc = (inc * 0.2) + 10000
        rebate = 0
    else:
        inc = income - 1000000
        tax_inc = (inc * 0.2)
        rebate = 0
    return tax_inc,rebate

def slab_three(age,income):
    """ for inc > 10 lakh """
    if 18<=  age<=60:
        inc = income - 1000000
        tax_inc = (inc * 0.3) + 112500
        rebate = 0
    elif 60 < age<=80:
        inc = income - 1000000
        tax_inc = (inc * 0.3) + 110000
        rebate = 0
    else:
        inc = income - 1000000
        tax_inc = (inc * 0.3) + 100000
        rebate = 0
    return tax_inc,rebate




def taxcomp(off_p1,filename,taxi,reba,fileout):
    """computation of the tax """
    file_out = open(fileout,"a")
    file_out.write("\n\n")

    file_out.write(FRMT.format("Tax payable on inc.",taxi)+'\n')
    file_out.write(FRMT.format("Rebate u/s 87A",reba)+'\n')
    net_tax = taxi - reba#d3
    file_out.write(FRMT.format("Tax after Rebate ",net_tax)+'\n')
    cess = net_tax * 0.04
    file_out.write(NUMFRMT.format("Health Education cess ",cess)+'\n')
    total_tax = net_tax + cess
    file_out.write(FRMT.format("Total tax and cess ",total_tax)+'\n')
    arrears = 0
    file_out.write(FRMT.format("Relif u/s 89",arrears)+'\n')
    filevar = open(filename,"r")
    filevar.seek(off_p1)
    count = filevar.readline().split(":")
    filevar2 = filevar.readline().split(":")
    dat,mon,year =map(int, count[-1].split("-"))
    depositd = date(year,mon,dat)#date_deposit x
    termend = date(2021,3,31)#date_termend y
    datetoday = date.today()#today's date z
    amt = total_tax
    adv_tax = int(filevar2[-1].strip())
    if depositd <= termend and datetoday <= termend:
        interesta = 0
    else:
        if datetoday > termend:
            yrtm = abs(((datetoday.year - termend.year) * 12) + (datetoday.month - termend.month))
            if adv_tax >= amt:
                amt = 0
            else:
                amt = (amt - adv_tax) // 100
                interesta = amt * yrtm
        else:
            interesta = 0
    file_out.write(FRMT.format("Intrest u/s 234A ",interesta)+'\n')

    tax_liablity = total_tax - adv_tax
    yrmt = ((datetoday.year - termend.year) * 12) + (datetoday.month - termend.month)

    if tax_liablity >= 10000:
        if adv_tax >= (0.9 * total_tax):
            interestb = 0
        else:
            if datetoday <= termend:
                interestb = 0
            else:
                amt = (tax_liablity)// 100
                interestb = amt * yrmt
    else:
        interestb = 0

    filevar.close()
    file_out.write(FRMT.format("Intrest u/s 234B ",interestb)+'\n')
    interestc = 0
    file_out.write(FRMT.format("Intrest u/s 234C ",interestc)+'\n')
    interestf = 0
    file_out.write(FRMT.format("Intrest u/s 234F ",interestf)+'\n')
    amt_payable = total_tax + interesta + interestb + interestc + interestf - arrears#d11
    file_out.write(FRMT.format("Total Tax is",amt_payable)+'\n')
    tax_paid = adv_tax#d12
    file_out.write(FRMT.format("Tax Paid",tax_paid)+'\n')
    if amt_payable >= tax_paid:#d11 >= d12
        more_pay = amt_payable - tax_paid#d13
        file_out.write(NUMFRMT.format("Amount Payable",more_pay)+'\n')
    elif tax_paid > amt_payable:
        refund = tax_paid  - amt_payable
        file_out.write(NUMFRMT.format("Amount Refund",refund)+'\n')
    file_out.close()
    return 0


def slabfind(off_p1,filename,age,income,fileout):
    """ finding the correct slab """
    if 0 < income <=250000:
        taxi,reba = slab_zero()
        taxcomp(off_p1,filename,taxi,reba,fileout)
    elif 250000 < income<=500000:
        taxi,reba = slab_one(age,income)
        taxcomp(off_p1,filename,taxi,reba,fileout)

    elif 500000 < income <=1000000:
        taxi,reba = slab_two(age,income)
        taxcomp(off_p1,filename,taxi,reba,fileout)

    elif 1000000 < income<=5000000:
        taxi,reba = slab_three(age,income)
        taxcomp(off_p1,filename,taxi,reba,fileout)
    return 0
