
def magic_square(n):

    n = int(n)
    if n % 2 == 0:
        print("Magic square is not possible for even values of n.")
        return
    magic_square_list = []
    for i in range(n):
        new_list = []
        for j in range(n):
            new_list.append(0)
        magic_square_list.append(new_list)
    magic_sum = (n * ((n ** 2) + 1)) // 2
    num = n * n
    count = 1
    flag = 0
    k = n // 2
    l = n - 1
    while num >= count:
        if k == -1 and l == n:
            k, l = 0, n - 2
        else:
            if l == n:
                l = 0
            if k < 0:
                k = n - 1

        if magic_square_list[k][l] != 0:
            k, l = k + 1, l - 2
            continue
        else:
            magic_square_list[k][l] = count
            count += 1

        k = k - 1
        l = l + 1

    for j in range(n):
        column_sum = sum(magic_square_list[i][j] for i in range(n))
        if column_sum != magic_sum:
            flag = 1
    for i in range(n):
        row_sum = sum(magic_square_list[i][j] for j in range(n))
        if row_sum != magic_sum:
            flag = 1
    for j in range(n):
        diagonal_sum = sum(magic_square_list[i][n - i - 1] for i in range(n))
        if diagonal_sum != magic_sum:
            flag = 1
    print("columnSum: ", column_sum, "rowSum: ", row_sum, "diagonalSum :" ,diagonal_sum, "magicSum: ", magic_sum)

    if flag == 0:
        for i in range(n):
            for j in range(n):
                print(magic_square_list[i][j], end=" ")
            print()
    else:
        print("Magic Square is not possible")


number = input("Enter the number: ")
magic_square(number)