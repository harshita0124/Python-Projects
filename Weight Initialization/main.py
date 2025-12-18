import random
import math

#==========================================================================================================
while True:
    try:
        rows:int = int(input("Enter Number of rows : "))
        break
    except ValueError:
        print("Enter an Integer Value.")

while True:
    try:
        cols:int = int(input("Enter Number of columns : "))
        break
    except  ValueError:
        print("Enter an Integer Value.")

def zero_intialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all values are zero
       for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(0.0)
        matrix.append(row)

    return matrix
print(zero_intialization(rows, cols))

#==========================================================================================================

def random_uniform_initialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all elements are 
       drawn from uniform distribution for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(random.uniform(-1.0, 1.0))
        matrix.append(row)

    return matrix

print(random_uniform_initialization(rows, cols))


def random_normal_initialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all elements are 
       drawn from normal distribution for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(random.gauss(0, 1))
        matrix.append(row)

    return matrix

print(random_normal_initialization(rows, cols))

#==========================================================================================================

def xavier_uniform_initialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all elements are 
       drawn from uniform distribution for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(random.uniform(-math.sqrt(6 / (rows + cols)), math.sqrt(6 / (rows + cols))))
        matrix.append(row)

    return matrix

print(xavier_uniform_initialization(rows, cols))


def xavier_normal_initialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all elements are 
       drawn from normal distribution for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(random.gauss(0.0, math.sqrt(2 / (rows + cols))))
        matrix.append(row)

    return matrix

print(xavier_normal_initialization(rows, cols))

#==========================================================================================================

def he_uniform_initialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all elements are 
       drawn from uniform distribution for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(random.uniform(-math.sqrt(2 / (rows + cols)), math.sqrt(62 / (rows + cols))))
        matrix.append(row)

    return matrix

print(he_uniform_initialization(rows, cols))


def he_normal_initialization(rows:int, cols:int)->list:
    '''
       This function generates a matrix whose all elements are 
       drawn from normal distribution for weight initialization.
    '''
    matrix:List = []

    for i in range(rows):
        row:List = []
        for j in range(cols):
            row.append(random.gauss(0.0, math.sqrt(2 / (rows + cols))))
        matrix.append(row)

    return matrix

print(he_normal_initialization(rows, cols))

