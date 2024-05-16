"""
File:		insertion_sort.py
Title:		Insertion Sort Demo
Description:	Insertion Sort is a sorting algorithm that works well for small arrays.
Author:		Daniel R. South
Date:		2024-05-09
"""

# Procedure to swap the value of the current element with the previous element (assumes ascending order)
#
def swap_with_previous(A, j):
	temp_val = A[j-1]
	A[j-1] = A[j]
	A[j] = temp_val


# Procedure to move one element in the list/array to its correct location in the sorted range
#
def sort_element(A, elem_pos):
	for i in range(elem_pos, 0, -1):
		if A[i] < A[i-1]:
			swap_with_previous(A, i)
		else:
			break

# Procedure to perform the Inserttion Sort algorithm on List or Array A
#
def insertion_sort(A):
	# Start with the second element in the array.
	# The sort_elements funciton compares A[i] to A[i-1]
	for i in range(1, len(A)):
		sort_element(A, i)

#
# Test the Insertion Sort algorithm as coded
#

list1 = [2, 4, 6, 3, 7, 9, 5]

print("\nBefore sort")
print(list1)
insertion_sort(list1)
print("After sort")
print(list1)


teams = ['Yankees', 'Braves', 'Pirates', 'Blue Jays', 'White Sox', 'Red Sox', 'Mets', 'Dodgers', 'Cubs' ]

print("\nBefore sort")
print(teams)
insertion_sort(teams)
print("After sort")
print(teams)


import numpy as np
array1 = np.random.randint(1, 1000, 250)

print("\nBefore sort")
print(array1)
insertion_sort(array1)
print("After sort")
print(array1)
