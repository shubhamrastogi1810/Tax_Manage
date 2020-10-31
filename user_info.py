frmt = '{:25}:{:}'
def get_per_info(filename):
        f = open(filename,"r")
        b=0
        a=1
	spac = "    "
        per_info ={}
        for i in f:
                b += len(i)
                key,val = i.split(":")
		per_info[key] = val.strip()
		
		a+=1
                if a == 13:
                        break
        f.close()
        lis = list(per_info.items())

        print()
        for key,val in lis:
		
                print(frmt.format(key,val))
        return b,filename

def salcalc(a,b):
        print("")
        Per_sal = {}
        d = 1
        f = open(b,"r")
        f.seek(a)
        c = 0
        for line in f:
                key,val = line.split(":")
                Per_sal[key] = val.strip()
                d+=1
                c = c + len(line)
                if d == 13:
                        break
        item = list(Per_sal.items())
        for key,val in item:
                print(frmt.format(key,val))
        f.close()
        a += c
        return a,b

def deduct(a,b):
        print("")
        ded_sal = {}
        d = 1
        f = open(b,"r")
        f.seek(a)
        c = 0
        for line in f:
                key,val = line.split(":")
                ded_sal[key] = val.strip()
                d+=1
                c = c + len(line)
                if d == 19:
                        break
        item = list(ded_sal.items())
        for key,val in item:
                print(frmt.format(key,val))
        f.close()
        a += c

        return a,b
        return a,b,item


def get_bank_detail(ofset,filename):
	print("")
	f = open(filename,"r")
	bank_detail ={}
	f.seek(ofset)	
	for line in f:
		key,val = line.split(":")
		bank_detail[key] = val.strip()

	item = list(bank_detail.items())
	for key,val in item:
		print(frmt.format(key,val))

	return 0
	
