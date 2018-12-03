# Reading Files

## Reading Text Files:

One way to read or write a file in Python is to use the built-in **open** function. The **open** function provides a **File object** that contains the methods and attributes you need in order to read, save, and manipulate the file. In this notebook, we only cover .txt files. The first parameter is the file path and the file name. Examample:

```Python
  file = open ("/resources/data/Example.1txt","r")
```

The mode argument is optional and the default value is **r**. In this note, we only cover to note:
  - **r** Read mode for reading files.
  - **w** Write mode for writing files.

For the next example, we will use the text file **Example1.txt**. The file is in Python_for_Data_Science/Week_4_Working_with_Data_in_Python

We can read the file:

```Python
example1="../Python_for_Data_Science/Week_4_Working_with_Data_in_Python"
file1 = open (example1,"r")
```
We can view the attributes of the file.

The name of file: `file1.name

The mode the file object is in: `file1.mode

We can read the file and assign it to a variable

```Python
FileContent=file1.read()
FileContent
```

the "/n" means that there is a new line.

We can print the file: `print FileContent`

The file is of type string: `type(FileContent)`

We must close the file object: `file1.close()`

## A Better Way to Open a File:

Using the **with** statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object.

```Python
with open(example1,"r") as file1:
  FileContent=file.read()
  print(FileContent)
```

The file object is closed, you can verify by running: 'file1.close'

We can see the info in the file: `print(FileContent)`

The syntax is a little confusing as the file object is after the **as** statement. We also don't explicitly close the file.

We don't have to read the entire file, for example, we can read the first 4 characters by entering 3 as the parameter to the method **.read()**:

```Python
with open(example1) as file1:
  print(file1.read(4))
```

Once the method **.read(4)** is called the first 4 characters are called. If we call the method again, the next 4 characters are called. Example:

```Python
with open(example1) as file1:
  print(file1.read(4))
  print(file1.read(4))
  print(file1.read(7))
  print(file1.read(15))
```

Here is an example using the same file, but instead we read 16,5, and then 9 characters:

```Python
with open(example1) as file1:
  print(file1.read(16))
  print(file1.read(5))
  print(file1.read(9))
```

We can also read one line of the file at a time using the method "readline()"

We can use a loop to iterate through each line:

```Python
with open(example1) as file 1:
  i=0
  for line in file1:
    print("Iteration", str(i),":",line)
    i=i+1
```

We can use the method **readline()** to save the text file to a list:

```Python
with open(example1) as file1:
    FileasList=file1.readlines()
```

Each element of the list corresponds to a line of text.
