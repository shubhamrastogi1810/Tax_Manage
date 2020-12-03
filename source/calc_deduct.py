"""this module calculates the deductions """

def deduct_amount(ofset,filename,agee):
    """calculate the total deduction amount """
    filevar = open(filename,"r")
    filevar.seek(ofset)
    deduct_val = {}
    item_val = []
    linecount =1#a
    for line in filevar:
        key,val = line.split(":")
        deduct_val[key] = val.strip()
        item_val.append(int(val.strip()))
        linecount+=1
        if linecount == 19:
            break

    filevar.close()
    new_val = []
    # 80c , 80 cc ,80ccd
    ccc = item_val[0] + item_val[1]+ item_val[2]
    new_val.append(min(150000,ccc))
    #80CCD(1)
    if item_val[2] == 0:
        new_val.append(min(50000,item_val[3]))
    #80CCD(2)
    ccd2 = item_val[4] * 0.1
    new_val.append(max(0,ccd2))
    #ccg
    ccg = item_val[5]*0.5
    new_val.append(min(50000,ccg))
    #80d
    new_val.append(min(100000,item_val[6]))
    #dd
    new_val.append(min(125000,item_val[7]))
    #ddb
    new_val.append(min(100000,item_val[8]))
    #80e
    new_val.append(item_val[9])
    #80ee
    new_val.append(min(50000,item_val[10]))
    #80g
    new_val.append(item_val[11])
    #80gg
    new_val.append(min(60000,item_val[12]))
    #80gga
    new_val.append(item_val[13])
    #80ggc
    new_val.append(item_val[14])
    #80TTA
    new_val.append(min(10000,item_val[15]))
    #80TTB
    if 60 <= agee < 80:
        new_val.append(min(50000,item_val[16]))
    else:
        new_val.append(0)
    #80u
    new_val.append(min(125000,item_val[17]))

    return sum(new_val)
