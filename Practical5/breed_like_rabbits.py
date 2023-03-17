#denifine the number of bottles，time and rabbits first
b=100
#rt represents total rabbit number
rt=2
t=1
#r represents the growth each time
r=2
while rt < b:
    r=rt
    rt=2*rt
    t=t+1
 #output the total number of rabbits that will be born each generation  
    print("the geration",t,"born",r)
#output the number of generations required to exceed 100 rabbits       
print("total gerations",t )
print("total rabbit number",rt)
