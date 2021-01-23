n = int(input("Enter the last number "))

for i in range(1, n+1, 1):
    if i % 3 == 0:
        continue
    print(i)
