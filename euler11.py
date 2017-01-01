# "This is my solution for Problem 11 of Project Euler." - Sumedh Garimella
print("Now calculating the largest product of 4 adjacent numbers in the given grid...")
grid = [(8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8), #20x20 array
        (49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00),
        (81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65),
        (52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91),
        (22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80),
        (24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50),
        (32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70),
        (67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21),
        (24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72),
        (21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95),
        (78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92),
        (16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57),
        (86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58),
        (19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40),
        (4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66),
        (88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69),
        (4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36),
        (20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16),
        (20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54),
        (1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48)]
i = 0 #index for searching for products
max = 0 #rolling counter of max product
m1 = 0 #first number of max product
m2 = 0 #second number of max product
m3 = 0 #third number of max product
m4 = 0 #fourth number of max product
x = 0 #x
i = 0 #y
while i < 17: #VERTICAL SEARCH
    while x < 20:
        v1 = grid[i][x] #1
        v2 = grid[i + 1][x] #2
        v3 = grid[i + 2][x] #3
        v4 = grid[i + 3][x] #4
        v = v1 * v2 * v3 * v4 #product
        if v > max: #check for max
            m1 = v1
            m2 = v2
            m3 = v3
            m4 = v4
            max = v
            print(m1, m2, m3, m4, max, i+1, x+1, "vertical")
        x += 1 #iterate
    i += 1 #iterate
    x = 0 #reset x to 0, reset cycle
i = 0 #restart for next search
while i < 20: #HORIZONTAL SEARCH
    while x < 17:
        h1 = grid[i][x]
        h2 = grid[i][x + 1]
        h3 = grid[i][x + 2]
        h4 = grid[i][x + 3]
        h = h1 * h2 * h3 * h4
        if h > max:
            m1 = h1
            m2 = h2
            m3 = h3
            m4 = h4
            max = h
            print(m1, m2, m3, m4, max, i+1, x+1, "horizontal")
        x += 1
    i += 1
    x = 0
i = 0
while i < 17: #DIAGONAL DOWNWARDS SEARCH
    while x < 17:
        d1 = grid[i][x]
        d2 = grid[i + 1][x + 1]
        d3 = grid[i + 2][x + 2]
        d4 = grid[i + 3][x + 3]
        d = d1 * d2 * d3 * d4
        if d > max:
            m1 = d1
            m2 = d2
            m3 = d3
            m4 = d4
            max = d
            print(m1, m2, m3, m4, i+1, x+1, "diagonal down")
        x += 1
    i += 1
    x = 0
i = 0
while i < 17: #DIAGONAL UPWARDS SEARCH
    while x < 17:
        g1 = grid[i][x]
        g2 = grid[i - 1][x + 1]
        g3 = grid[i - 2][x + 2]
        g4 = grid[i - 3][x + 3]
        g = g1 * g2 * g3 * g4
        if g > max:
            m1 = g1
            m2 = g2
            m3 = g3
            m4 = g4
            max = g
            print(m1, m2, m3, m4, i+1, x+1, "diagonal up")
        x += 1
    i += 1
    x = 0
i = 0
print(m1, m2, m3, m4, max) #print max product
