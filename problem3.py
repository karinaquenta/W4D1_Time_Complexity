#input: array containing 'names'
#output: text or a string

#need an empty list
#need to use the length functionto see how many ppl like the item
#if no names = no one likes it
#if 1 name = return 'name' as string "likes this"
#if there are 2 names = return the first name "and" the 2nd name + "likes this"
#if there are 3 names = return all 3 names and "like this"
#if more than 3 names in the array = return the first 2 names "and" 3rd person name with "others like this"



def likes(names):
    n = (len(names))
    
   if n == 0: #Ο(1)
        return "no one likes this"
    elif n == 1: #Ο(1)
        return names[0] + " " + "likes this"
    elif n == 2: #Ο(1)
        return names[0] + " " + "and" + " " + names[1] + " " + "like this"
    elif n == 3: #Ο(1)
        return names[0] + "," + " " + names[1] + " " + "and" + " " + names[2] + " " + "like this"
    else:
        n == 4 #Ο(1)
        return names[0] + "," + " " + names[1] + " " + "and" + " " + str(n-2) + " others like this"


#Ο(1) Constant