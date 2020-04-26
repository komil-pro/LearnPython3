def while1(a=11,b=3):
    while a>b:
        a-=b
    print("Otvet: ", a)

#while1()

def while2(a=10,b=3):
    kolichestvo=0
    while a>b:
        kolichestvo+=1
        a-=b
    print("Otvet: ",kolichestvo)

#while2()

def while3(a=10,b=3):
    i=0
    while a>b:
        i+=1
        a-=b
    print("Otvet: chastnoe =",i,", ostatok =",a)

#while3()

def while4(n=27):
    x=1
    while x<n:
        x*=3
        if x==n:
            return True        
        #print(i,x)
    return False

#print(while4())

def while5(n=16):
    k=0
    x=1
    while x<n:
        k+=1
        x*=2
    print("K =",k)

#while5()