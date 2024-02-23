print("Enter the Number of Elements in Array")
n=int(input())
print("Enter the Array")
l=list(map(int,input().split()))
print("Enter the Element you want to find")
ele=int(input())
print("The given Array is",l)
notfound=False
for i in range(0,len(l)):
    if(ele==l[i]):
        print("Element is present at index",i)
        break
    else:
        notfound==True   
