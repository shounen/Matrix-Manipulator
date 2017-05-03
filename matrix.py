
# Enter() takes raw input and creates a list of lists, where each list inside
#		  has the same length. Each list represents a row, and the complete list
#		  forms a matrix.
# Enter(): Null -> matrix (list of lists)
def enter():									
    array = list()
    length = -1
    while True:
        inp = input()
        numbers = [float(n) for n in inp.split()]
        if inp == "":
            break
        if length == -1:
            length = len(numbers)
        elif length != len(numbers):
            raise IOError('Invalid Matrix.')
        array.append(numbers)
    if not array:
        return enter()    
    return array

# Transpose(a,n,m) takes an matrix with respective dimensions and returns
# 		a transpose of the matrix
# Transpose(a,n,m): matrix, int, int -> matrix (list of lists)
def transpose(array, n, m):
    newlist = list()
    for column in range(0, m):
        temp = list()
        for row in array:
            temp.append(row[column])
        newlist.append(temp)
    return newlist

# leading(r) takes a list and returns number of leading 0's
# leading(r): list -> int
def leading(row):
    count = 0
    for i in row:
        if i != 0:
            break
        else:
            count += 1
    return count

# reorder(a) takes a matrix and returns a sorted matrix based on
# 		number of leading 0s
# reorder(a): matrix -> matrix
def reorder(array):
    newarr = array
    order = list()
    for row in newarr:
        order.append(leading(row))
    group = zip(newarr, order)
    group = sorted(group, key=lambda leading: leading[1])
    unzip1, unzip2 = zip(*group)
    return list(unzip1)

# checkzero(r) determines if the input row is all zero
# checkzero: list -> bool
def checkzero(row):
    for i in row:
        if i != 0:
            return 0
    return 1

# divrow(r,n) divides all row elements by n
# divrow: list, num -> row
def divrow(row, n):
    newrow = list()
    for i in row:
        newrow.append(i/n)
    return newrow

# addrow(r1, r2, n) adds r1 + nr2 and returns the result.
# addrow: list, list, num -> list
def addrow(row1, row2, n):
	newrow = list()
	ind = 0
	for i in row1:
		newrow.append(i+(n*row2[ind]))
		ind += 1
	return newrow

# firstele(r) determines where the first nonzero element is in the row.
# firstele(r): list -> int
# returns -1 if it is a zero row
def firstele(row):
    count = 0
    for i in row:
        if i != 0:
            return count
        count += 1
    return -1

# redmat(a,r) reduces a matrix  by subtracting all rows except the given row
#   by a specified row until leading entries are 0
# restricts: specified row must have leading 1
# ie. all rows except specified one becomes row - (specified * d)
# redmat(a,r): matrix, int -> matrix
def redmat(array, rownum):
    newarr = list()
    row = array[rownum]
    count = 0
    for i in array:
        if count == rownum:
            newarr.append(i)
        else:
            if firstele(i) == -1:
                newarr.append(i)
            else:
                ele = i[firstele(row)]
                newarr.append(addrow(i, row, -1*ele))
        count += 1
    return newarr

# rref(a, n, m) takes array and dimensions and returns reduced row echelon form
# rref(a, n, m): matrix, int, int -> matrix
def rref(array, n, m):
    newarr = reorder(array)
    dim = min(n, m)
    count = 0
    for i in range(0, dim):
        print(count)
        row = newarr[count]
        ind = firstele(row)
        if ind == -1:
            count += 1
            continue
        else:
            newarr[count] = divrow(row, row[ind])
            newarr = redmat(newarr, count)
        count += 1
        newarr = reorder(newarr)
        for j in newarr:
            print(j)
    newarr = reorder(newarr)
    return newarr
        

# define program. Requires user input for matrix and commands. 
def main():
    print ("Enter your matrix.")
    newarr = enter()
    print ("Enter your command.")
    ret = list()
    n = len(newarr)
    m = len(newarr[0])
    while True:
        newinp = input()
        if newinp == "show":
            for i in newarr:
                print(i)
        elif newinp == "transpose":
            ret = transpose(newarr, n, m)
            newarr = ret
            temp = n
            n = m
            m = temp
            for k in newarr:
                print(k)
        elif newinp == "break":
            break
        elif newinp == "new":
            main()
            break
        elif newinp == "rref":
            temp = rref(newarr, n, m)
            for i in temp:
                print (i)
        elif newinp == "test":
            test = rref(newarr, n, m)
            print("break")
            for i in test:
                print(i)
        else:
            print("Invalid command.")
