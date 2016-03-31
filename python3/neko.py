# coding: utf-8
# Here your code !
s=input()
c,a,t=s.count("c"),s.count("a"),s.count("t")
min=min(c,a,t)
max=max(c,a,t)
print(min)
print(max-c)
print(max-a)
print(max-t)