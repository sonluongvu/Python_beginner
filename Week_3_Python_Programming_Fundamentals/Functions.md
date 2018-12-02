# Writing Your Own Functions in Python

## Defining a Function

A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.

There are two types of functions:
  - Pre-defined functions
  - User defined functions

### What is a Function?

You can define functions to provide the required functionality. Here are simple rules to define a function in Python:
  - Functions blocks begin **def** followed by the function **name** and parentheses()
  - There are input parameters or arguments that should be placed within these parentheses.
  - You can also define parameters inside these parentheses.
  - There is a body within every function that starts with a colon (:) and is indented
  - you can also place documentation before the body
  - The statement **return** exits a function, optionally passing back a value

An example of a function that adds on to the parameter **a** prints and returns the output as **b**:

```Python
def add(a):
  """
  add 1 to a
  """
  b=a+1
  print a, "if you add one", b
  return(b)
```

### A labeled function:

We can obtain help about a function: ```help(add)```

We can call the function: ```add(1)```

If we call the function with the new input we get a new result.

We can create different functions. For example, we can create a function that multiplies two numbers. The numbers will be represented by the variables **a** and **b**:

```Python
def Mult(a,b):
  c=a*b
  return(c)
```

The same function can be used for different data types. For example, we can multiply two integers: ```Mult(2,3)

Two floats: ```Mult(10,3.14)'''

We can even replicate a str by multiplying with an int: ```Mult(2,"Michael Jackson")```

## Variables:

The input to a function is called a formal parameter.

A variable that is declared inside a function is called a local variable. The parameter only exists within the function (i.e. the point where the function starts and stops).

A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program.

```Python
def square(a):
  """Square the input and add one"""
  #Local variable
  b=1
  c=a*a+b
  print a, "if you square +1", c
  return(c)
```

If there is no **return** statement, the function returns **None**. The following two functions are equivalent:

```Python
def MJ():
  print('Michael Jackson')

def MJ1():
  print('Michael Jackson')
  return(none)
```

## Pre-defined functions:

There are many pre-defined functions in Python like: print(), sum(), len()

## Functions makes Things Simple:

We can replace the lines of code with a function. A function combines many instructions into a single line of code. Once a function is defined, it can be used repeatedly. The same fuction can be invoked many times in the program. We can save our function and use it in another program or use someone else's function.

## Using if/else Statements and Loops in Functions:

The **return()** function is particularly useful if there is **IF** statements in the function, when we want our output to be dependent on some condition:

```Python

def type_of_album(artist, album, year_released):
  if year_released > 1980:
    print(artist, album, year_released)
    return "Modern"
  else:
    print (artist, album, year_released)
    return "oldie"

x= type_of_album("MJ", "Thriller", 1980)
print x
```

We can use loop in a function as well.

## Setting Default Argument Values In Our Custom Functions:

We can set a default value for arguments in our function. For example, in the ```isGoodRating()``` function, what if we wanted to create a threshold for what we consider to be a good rating? perhaps by defaul, we should have a default rating of 4

```Python
def isGoodRating(rating=4):
  if rating < 7:
    print "this album sucks it's rating is", rating
  else:
    print 'this album is good its rating is', rating
```

## Global Variables:

So far, we've been creating variables within functions, but we have not discussed variables outside the function. These are called global variables.

```Python
artist = "MJ"
def printer1(artist):
  internal_var=artist
  print(artist,"is an artist")

printer1(artist)
```
If we print ```internal_var``` we get an error: ```name 'interval_Var' is not defined```

It's because all the variables we create in the function is a **local** variable.

But there is a way to create **global variables** from within a function as follows:

```Python
artist='MJ'

def printer(artist):
  global internal_var
  internal_var = 'WH'
  print artist, 'is an artist'

printer (artist)
printer (internal_var)
```

## Scope of a Variable:

The scope of a variable is the part of that program where that variable is accessible. Variables that are declared outside of all function definitions are accessible from anywhere within the program. As a result, such variables are said to have global scope, and are known as global variables.

A variable that is defined within a function is said to be a local variable of that function. That means that it is only accessible from within the function in which it is defined.

If there are 2 variables, the first one is at the global scope, and the second one is a local variable. Inside the defined function, the local variable takes precedence. However, outside the defined function, the global variable take precedence because the local variable is not defined.
