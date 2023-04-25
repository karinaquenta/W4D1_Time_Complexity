def high_and_low(numbers):

    numbers = numbers.split()
    min = max = int(numbers[0])

    for x in numbers:
        x = int(x) #Ο(1) 
        if x > max: #Ο(1)
            max = x #Ο(1)
        elif x < min: #Ο(1)
            min = x #Ο(1)
    
    return ' '.join([str(x) for x in (max, min)])

#Ο(1) Constant