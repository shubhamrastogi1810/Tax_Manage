""" This module should be run to calculate the tax of individual """
import user_info as ui
import calculate_salary as cs
import age
import slabs
import calc_deduct as cd

FRMT ='{:25}:{:}'

def showoutput(fname,filename):
    """This function will show the output we get from computation """
    print('\n\n',filename)
    ofsset = ui.get_per_info(fname)
    ofset = ui.salcalc(ofsset,fname)

    income = cs.incomecalc(ofsset,fname)
    off_d1= ui.deduct(ofset,fname)
    agee = age.agecal(fname)
    deduct_val = cd.deduct_amount(ofset,fname,agee)
    print(FRMT.format("Gross income is",income))
    ded = income - deduct_val
    print(FRMT.format("Income after deduction",ded))


    slabs.slabfind(off_d1,fname,agee,ded)

    ui.get_bank_detail(off_d1,fname)

    return 0

filevar = open("fileinfo.txt")

for i in filevar:

    FILE = "../cases/" + str(i.strip())
    showoutput(FILE,i)

filevar.close()
