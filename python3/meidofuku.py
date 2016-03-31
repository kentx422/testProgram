# coding: utf-8
# Here your code !
import datetime
n=int(input())
for i in range(n):
    tmp=60
    m=int(int(input())/3)
    tmp-=m
    if tmp < 0:
        tmp+=24*60
    hour=int(tmp/60)
    minu=tmp-hour*60
    h,m=str(hour),str(minu)
    if hour/10<1:
        h="0"+str(hour)
    if minu/10<1:
        m="0"+str(minu)
    print(h+":"+m)