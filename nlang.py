"""
N Programming Language
Create by Nafis Handoko
at 16 August 2018
"""

#IMPORT ANY DESIRED LIBRARY
import sys,traceback,os
import marshal,imp,signal
from nkeyword import *
from keyword import *
from nexception import *
from stdlib import *

global isCompiler
isCompiler=1

#FUNCTION TO GET N SOURCE CODE FILE    
def getSource(ext):
    try:
        global arg
        arg=0
        for i in sys.argv[1:]:
            arg=i
        if arg==0:
            return arg
        elif arg.endswith(ext):
            nlang=open(arg,"r")
            nst=nlang.read()+' '
            return nst
        else:
            print('Error!:\nFormat File tidak didukung')
            raise SystemExit
    except:
        exc=sys.exc_info()
        if str(exc[0].__name__)=='IOError':
            print('Error!:\nFile tidak ditemukan!')
        elif str(exc[0].__name__)=='NameError':
            print('Sintaks:ncompiler namafile.n')
        raise SystemExit

#FUNCTION FOR CHECKING ANY IMPORTED LIBRARY
def libCheck(source):
    ar=[]
    st=''
    for i in source:
        if i=='\n':
            ar.append(st)
            st=''
        else:
            st+=i
    ar2=[]
    for i in ar:
        if 'Masukkan' in i:
            ar2.append(i.replace('Masukkan ',''))
    npath=sys.executable
    sys.path.append(os.getcwd())
    sys.path.append(npath.replace('nlang.exe','lib'))
    #libpath=os.listdir(npath.replace('nlang.exe','lib'))
    curpath=os.listdir(os.getcwd())
    for i in ar2:
        if i+'.n' in curpath:
            try:
                module=open(i+'.n','r')
                nsource=module.read()+' '
                codeObject=compile(parser(nsource),i,'exec')
                bytecode=marshal.dumps(codeObject)
                bytefile=open(i+'.pyc','wb')
                bytefile.write(imp.get_magic()+'\xf7\xeb\xae['+bytecode)
                bytefile.close()
                global isError
                isError=0
            except IOError,info:
                print('FATAL ERROR!:\nKesalahan Input Output')
                print('Kompilasi Dihentikan\n')
                if isCompiler==1:
                    raise SystemExit
                global isError
                isError=1
            except Exception,info:
                exc=sys.exc_info()
                #print(exc)
                #print(traceback.extract_tb(exc[-1]))
                errClass=npyerror[str(exc[0].__name__)]
                errLine=info[1][1]
                errFile=info[1][0]
                print(str('ERROR!:\n'+errClass+', File '+errFile+', Di baris '+str(errLine)))
                print('Kompilasi Dihentikan\n')
                if isCompiler==1:
                    raise SystemExit
                global isError
                isError=1
    
#FUNCTION FOR PARSING N SOURCE CODE
def parser(nst):
    pykwlist=kwlist+['None','True','False']
    st=''
    pyst=''
    quotes=0
    for i in range(0,len(nst)):
        st2=''
        if nst[i]=='"' or nst[i]=="'":quotes+=1
        if nst[i]==' ' or nst[i]=='\n' or nst[i]=='\t':
            st2=st
            st=''
            if quotes%2==0:
                signal=0
                for j in range(len(nkwlist)):
                    if st2==nkwlist[j]:
                        pyst+=pykwlist[j]+nst[i]
                        signal=1
                        break
                    elif st2=='Maka' or st2=='Lakukan' or st2=='Isinya':
                        pyst+=':'+nst[i]
                        signal=1
                        break
                if signal!=1:pyst+=st2+nst[i]
            else:
                pyst+=st2+nst[i]
        else:
            st+=nst[i]
    return pyst

#FUNCTION FOR EXECUTE PARSED CODE
def execute(pyst,fname):
    try:
        if isError==0:
            source=compile(pyst,fname,'exec')
            exec(source,globals())
        else:
            pass
            global isError
            isError=0
        
        '''
        data=marshal.dumps(source)
        bytefile=open(fname+'.pyc','wb')
        res=imp.get_magic()+'\xf7\xeb\xae['+data
        bytefile.write(res)
        bytefile.close()
        '''
    except Exception, info:
        exc=sys.exc_info()
        #print(str(exc[0].__name__))
        #print(exc)
        #print(traceback.extract_tb(exc[-1]))
        errClass=npyerror[str(exc[0].__name__)]
        try:
            errLine=info[1][1]
            errFile=info[1][0]
        except:
            errLine=traceback.extract_tb(exc[-1])[-1][1]
            errFile=traceback.extract_tb(exc[-1])[-1][0]
        print(str('ERROR!:\n'+errClass+', File '+errFile+', Di baris '+str(errLine)))
        print('Eksekusi Dihentikan\n')

#FUNCTION FOR N INTERACTIVE SHELL MODE
def nshell():
    ifKond='Jika' and 'Maka'
    forKond='Untuk' and 'Dalam' and 'Lakukan'
    defKond='Fungsi' and 'Isinya'
    tryKond='Coba' and 'Lakukan'
    print('N Programming Language')
    print('Copyright (c) 2018 Nafis Handoko\nAll Rights Reserved')
    while True:
        nIn=str(raw_input('>>> '))
        if (forKond in nIn) or (ifKond in nIn) or (defKond in nIn) or (tryKond in nIn):
            nIn2=''
            nIn2+=nIn+'\n'
            while True:
                nIn=str(raw_input('... '))
                if nIn=='':
                    libCheck(nIn2+'\n')
                    execute(parser(nIn2+' '),'<stdin>')
                    break
                else:
                    nIn2+=nIn+'\n'
        else:
            libCheck(nIn+'\n')
            execute(parser(nIn+' '),'<stdin>')

#THE MAIN FUNCTION
def main():
    source=getSource('.n')
    global isError
    isError=0
    if source==0:
        global isCompiler
        isCompiler=0
        nshell()
    else:
        global isCompiler
        isCompiler=1
        libCheck(source)
        execute(parser(source),arg)

#FUNCTION FOR HANDLING KEYBOARD INTERRUPT
def sigint_handler(signum,frame):
    sys.exit()
signal.signal(signal.SIGINT, sigint_handler)

#CALL THE MAIN FUNCTION WHEN PROGRAM EXECUTED
if __name__=='__main__':
    try:
        main()
    except:
        pass
    finally:
        if isCompiler==0:
            print('NSHELL DIHENTIKAN')
        else:
            pass
