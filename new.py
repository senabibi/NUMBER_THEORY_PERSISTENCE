def multiplicative(num):
    r=0
    while len(str(num))!=1:
        m=1
        for i in range(len(str(num))):
            num=int(num)
            rem=num%10
            m*=rem
            num=num%10
            r+=1

        

def persistence(num)->int:
    num=int(num)
    if num<0:
        quit()
    else:
        multiplicative(num)    
persistence(input("please give me an integer (negative integer to quit):"))

