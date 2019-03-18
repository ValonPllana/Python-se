def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def shb(n,x,p):
    return fact(n)/(fact(n-x)*fact(x)) * p**x * (1-p)**(n-x)

a = int(input("Jep shpejtesin e internetit (Mb/s): "))            #Shpejtesia e internetit
b = int(input("Shpejtesia qe shfrytezojn kompjuterat (kb/s): "))  #Shpejtesia qe shfrytezohet kur user eshte aktiv
c= int(input("Numri i kompjutereve: "))                           #Numri i kompjutereve
d= int(input("Perqindja e kohes te perdorimit: "))                #Perqindja e kohes aktive

e= int(a*1000/b)   #Numri i kompjutereve qe mund te jene aktiv njekohesisht pa pasur problem
f=d/100            #Perqindja e shprehur ne numer(duke perdorur internetin)

s=0
for i in range(e+1,c+1):
    s=s+shb(c,i,f)
print("Mundesia qe te ket probleme eshte: ",s)
