lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))


for num in range(lower, upper + 1):
	
	l=len(str(num))
	temp=int(num)
	sum = 0
	while temp > 0:
		digit = temp % 10
		sum  = sum+digit ** l
		temp = temp/10
	if num == sum:
		print(num)
