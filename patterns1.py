def zero_one_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print((i + j) % 2, end=" ")
        print()

n = 4  
zero_one_triangle(n)
