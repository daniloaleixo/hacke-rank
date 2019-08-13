#!/bin/python3

# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 10.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .

# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

# Function Description

# Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

# gradingStudents has the following parameter(s):

# grades: an array of integers representing grades before rounding
# Input Format

# The first line contains a single integer, , the number of students.
# Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    result_grades = []
    for grade in grades:
        if (grade < 38):
            result_grades.append(grade)
        elif (grade % 5 < 3):
            result_grades.append(grade)
        else:
          result_grades.append(grade + 5 - (grade % 5))
    return result_grades


if __name__ == '__main__':
        # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
