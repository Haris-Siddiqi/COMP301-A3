''' 
Name: copyfile.py
Assignment: Assignment 3, COMP301
Description: Copies content from one file to another
Author: Haris Siddiqi
Student #: 301126020
Date: August 5, 2020
'''

def copier(Source, Destination):
    ''' Copies content from one file to another '''
    # Read source
    with open(Source,'r') as fileData:
        SourceContent= fileData.readlines()

    # Save content of destination
    with open(Destination,'r')as fileData:
        DestinationContent= fileData.readlines()

    # Append to destination
    for eachline in SourceContent:
        DestinationContent = open(Destination,'a')
        DestinationContent.write(eachline)
    
    print("\nCopy complete")

# Get files from user
print("This program copies text from one file to another")
print("Enter the name of the source file: ")
file1 = input()
print("Enter the name of the destination file: ")
file2 = input()

# Calls copy function
copier(file1, file2)