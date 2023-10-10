num=int(input("Enter the number:"))
num1=num
nums=num1
product=1
is_ok=True

print("Multiplicative loop")
while is_ok:
    m_persis=0
    while num:
        c+=1
        m_persis+=1
        rem=num%10
        product=product*rem
        num//=10
        
    print(f"product:{product}")
    num=product
    
    product=1
    if len(str(num))==1:
        m_root=m_persis
        is_ok=False

print("Additive loop")
is_con=True
sum=0
while is_con:
    a_persis=0
    while num1:
       
        
        rem=num1%10
        sum=sum+rem
        num1//=10
        a_persis+=1
    print(f"sum:{sum}")
    num1=sum
    
    sum=0
    if len(str(num1))==1:
        a_root=a_persis
        is_con=False
print(f"For the integer:{nums}")
print(f"\t\tAdditivie Persistence:{a_root} ,Additive root:{num1}")
print(f"\t\tMultiplicative  Persistence:{m_root} ,Additive root:{num}")
