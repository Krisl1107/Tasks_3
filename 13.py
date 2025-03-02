N=int(input())
C=int(input())
number=int(input())
page=(number-1)//(N*C)+1
column=(number-1)%(N*C)//N+1
line=(number-1)%(N*C)//C+1
print("Страница",page,"Стобец",column,"Сртока",line)
