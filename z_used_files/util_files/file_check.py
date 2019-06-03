import os
arr = os.listdir()
#print (arr)
n = 1000
for i in arr:
    if(i == 'file_check.py'):
        continue
    a,b = i.split('.')
    if n == int(a):
        n = n+1
    else:
        break
print(n)