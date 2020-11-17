""" display the details of the user """
FRMT = '{:25}:{:}'
def get_per_info(filename):
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
    lis = list(per_info.items())
    for key,val in lis:
        print(FRMT.format(key,val))
    return count



def salcalc(ofset,filename):#a,b
    """ display salary and house income """
    print("")
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
    item = list(per_sal.items())
    for key,val in item:
        print(FRMT.format(key,val))
    filevar.close()
    ofset += count
    return ofset

def deduct(ofset,filename):
    """ display deductions """
    print("")
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
    item = list(ded_sal.items())
    for key,val in item:
        print(FRMT.format(key,val))
    filevar.close()
    ofset += count

    return ofset



def get_bank_detail(ofset,filename):
    """ display bank details """
    print("")
    filevar = open(filename,"r")
    bank_detail ={}
    filevar.seek(ofset)
    for line in filevar:
        key,val = line.split(":")
        bank_detail[key] = val.strip()

    item = list(bank_detail.items())
    for key,val in item:
        print(FRMT.format(key,val))

    return 0
