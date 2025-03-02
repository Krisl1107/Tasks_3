x,y=map(int,input().split())
a=bool(x%y==0 or y%x==0)
print(int(a))
