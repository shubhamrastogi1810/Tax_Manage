""" This module should be run to calculate the tax of individual """
import user_info as ui
import calculate_salary as cs
import age
import slabs
import calc_deduct as cd

FRMT ='{:25}:{:}'

def showoutput(fname,filename):
    """This function will show the output we get from computation """
    fileout = "../output/" + filename[:-3] +"out"
    out_open = open(fileout,"w")
    out_open.write(filename+'\n')
    out_open.close()
    ofsset = ui.get_per_info(fname,fileout)
    ofset = ui.salcalc(ofsset,fname,fileout)

    income = cs.incomecalc(ofsset,fname,fileout)
    off_d1= ui.deduct(ofset,fname,fileout)
    agee = age.agecal(fname)
    deduct_val = cd.deduct_amount(ofset,fname,agee)
    out_open = open(fileout,"a")
    out_open.write(FRMT.format("Gross income is",income)+'\n')

    ded = income - deduct_val

    out_open.write(FRMT.format("Income after deduction",ded)+'\n')
    out_open.close()

    slabs.slabfind(off_d1,fname,agee,ded,fileout)

    ui.get_bank_detail(off_d1,fname,fileout)

    return 0

filevar = open("fileinfo.txt")

for i in filevar:

    FILE = "../cases/" + str(i.strip())
    showoutput(FILE,i)

filevar.close()
