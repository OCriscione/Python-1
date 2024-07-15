import unittest

### Olivia Criscione

### The file name should be renamed to your Student ID (001527562_pa1.py)
### Each question in section 1 is worth 1 point. 
### Each question in section 2 is worth 2 point. 
### Read the instructions and examples for each question. 
### The questions are separate, and the earlier results do not affect your ability to complete other question. 
### Do not modify the structure of the code.


### Start of HW1

input_list = [1, 3, 5, 7, 9, 14, 18, 21, 89, 99]
input_list2 = [2, 4, 7, 8, 9, 22, 77]
input_list3 = ['hello', 'hi', 'bye']
messy_list = [3, 1, 7, 5, 2, 9, 8]
nested_list = [[1,3,2],[6,4,5]]
nested_list2 = [[1,2,3],[4,5,6]]
old_list = [3,5,2,7,9,4,5]

# 1a Given a list, input_list, write a program that prints the length of the list using len().
# Inputs:
# input_list is a list.
# Output:
# The function should return the the_length with updated numeric value.
def q1a(input_list):
    the_length = len(input_list)
    return the_length

# 1b Do the same thing, without using len()
# Inputs:
# input_list is a list.
# Output:
# The function should return the the_length with updated numeric value.
def q1b(input_list):
    the_length = 0
    for _ in input_list:
        the_length += 1
    return the_length

# 1c Given a list, messy_list, write a program that sorts the elements in the list in ascending order. 
# Inputs:
# messy_list is a list.
# Output:
# The function should return the sorted list in ascending order.
# You may create a new list called sorted_messy_list or return the sorted messy_list.
def q1c(messy_list):
    sorted_messy_list = sorted(messy_list)
    return sorted_messy_list

# 1d Do the same thing, but in descending order. 
# Inputs:
# messy_list is a list.
# Output:
# The function should return the sorted list in descending order.
# You may create a new list called sorted_messy_list or return the sorted messy_list.
def q1d(messy_list):
    sorted_messy_list = sorted(messy_list, reverse=True)
    return sorted_messy_list

# 1e Given two lists, input_list2 and input_list3, write a program that returns the concatenation of two lists. 
# Inputs:
# input_list2 and input_list3 are lists.
# Output:
# The function should return a list with the elements from the first list first.
# You may create a new list called final_list or return the list that contains all elements.
def q1e(input_list2, input_list3):
    final_list = input_list2 + input_list3
    return final_list


# 1f Given a list, input_list, write a program that returns the list with all elements that are less than 10. 
# Inputs:
# input_list is a list.
# Output:
# The function should return a list with the elements that are less than 10.
# You may create a new list called small_list or return the list that contains all elements that are less than 10. 
def q1f(input_list):
    small_list = [x for x in input_list if x < 10]
    return small_list

# 1g Given a list, nested_list, write a program that returns a list, called combined_list, with all the elements of the list of the inner list. 
# Inputs:
# nested_list is a list.
# Output:
# The function should return a list called combined_list with the elements from two inner lists.
def q1g(nested_list):
    combined_list = []
    for sublist in nested_list:
        combined_list.extend(sublist)
    return combined_list

# List Comprehension
# 2a Write a program that creates a list with square values of numbers that are less than 5 and returns it.
# Inputs:
# old_list is a list.
# Output:
# The function should return a list called squared_list with the squared numbers.
# EXPECTED old list: [2, 3, 4, 7] -> new list printed: [4, 9, 16]
def q2a(old_list):
    squared_list = [x**2 for x in old_list if x < 5]
    return squared_list


# 2b Write a program that returns a transpose of nested_list2, using list comprehension.
# Inputs:
# nested_list2 is a list.
# Output:
# The function should return a list called transposed_list with the transpose of nested_list2.
# EXPECTED nested_list2 -> [[1,4], [2,5], [3,6]]
def q2b(nested_list2):
    transposed_list = [[row[i] for row in nested_list2] for i in range(len(nested_list2[0]))]
    return transposed_list

# 2c Do the same, without using list comprehension. 
# Inputs:
# nested_list2 is a list.
# Output:
# The function should return a list called transposed_list with the transpose of nested_list2.
# EXPECTED nested_list2 -> [[1,4], [2,5], [3,6]]
def q2c(nested_list2):
    transposed_list = []
    for i in range(len(nested_list2[0])):
        transposed_row = []
        for row in nested_list2:
            transposed_row.append(row[i])
        transposed_list.append(transposed_row)
    return transposed_list


### End of HW1

# Extra Credit (1pt)
# Have you had any errors completing the assignment? Please explain the error and how you resolved it. Minimum 50 words.
# Write your answer in the comments.
# When I removed comments to simplify testing, I faced unexpected indentation errors due to there still being one space between the start of the test.
# It was easy to fix once I noticed but frustrating because of how long it took me to notice that one space on each text line.
# I learned the importance of preserving code integrity and paying attention to indentation for Python's syntax rules because even one space will prevent the code from being able to run.
#

# Test
# Tells you which test case the program has failed in terminal. 
# These are examples of test cases provided for you to test your program during the homework. 
# All test cases must pass. 
# Your programs will be graded with more than just the provided test cases. 
# Will your program still run and pass with different input?
# Uncomment the class when you want to test your program!

class TestQuestion1a(unittest.TestCase):
     def test_one(self):
         list_length = len(input_list)
         self.assertEqual(list_length, q1a(input_list))
     def test_two(self):
         list_length = len(input_list3)
         self.assertEqual(list_length, q1a(input_list3))

class TestQuestion1b(unittest.TestCase):
     def test_one(self):
         list_length = len(input_list)
         self.assertEqual(list_length, q1b(input_list))
     def test_two(self):
         list_length = len(messy_list)
         self.assertEqual(list_length, q1a(messy_list))

class TestQuestion1c(unittest.TestCase):
     def test_one(self):
         self.assertEqual(sorted(messy_list), q1c(messy_list))
     def test_two(self):
         self.assertEqual(sorted(input_list3), q1c(input_list3))

class TestQuestion1d(unittest.TestCase):
     def test_one(self):
         self.assertEqual(sorted(messy_list, reverse=True), q1d(messy_list))
     def test_two(self):
         self.assertEqual(sorted(input_list3, reverse=True), q1d(input_list3))

class TestQuestion1e(unittest.TestCase):
     def test_one(self):
         self.assertEqual((input_list2+input_list3), q1e(input_list2, input_list3))
     def test_two(self):
        self.assertEqual((input_list+input_list3), q1e(input_list, input_list3))

class TestQuestion1f(unittest.TestCase):
     def test_one(self):
         self.assertEqual([1,3,5,7,9] , q1f(input_list))
     def test_two(self):
         self.assertEqual([1,3,5,7] , q1f([1,3,5,7]))
     def test_three(self):
         self.assertEqual([-1,-5,1,3,5] , q1f([-1,-5,1,3,5]))

class TestQuestion1g(unittest.TestCase):
     def test_one(self):
         self.assertEqual([1,3,2,6,4,5], q1g(nested_list))
     def test_two(self):
         self.assertEqual([1,2,3,4,5,6], q1g(nested_list2))

class TestQuestion2a(unittest.TestCase):
     def test_one(self):
         self.assertEqual([9,4,16], q2a([3,5,2,7,9,4,5]))

class TestQuestion2b(unittest.TestCase):
     def test_one(self):
         self.assertEqual([[1,4], [2,5], [3,6]], q2b(nested_list2))
     def test_two(self):
         self.assertEqual([[1],[2],[3],[4],[5]], q2b([[1,2,3,4,5]]))

class TestQuestion2c(unittest.TestCase):
     def test_one(self):
         self.assertEqual([[1,4], [2,5], [3,6]], q2c(nested_list2))
     def test_two(self):
         self.assertEqual([[1],[2],[3],[4],[5]], q2c([[1,2,3,4,5]]))

if __name__ == '__main__':
    unittest.main()