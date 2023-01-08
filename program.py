x=input()
y=input()
if(y=='0'):
    print(-1)
else:
    l1=list(x)
    l2=list(y)
    numer=[]
    denomi=[]
    l3=l1.copy()
    l4=l2.copy()
    i=0
    j=0
    while(i<len(l1)):
        if(l1[i] in l4):
            l4.remove(l1[i])
            i+=1
        else:
            numer.append(l1[i])
            i+=1
    while(j<len(l2)):
        if(l2[j] in l3):
            l3.remove(l2[j])
            j+=1
        else:
            denomi.append(l2[j])
            j+=1
    print(numer,denomi)
    if(len(denomi)!=0 and int("".join(denomi))==0):
        print(-1)
    else:
        if(len(numer)==0 and len(denomi)!=0):
            m=1
            n=int("".join(denomi))
        elif(len(denomi)==0 and len(numer)!=0):
            n=1
            m=int("".join(numer))
        elif(len(denomi)==0 and len(numer)==0):
            m=1
            n=1
        else:
            m=int("".join(numer))
            n=int("".join(denomi))
        print(m/n)
