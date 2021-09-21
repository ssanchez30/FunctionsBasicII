#1. Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 
# (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countDown(num):

    while num>=0:
        print(num)
        num=num-1

countDown(5)

print("********** end exercise 1 ************")

#2. Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def printReturn(arr):
    print(arr[0])
    return arr[1]

valorRetornado=printReturn([1,2])
print(valorRetornado)

print("********** end exercise 2 ************")

#3. First Plus Length - Create a function that accepts a list and returns the sum of the first value 
# in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlusLengh(arr):
    number = arr[0]+len(arr)
    return number

valorReturned = firstPlusLengh([1,2,3,4,5])
print(valorReturned)

print("********** end exercise 3 ************")

#4. Values Greater than Second - Write a function that accepts a list and creates a new list 
# containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements,
#  have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def greater(arr):
    
    if len(arr)<2:
        return False
    else:
        second=arr[1]
        newArr=[]

    i=0
    while i<len(arr):
        if arr[i]>second:
            newArr.append(arr[i])
        i=i+1    
                
    print(len(newArr))
    return newArr

valorDevuelto=greater([5,2,3,2,1,4])
#valorDevuelto=greater([3])
print(valorDevuelto)

print("********** end exercise 4 ************")

#5. This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def lenghtValue(numero1, numero2):
    newArreglo=[]
    for i in range(numero1):
        newArreglo.append(numero2)
    return newArreglo

arregloDevuelto = lenghtValue(6,2)
print(arregloDevuelto)

print("********** end exercise 5 ************")