#задача 1

n= int(input())
m=list(map(int,input().split()))
print (m)
k=0
for i in range (0,n-1):
    for j in range(i+1,n):
        if m[i]>m[j]:
            m[i],m[j]=m[j],m[i]
            print(m)
            k+=1
if k==0:
    print (0)
    
#задача 2

n= int(input())
num=[]
zen=[]
for i in range (n):
    a,b = map(int,input().split())
    num.append(a)
    num.append(b)
for i in range (0,n-1):
    for j in range (i+1,n):
        if zen[i]<zen[j] or zen[i]==zen[j] and num[i]>num[j]:
            zen[i],zen[j]=zen[j],zen[i]
            num[i],num[j]=num[j],num[i]
for i in range(n):
    print (num[i],zen[i])

#задача 3

def razd(mas):
    if len(mas)<2:
        return mas
    else:
        mid = len(mas)//2
        left = razd(mas[:mid])
        right = razd(mas[mid:])
        print (mid,mid-1,right[0],left[-1])
        return vstavk(left,right)
def vstavk(left,right):
    rez= []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            rez.append(left[i])
            i+=1
        else:
            rez.append(right[j])
            j+=1
    while i<len(left):
        rez.append(left[i])
        i+=1
    while j<len(right):
        rez.append(right[j])
        j+=1
    return rez
n= int(input())
m=[]
m= list(map(int,input().split()))
print(razd(m))

#задача 4

n= int(input())
m=[]
m=list(map(int,input().split()))
k=0
for i in range (0,n-1):
    for j in range (i+1,n):
        if m[i]>m[j] and i<j:
            k+=1
print (k)

#задача 5

n= int(input())
m=[]
m=list(map(int,input().split()))
a=set(m)
print (len(a))
