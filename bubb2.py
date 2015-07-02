a=[input("Enter numbers")] 
for i in range(10)
list=a.split()
print list
x=[]
for i in list:
	t=int(i)
	x.append(t)
print (x)
length=len(x)
for k in range(length):
    for l in range(length-1):
        if x[l] > x[l+1]:
           x[l],x[l+1]=x[l+1],x[l]
print(x)
          
          

 



             
