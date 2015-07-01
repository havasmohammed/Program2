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
for i in range(length):
    for j in range(length-1):
        if x[j] > x[j+1]:
           x[j],x[j+1]=x[j+1],x[j]
print(x)
          
          

 



             
