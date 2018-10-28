###########################################
# Palindrom check #
###########################################

# Returns True if the input is a palindrom. First of all the algorithm needs to
# check, that the word that is provided as an input is a string. After that all
# the characters are converted to lower cases in order to check whether the
# original string and the reversed string are both equal. Addtionally all the
# unnecessary whitespaces in the beginning or the end of the input string are
# removed. For reversing the string the slicing tool is used as following:
# string[start:end:step] Start and end are kept empty to consider the whole
# string and the last parameter step is set to -1 in order to go through each
# letter of the word from the end to the start.

def palindrom_check(word):
    """Check word for palindrom.

    Args:
        word: String that should be checked.

    Returns:
        boolean: True if the word is a palindrom and False if the word is no palindrom.

    Raises:
        error: If the type of the input is not equal to string.
    """
    if type(word) != str:
        print("Error: Please enter a string!")
    else:
        check = word.lower().strip()
        return check == check[::-1]
        
#print(palindrom_check("Anna"))


###########################################
# Palindromic sections of string #
###########################################

# Returns a list of palindromic sections within a string. First of all the
# algorithm needs to check, that the word that is provided as an input is a
# string. After that all the characters are converted to lower cases in order to
# to be able to check all sections of the word. Addtionally all the unnecessary
# whitespaces in the beginning or the end of the input string are removed. For
# reversing the string the slicing tool is used as following:
# string[start:end:step] Start and end are kept empty to consider the whole
# string and the last parameter step is set to -1 in order to go through each
# letter of the word from the end to the start. The sections of the word are
# generated by starting with the first letter and increasing the length of the
# word by one addtional letter until the end of the word is reached. For each
# interation the comparison with the reversed string is performed. After all
# sections starting with the first letter are checked the algorithm continues
# with the sections beginning with the second letter and so on. If a palindromic
# section is found, the section is added to a list.

def palindromic_sections(word):
    """Check for palindromic sections in a word.

    Args:
        word: String that should be checked.

    Returns: 
        list: List of palindronic sections within the provided string.

    Raises:
        error: If the type of the input is not equal to string.
    """
    if type(word) != str:
        print("Error: Please enter a string!")
    else:
        valid_sections = []
        check = word.lower().strip()
        for i in range(0, len(check)):
            for j in range(i+1, len(check)):
                section = check[i:j+1]
                if section == section[::-1]:
                    valid_sections.append(section)
        return valid_sections

#print(palindromic_sections("detartrated"))


###########################################
# Fibonacci sequence #
###########################################

# The aim of the algorith is to print out a list of fibonacci numbers, that are
# smaller than a provided number. First a check is performed whether the
# provided number is of the type integer and positive. Since 0 is not considered
# as a fibonacci number a list with the values [0, 1] is initialized. After that
# a while loop is entered, which adds up the last item and the item before that
# and appends this value to the list. The while loop is exited when the newly
# calculated fibonacci number is greater than the input number. In the last step
# the list is printed out starting with the second element in the list, because
# 0 is not included as a fibonacci number.

def fibonacci(number):
    """Prints out a list of Fibonacci numbers, which are smaller than the parameter number.

    Args:
        number: Fibonacci numbers smaller or equal to the input number are calculated.

    Returns:
        list: Prints out a list of Fibonacci numbers.

    Raises:
        error: If the type of the number is no integer and the number is smaller or equal 0. 
    """
    if type(number) != int or number <= 0:
        print("Error: Please enter an integer greater than 0!")
    else:
        fib_list = [0, 1]
        while fib_list[-1] <= number:
            fib_num = fib_list[-1] + fib_list[-2]
            if fib_num >= number:
                break
            fib_list.append(fib_num)
        print(fib_list[1:])

#fibonacci(1000)
    

###########################################
# Increasing number check #
###########################################

# First a check is performed whether a list is passed as an argument. If this is
# the case each element in the list is iterated and the first two elements are
# compared. As long as the second element is greater than the first element, the
# index of the list is increased by one and the next two elements are compared.
# If there is one comparison where the second item is smaller than the first
# item, the loop is exited and the boolean False is returned. However if the second
# element is always greater than the first element and the end of the list is
# reached, the function returns True.

def increase_check(input_list):
    """ Returns True if all the numbers in the provided input_list are increasing.

    Args:
        input_list: List of numbers.

    Returns:
        boolean: True if all numbers in the input_list are increasing.

    Error:
        Input error: Input is not a list.
        Type error: Elements in list have the wrong type for comparison.
    """
    if type(input_list) != list:
        return "Error: Please provide a list as an input!"
    
    try:
        for i in range(1, len(input_list)):
            if input_list[i] <= input_list[i-1]:
                return False
        return True
    except TypeError:
        return "Error: Element in list has wrong type for comparison!"

#print(increase_check([1, 3, 4, 5, 6, 8, 10, 14]))
#print(increase_check([1, 4, 5, 6, 8, 10, 9, 13]))
#print(increase_check(["a", "b", "c", "d", "e", "f"]))
#print(increase_check(["a", "b", "c", 8, "e", "f"]))
#print(increase_check(1))


###########################################
# Longest sequence of increasing numbers #
###########################################

def longest_seq(input_list):
    """ Prints out the longest sequence of increasing numbers

    Args:
        input_list: List of numbers.
    
    Returns:
        list: Longest list of increasing numbers
    
    Errors:
        Input error: Input is not a list.
        Type error: Elements in list have the wrong type for comparison.
    """

    if type(input_list) != list:
        return "Error: Please provide a list as an input!"
    
    try:
        seq = []

        for i in range(0, len(input_list)):
            if i==0:
                seq.append([input_list[i]])
            elif input_list[i] > seq[-1][-1]:
                seq[-1].append(input_list[i])
            else:
                seq.append([input_list[i]])

        longest_len = 0

        for i in seq:
            if len(i) > longest_len:
                longest_len = len(i)
                longest_list = i

        return longest_list

    except TypeError:
        return "Error: Element in list has wrong type for comparison!"


#print(longest_seq([1, 4, 5, -1, 0, 6, 8, 10, 9, 13]))
#print(longest_seq([1, "A", 5, -1, 0, 6, 8, 10, 9, 13]))


###########################################
# Anagram #
###########################################

# Define function with two input parameters string1 and string2 

# Check if the two input parameters have the type str. If not return a error
# message.
 
# Clean both strings by converting it to lowercases and remove
# unnecessary whitespaces.

# Compare string1 with the reversed string2

# Return True if they are equal and False if they are different

def anagram(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 'Error: Please provide two strings for comparison!'
    else:
        return string1.strip().lower() == string2.strip().lower()[::-1]

#print(anagram('anagram', 'margana'))
#print(anagram('anagrame', 'margana'))
#print(anagram('anagram', 1))


###########################################
# Calculate frequencies #
###########################################

# The algorithm takes a list as an input parameter. First it is checked, whether
# a list is provided. If that's not the case an error message is provided. A
# further check is performed whether all elements in the list is of the type
# string. A for loop is used to itereate over all elements in the list. The
# strings are converted to lowercases and unnecessary whitespaces are removed.
# For each word in the list it is checked whether the word is already included
# in the dictionary. If it is already included in the dict the counter of the
# element is increased by one. Else it is added to the dict and initialized with
# a value of 1. 

def frequencies(text):
    output = {}
    if type(text) != list:
        return "Error: Please provide a list of strings as an input!"
    try:
        for i in text:
            word = i.strip().lower()
            if word not in output:
                output[word] = 1
            else:
                output[word] += 1
        return output
    except:
        return "Error: Please use only use strings as an input!"

#print(frequencies(['hi', 'I', 'am', 'Alex', 'would', 'just', 'like', 'hi', 'say', 'hi']))
#print(frequencies(['hi', 'I', 'am', 'Alex', 'would', 1, 'like', 'hi', 'say', 'hi']))
#print(frequencies('test'))


###########################################
# Vigenere Cipher #
###########################################

class Cipher:
 
    def __init__(self, text):
        self.text = text
        self.encoded_text = None

    def encode(self, key):
        encoded_text = ""
        for i in range(0, len(self.text)):
            letter = self.text[i] 
            key_index = i % len(key)
            key_letter = key[key_index]
            en_letter = chr((ord(letter) + ord(key_letter)) % 128)
            encoded_text += en_letter
        self.encoded_text = encoded_text
        return encoded_text
    
    def decode(self, key):
        decoded_text = ""
        for i in range(0, len(self.encoded_text)):
            letter = self.encoded_text[i] 
            key_index = i % len(key)
            key_letter = key[key_index]
            de_letter = chr((ord(letter) - ord(key_letter)) % 128)
            decoded_text += de_letter
        return decoded_text

Test = Cipher("This text should be encoded!")
print(Test.encode(key="fjio!jf+"))
print(Test.decode(key="fjio!jf+"))

# Example with wrong key
print(Test.decode(key="jo$jif+"))
