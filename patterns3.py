def left_rhombus_pattern(n):
    for i in range(1, n + 1):
        print(" " * (i - 1) + "* " * n)

n = 5  
left_rhombus_pattern(n)

