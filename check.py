print("Enter the number")
a = int(input())

str = str(a)
print(str)
find = str(input("Enter the number you want to find : "))
count = 0
for i in range(0, len(str)):
    if find == str[i]:
        count = count + 1

print("Total Count is : ", count)



