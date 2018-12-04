with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt','w') as writefile:
    writefile.write('This is line A\n') #the \n is for a new line
    writefile.write('This is line B\n') #the \n is for a new line

# with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt') as testwritefile:
#     print(testwritefile.read())

# with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt','a') as writefile:
#     writefile.write('This is line C\n')

# with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt') as testwritefile:
#     print(testwritefile.read())

with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)

with open('Example3.txt','r') as testwritefile:
    print testwritefile.read()
