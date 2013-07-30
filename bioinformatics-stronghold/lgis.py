
n = 5
str = "5 1 4 2 3"
strarr = str.split(" ")

digits = []
lastindex = 0

for i in range(len(strarr)):
    digit = int(strarr[i])
    if digit == 1:


    if digit > digits[len(digits)] and (i - lastindex) < digit:
        digits.append(digit)
        lastindex = i

print(digits)