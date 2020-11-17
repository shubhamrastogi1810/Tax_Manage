""" calculate the taxable_inc of the  person under salary and house income """
FRMT='{:25}:{:}'
def incomecalc(ofset,filename):
    """ calculate the income from the house property and salary """
    filevar = open(filename,"r")
    item =[]
    filevar.seek(ofset)
    linecount=0#a

    for line in filevar:
        val = line.split(":")
        item.append(int(val[-1].strip()))
        linecount+=1
        if linecount == 30:
            break
    filevar.close()

    t_sal=0
    d_sal=0
    for i in range(0,3):
        t_sal = t_sal + item[i]
        n_sal = t_sal - item[3]
    print(FRMT.format("Gross Salary",t_sal))
    print(FRMT.format("Net Salary",n_sal))
    for i in range(4,7):
        d_sal = d_sal + item[i]
        net_sal=n_sal - d_sal#b1
    print(FRMT.format("Total Deduction",d_sal))

    print(FRMT.format("Inc. under head of Salary",net_sal))

    print(FRMT.format("Total Salary",net_sal))

    rent = item[7]
    print(FRMT.format("rent received",rent))
    tax_paid= item[8]
    annual = rent - tax_paid#b23
    print(FRMT.format("Annual value",annual))
    house_inc = annual * 0.3#b24
    nethouse_inc = (annual - house_inc - item[9]) + item[10]
    print(FRMT.format("Income Head of Tax_property",nethouse_inc))
    other_inc = item[11]#b3
    print(FRMT.format("Other sources Income",other_inc))
    gross_inc = net_sal + nethouse_inc + other_inc
    print(FRMT.format("Gross Total Income",gross_inc))

    return gross_inc
