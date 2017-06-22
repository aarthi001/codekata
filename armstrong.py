num=raw_input("enter the number")
sum = 0
temp = num

l=len(temp)
temp=int(temp)
while temp > 0:
  
   digit = temp % 10
   sum  = sum+digit ** l
   temp = temp/10
if num == str(sum):
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
