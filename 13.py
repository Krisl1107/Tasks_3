N=int(input())
C=int(input())
number=int(input())
page=(number-1)//(N*C)+1
column=(number-(page-1)*N*C)//N+1
line=(number-(page-1)*N*C)-N*(column-1)
print("Страница",page,"Стобец",column,"Строка",line)

