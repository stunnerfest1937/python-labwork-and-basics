number_of_rows = int(input("Total number of rows: "))

row_number = 1

while row_number <= number_of_rows:
    number = 1

    while number <= row_number:
        if number % 3 == 0:
            print("*", end=" ")
        else:
            print(number, end=" ")

        number = number + 1

    print()
    row_number = row_number + 1