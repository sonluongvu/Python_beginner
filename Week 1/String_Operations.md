# String Operations

## String

A string is a sequence of characters.

A string can be spaces or digits.

A string can be special characters.

A string can be considered as an ordered sequence and its index can be accessed. For example:

```python
  Name='Michael Jackson'
  Name[0]:M
  Name[6]:l
  Name[-1]:n
  Name[-3]:s
  #the space are not counted in the number
  Name[8]:J
```

We can bind a string to another variable

```python
  Name[0:4]=Mich
  Name[8:12]=Jack
  Name[::2]:'McalJcsn' # Every second letters is selected
  Name[0:5:2]:'Mca'
```

len command can be used to obtain the length of the String

```python
  len('Michael Jackson'):15
```

The string can be added together.

```python
  Name='Michael Jackson'
  Statement = Name + 'is the best'
  Statement = 'Michael Jackson is the best'
```

The string can be replicated by using multiplication '*'

```python
  Name*3='Michael JacksonMichael JacksonMichael Jackson'
```

## Strings: escape sequences

'\' are meant to proceed escape sequences

Escape sequences are strings that are difficult to input

```python
  print('Michael Jackson \n is the best') # \n represents a new line
  print('Michael Jackson \t is the best') # \n represents a tab
  print('Michael Jackson \\ is the best') # Michael Jackson \ is the best
```

## String Methods

String are sequences so it has apply methods that work on lists and tuples.

Upper changes the letters to be upper cases.

```python
  A='Thriller is'
  B=A.upper()
  B:'THRILLER IS'
```

Replace can replace the part of the string with another substring

```python
  A='Michael Jackson'
  B=A.replace('Michael','Janet')
  B:'Janet Jackson'
```

Find can find the substring. The output is the first index of the sequence.

```python
  Name='Michael Jackson'
  Name.find('el'):5
```
