""" calculate the age of the user module """
from datetime import datetime,date

def agecal(filename):
    """calculate the age of the user """
    filevar = open(filename,"r")
    ofset=0#a
    linecount=0#b
    for i in filevar:
        if linecount == 2:
            break
        ofset+=len(i)
        linecount+=1
    filevar.seek(ofset)
    inp_date = filevar.readline().split(":")
    filevar.close()
    dat,mon,year =map(int, inp_date[-1].split("-"))
    birth = datetime(year,mon,dat)#d1
    nowd = date.today()#d2
    age = (nowd.year - birth.year) -((birth.month,birth.day)>(nowd.month,nowd.day))
    return age
