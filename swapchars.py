str = 'chennai'
newStr = ''
for i in range(len(str)/2):
    newStr += str[i*2+1] + str[i*2]
if len(str)%2 != 0:
    newStr += str[-1]
print(newStr)
