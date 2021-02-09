def cmmdc(a,b):
    r=a%b
    print(r)
    if r==0:
        return b
    elif r==1:
        return 1
    return(b,r)
print(cmmdc(2016,16))