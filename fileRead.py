"""
Chapter 4 Example ( page 102)
Program:fileRead.py
2/28/2025

application that will prompt for a filename, then open the file contents in READ mode and display them
"""

#prompt the user for a filename(text files only)
fileName = input("Which file would you like to read? >>")
# Variable that becomes the local referenceto the file data

aFile = open(fileName , "r")

#FOR loop to go throught the contents of the aFile variable, counter variable will be focusing on any line with a line break
for eachLine in aFile:
	print(eachLine, end=" ")
print("\n\nEnd of content")

#use the close () method to cut off unwanted access to the file

aFile.close()

input("press ENTER to close thi application...")