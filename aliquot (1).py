#python 3.7.1
n = int(input ("Enter a number"))
sum =1
for i in range (2, n):
  if(n%i==0):
    sum =sum+1
if (sum==n):
  print ("Perfect")
elif(sum>n):
  print("Abundamt")
else:
  print("Deficient")