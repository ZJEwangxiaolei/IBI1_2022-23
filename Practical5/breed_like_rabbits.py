#denifine the number of bottles，time and rabbits first
#rt represents total rabbit number
#r represents the growth each time
#output the total number of rabbits that will be born each generation 
#output the number of generations required to exceed 100 rabbits  
b=100
rt=2
t=1
r=2
while rt < b:
    r=rt
    rt=2*rt
    t=t+1
    print("the geration",t,"born",r)
print("total gerations",t )
print("total rabbit number",rt)
