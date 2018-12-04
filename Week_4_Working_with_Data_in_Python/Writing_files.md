# Writing and Saving Files in Python

This notebook only provide information regarding writing and saving data into **.txt** files.

## Writing Files:

We can open a file object using the method **write()** to save the text file to a list. To write the mode, argument must be set to write **w**. Example:

```Python
with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt','w') as writefile:
    writefile.write('This is line A')
```

we can read the file to see if it worked:

```Python
with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt') as testwritefile:
    print(testwritefile.read())
```

We can write in multiple lines:
```Python
with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt','w') as writefile:
    writefile.write('This is line A\n') #the \n is for a new line
    writefile.write('This is line B\n') #the \n is for a new line
```

the method **.write()** works similar to the method **readline()**, except instead of reading a new line it writes a new line. The process is illustrated in the figure, the different colour coding of the grid represents a new ine added to the file after each method call.

We can check if the result correct by use the method **read()**

By setting the mode argument to append **a** you can append a new line as follow:

```Python
with open('../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example2.txt','a') as writefile:
    writefile.write('This is line C\n')
```

We can write a list to a **.txt** file by:

```Python
Lines=['This is line A\n','This is line B\n','This is line C\n']
with open()
```
