num = int(input("Enter a number: "))
flag=0
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
          flag=flag+1
if(flag==0):
	print("it is prime number")
else:
	print("not a prime number")
