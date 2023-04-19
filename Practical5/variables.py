a=-3.19
b=-118.24
c=116.39
d=b-a
e=c-a

if d > e:
    print("Rob travelled further to Los Angeles than to Haining.")
elif d < e:
    print("Rob travelled further to Haining than to Los Angeles.")
else:
    print("Rob travelled the same distance to Los Angeles and Haining.")

X=True
Y=False
W=X and Y
Z=X or Y
print("W=",W)
print("Z=",Z)
#W= False and Z= True
