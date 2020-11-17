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




def taxcomp(off_p1,filename,taxi,reba):
    """computation of the tax """
    print("")

    print(FRMT.format("Tax payable on inc.",taxi))
    print(FRMT.format("Rebate u/s 87A",reba))
    net_tax = taxi - reba#d3
    print(FRMT.format("Tax after Rebate ",net_tax))
    cess = net_tax * 0.04
    print(NUMFRMT.format("Health Education cess ",cess))
    total_tax = net_tax + cess
    print(FRMT.format("Total tax and cess ",total_tax))
    arrears = 0
    print(FRMT.format("Relif u/s 89",arrears))
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
    print(FRMT.format("Intrest u/s 234A ",interesta))

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
    print(FRMT.format("Intrest u/s 234B ",interestb))
    interestc = 0
    print(FRMT.format("Intrest u/s 234C ",interestc))
    interestf = 0
    print(FRMT.format("Intrest u/s 234F ",interestf))
    amt_payable = total_tax + interesta + interestb + interestc + interestf - arrears#d11
    print(FRMT.format("Total Tax is",amt_payable))
    tax_paid = adv_tax#d12
    print(FRMT.format("Tax Paid",tax_paid))
    if amt_payable >= tax_paid:#d11 >= d12
        more_pay = amt_payable - tax_paid#d13
        print(NUMFRMT.format("Amount Payable",more_pay))
    elif tax_paid > amt_payable:
        refund = tax_paid  - amt_payable
        print(NUMFRMT.format("Amount Refund",refund))
    return 0


def slabfind(off_p1,filename,age,income):
    """ finding the correct slab """
    if 0 < income <=250000:
        taxi,reba = slab_zero()
        taxcomp(off_p1,filename,taxi,reba)
    elif 250000 < income<=500000:
        taxi,reba = slab_one(age,income)
        taxcomp(off_p1,filename,taxi,reba)

    elif 500000 < income <=1000000:
        taxi,reba = slab_two(age,income)
        taxcomp(off_p1,filename,taxi,reba)

    elif 1000000 < income<=5000000:
        taxi,reba = slab_three(age,income)
        taxcomp(off_p1,filename,taxi,reba)
    return 0
