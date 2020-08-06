''' 
Name: payroll.py
Assignment: Assignment 3, COMP301
Description: Displays csv data in table
Author: Haris Siddiqi
Student #: 301126020
Date: August 6, 2020
'''

# Data is in csv format
import csv

# Write function and variable names according to python formatting conventions
def make_table(csv_file):
    ''' Displays csv data in tabular format '''
    # Open file
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Format table
        print(f"\n\t\t\tEmployee Work Hours")
        print(f"\t----------------------------------------------")
        print(f"\tEmployee Number | Employee Name | Hours Worked")
        print("\t----------------------------------------------")

        # Create table
        for employee in csv_reader:
            print(f'\t\t{employee[0]}\t\t{employee[2]}\t\t{employee[3]}')

# Call function
make_table('data.txt')
