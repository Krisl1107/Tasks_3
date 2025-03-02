import math
a=int(input())
b=int(input())
c=int(input())
angle_1=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
angle_2=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
angle_3=math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
print(angle_1,angle_2,angle_3,end="/n")
