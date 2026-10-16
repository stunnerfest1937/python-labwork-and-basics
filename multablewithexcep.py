i = int(input("Enter the number: "))

if i != 0:
    h = 100 // i

    for j in range(1, h + 1):
        if j != 4:
            print(i * j)
else:
    print("Please enter a number other than 0.")
