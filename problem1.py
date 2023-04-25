def sum_factorial(alist):
    output_sum = 0 #Ο(1)
    for i in alist: #O(n)
        factorial = 1 #start at 1 #Ο(1)
        for num in range(1, i + 1): #start at 1 #O(n)
            factorial *= num #Ο(1)
        output_sum += factorial #Ο(1)
    return output_sum

 #O(N^2) Quadratic 