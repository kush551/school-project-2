num = int(input("Enter a number: "))
print("Factor of the number")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)