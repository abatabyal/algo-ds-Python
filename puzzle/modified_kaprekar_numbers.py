def kaprekarNumbers(p, q):
    valid_range = False
    for i in range(p,q+1):
        test_number = i
        number_string = str(i)
        d = len(number_string)
        square_test_number = test_number ** 2
        square_test_number_string = str(square_test_number)
        if len(square_test_number_string) > 1:
            r = int(square_test_number_string[-d:])
            if r == 0 or len(square_test_number_string) % 2 != 0:
                l = int(square_test_number_string[:d-1])
            else:
                l = int(square_test_number_string[:d])
            if l + r == test_number:
                print(i, end=" ")
                valid_range = True
        if len(square_test_number_string) == 1 and int(square_test_number_string) == i:
            print(i, end=" ")
            valid_range = True
    if not valid_range:
        print("INVALID RANGE")

kaprekarNumbers(1, 99999)
