#N STANDARD LIBRARY
import sys
def Mutlak(x):
    if x<0:
        return x*-1
    elif x>=0:
        return x
def Semua(iterable):
    return all(iterable)
def Segala(iterable):
    return any(iterable)
def Biner(x):
    return bin(x)
def Kebenaran(x):
    return bool(x)
def Karakter(i):
    return chr(i)
def Perbandingan(x,y):
    return cmp(x,y)
def BilDesimal(x):
    return float(x)
def Bantuan(objects):
    return help(objects)
def BilHeksadesimal(x):
    return hex(x)
def Identitas(objects):
    return id(objects)
def BilBulat(x):
    return int(x)
def Panjang(s):
    count=0
    for i in s:
        count+=1
    return count
def BilOktadesimal(x):
    return oct(x)
def Ordinari(c):
    return ord(c)
def Jangkauan(stop):
    i=0
    nList=[]
    while i<stop:
        nList.append(i)
        i+=1
    return nList
def Jangkauan(start,stop,step=1):
    i=start
    nList=[]
    while i<stop:
        nList.append(i)
        i+=step
    return nList
"""
def Jangkauan(start,stop,step):
    return range(start,stop,step)
"""
def Sajak(objects):
    return str(objects)
def Tulis(objects,akhir='\n'):
    sys.stdout.write(str(objects)+str(akhir))
"""
def Input(x):
    return raw_input(x)
"""
def Baca(x=''):
    sys.stdout.write(str(x))
    In=sys.stdin.readline()
    In2=''
    for i in range(len(In)-1):
        In2+=In[i]
    return In2
