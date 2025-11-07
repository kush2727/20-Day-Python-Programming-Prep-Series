n=5
for i in range(1,n+1,1):
  a=69
  for j in range(1,n-i+1+1,1):
    print(chr(a),end=" ")
    a-=1
  a=a-1
  print()