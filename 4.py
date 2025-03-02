x,y,n=map(int,input().split())
latte=(x*100+y)
revenue=n*latte
rub=revenue//100
kop=revenue%100
print(rub,"руб.",kop,"коп.")
