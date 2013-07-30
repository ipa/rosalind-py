__author__ = 'paoliw'


a = 100
b = 200
result = 0

for i in range(a,b+1):
    if i % 2 != 0:
        result += i

print (result)