ATT=int(input())
COMS=int(input())
YDS=int(input())
TD=int(input())
INT=int(input())
rating_1=((COMS/ATT)-0.3)/0.2
rating_2=(YDS/ATT-3)/4
rating_3=(TD/ATT)/0.05
rating_4=(0.095-(INT/ATT))/0.04
raitig=(((rating_1+rating_2+rating_3+rating_4)*100)/6)
print(raitig)
