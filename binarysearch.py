#Give input only as sorted array
def binarySearch(l,ele):
    sti=0
    edi=len(l)-1
    
    while sti<=edi:
        mid=(sti+edi)//2
        if l[mid]==ele:
            print("Element found at",mid)
            return mid
        elif(l[mid]<ele):
            sti=mid+1
        else:
            edi=mid-1
    return -1       
print("Enter the Number of Elements in Array")
n=int(input())
print("Enter the Array")
l=list(map(int,input().split()))
print("Enter the Element you want to find")
ele=int(input())
index=binarySearch(l,ele)
print(index)
            
    
        
            
    
        
    