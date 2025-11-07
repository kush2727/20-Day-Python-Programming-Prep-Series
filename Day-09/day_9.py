
""" 41.Write a program to reverse a list without using reverse () or slicing."""

a=[1,2,3,4,5,62,23]
i=0
j=len(a)-1
while i<j:
    c=a[i]
    a[i]=a[j]
    a[j]=c
    i+=1
    j-=1
print(a)

"""42) Write a program to separate positive and negative numbers from a list into two different lists."""

a=[-1,-9,2,34,12,-10,23,21,-11,0]
pos=[]
neg=[]
zero=[]
for i in a:
  if i>0:
    pos.append(i)
  elif i<0:
    neg.append(i)
  else:
    zero.append(i)

print(pos)
print(neg)
print(zero)

"""43) Write a program to find the intersection of two lists (common elements) without using set ( )."""

a=[1,2,3,4,78,5]
b=[2,6,3,4,5]
store=[]
print("common elements: ")
for i in a:
  for j in b:
    if i==j:
      print(i,end=" ")

"""44) Write a program to sort a list in descending order manually (without using sort () or sorted ())."""

a=[1,23,2,24,101,3,34,56,2]
n=len(a)
for i in range(0,n-1+1,1):
    for j in range(0,n-2+1,1):
        if a[j]<a[j+1]:
            c=a[j]
            a[j]=a[j+1]
            a[j+1]=c
print(a)

"""45.Logical patterns"""
#1
n=5
for i in range(1,n+1,1):
  for j in range(1,i-1+1,1):
    print(" ",end=" ")
  for j in range(1,n-i+1+1,1):
    print(j,end=" ")
  for j in range(j-1,0,-1):
      print(j,end=" ")
  print()

#2
n=5
for i in range(1,n+1,1):
  a=1
  b=2
  for j in range(1,i+1,1):
    if i%2!=0:
      print(a,end=" ")
      a+=2
    else:
      print(b,end=" ")
      b+=2
  print()
    
#3
n=5
for i in range(1,n+1,1):
  for j in range(1,n+1,1):
    if i==j or i+j==n+1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
    
#4
n=5
for i in range(1,n+1,1):
  for j in range(1,n+1,1):
    if i==1 or j==1 or j==5 or i==5:
      print(1,end=" ")
    else:
      print(0,end=" ")
  print()

#5
n=7
for i in range(1,n+1,1):
  for j in range(1,n+1,1):
    if i==1 or j==1 or j==7 or i==7 or i==j or i+j==n+1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
