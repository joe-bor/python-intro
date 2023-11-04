'''
// --- Directions
// Write a program that console logs the numbers
// from 1 to n. But for multiples of three print
// “fizz” instead of the number and for the multiples
// of five print “buzz”. For numbers which are multiples
// of both three and five print “fizzbuzz”.
// --- Example
//   fizzBuzz(5);
//   1
//   2
//   fizz
//   4
//   buzz
'''

def FizzBuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0 and i % 5 == 0):
            print('fizzbuzz')
        elif (i % 3 == 0):
            print('fizz')
        elif (i % 5 == 0):
            print('buzz')
        else:
            print(i)
        
FizzBuzz(15)

'''
// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False
'''

def AnagramChecker(str1, str2):
    
    # turn lowercase / uppercase
    # iterate over the strings
    # create a frequency counter <char> : <count>
    # compare each key-value pair
        # return true if all the same
        
    string1 = str1.lower()
    string2 = str2.lower()
    
    counter1  =  {}
    counter2 = {}
    
    for item in string1:
        if item in counter1:
            counter1[item] += 1
        else:
            counter1[item] = 1
   
    for item in string2:
        if (item in counter2):
            counter2[item] += 1
        else:
            counter2[item] = 1
            
    print(counter1 == counter2)
    return counter1 == counter2
    
AnagramChecker("car", "rac")