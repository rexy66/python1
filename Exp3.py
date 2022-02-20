# Sum of each Row and Column of a Matrix in Python language

print ("-----Enter the number of rows & columns of the matrix-----")

# These are the matrix's dimension
x = int (input ())
y = int (input ())

a, sum = [], 0

print ("\n-----Enter the co-efficients of the matrix-----")
for i in range (x):
    a.append([])
    for j in range (y):
        a[i].append(int (input ()))

    print (end="\n")

# This statement will compute the
# sum of the matrix's rows elements
for i in range (x):
    for j in range (y):
        sum = sum + a[i][j]

    print ("The Sum of the ", i, " position row is = ", sum)
    sum = 0

print (end="\n")
sum = 0

# This statement will compute the
# sum of the matrix's columns elements
for j in range (y):
    for i in range (x):
        sum = sum + a[i][j]

    print ("The Sum of the ", j, " position column is = ", sum)
    sum = 0

                              
                              
                              
