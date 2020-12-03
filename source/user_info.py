""" display the details of the user """
FRMT = '{:25}:{:}'

def get_per_info(filename,fileout):
    """ display the personal info of the user """
    filevar = open(filename,"r")
    count = 0
    linecount = 1
    per_info ={}
    for i in filevar:
        count += len(i)
        key,val = i.split(":")
        per_info[key] = val.strip()
        linecount+=1
        if linecount == 13:
            break
    filevar.close()
    file_outvar = open(fileout,"a")
    lis = list(per_info.items())
    for key,val in lis:
        file_outvar.write(FRMT.format(key,val)+'\n')
    file_outvar.close()
    return count



def salcalc(ofset,filename,fileout):#a,b
    """ display salary and house income """
    file_outvar = open(fileout,"a")
    file_outvar.write("\n\n")
    per_sal = {}
    linecount = 1#d
    filevar = open(filename,"r")
    filevar.seek(ofset)
    count = 0
    for line in filevar:
        key,val = line.split(":")
        per_sal[key] = val.strip()
        linecount+=1
        count += len(line)
        if linecount == 13:
            break
    filevar.close()
    item = list(per_sal.items())

    for key,val in item:
        file_outvar.write(FRMT.format(key,val)+"\n")
    file_outvar.close()
    ofset += count
    return ofset

def deduct(ofset,filename,fileout):
    """ display deductions """
    file_outvar = open(fileout,"a")
    file_outvar.write("\n\n")
    ded_sal = {}
    linecount = 1
    filevar = open(filename,"r")
    filevar.seek(ofset)
    count = 0
    for line in filevar:
        key,val = line.split(":")
        ded_sal[key] = val.strip()
        linecount+=1
        count +=len(line)
        if linecount == 19:
            break
    filevar.close()
    item = list(ded_sal.items())

    for key,val in item:
        file_outvar.write(FRMT.format(key,val)+'\n')
    file_outvar.close()
    ofset += count

    return ofset



def get_bank_detail(ofset,filename,fileout):
    """ display bank details """
    file_outvar = open(fileout,"a")
    file_outvar.write("\n\n")
    filevar = open(filename,"r")
    bank_detail ={}
    filevar.seek(ofset)
    for line in filevar:
        key,val = line.split(":")
        bank_detail[key] = val.strip()
    filevar.close()
    item = list(bank_detail.items())
    for key,val in item:
        file_outvar.write(FRMT.format(key,val)+'\n')
    file_outvar.close()
    return 0
