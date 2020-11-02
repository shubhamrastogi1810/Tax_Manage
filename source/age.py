from datetime import datetime,date

def  agecal(filename):
        f = open(filename,"r")
        a=0
        b=0
        for i in f:
                if b == 2:
                        break
                a+=len(i)
                b+=1
        f.seek(a)
        b,a = f.readline().split(":")
        f.close()
        dat,mon,year =map(int, a.split("-"))
        d1 = datetime(year,mon,dat)
        d2 = date.today()
        age= (d2.year - d1.year) -((d1.month,d1.day)>(d2.month,d2.day))
        return age


