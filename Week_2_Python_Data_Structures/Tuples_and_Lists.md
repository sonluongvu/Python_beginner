# List and Tuples

## Tuples

Tuples are an ordered sequence

Tuples are written as comma-separated elements within parentheses

Example:

```Python
  Ratings=(10,9,6,5,10,8,9,6,2)
```
Tuples can contain different types of data (like str, int, or float)

The elements of the tuples can be accessed through their correspondent indexes.

Example: For the tuple Tuple1

```Python
  Tuple1 =("disco",10,1.2)
```

  - The index of each elements in Tuple1:

    index | element
    -----|------
    0/-3 | "disco"
    1/-2 | 10
    2/-1 | 1.2

To call the element use Tuple1[index]

Example:

```Python
  Tuple1[0]:"disco"
  Tuple[2]: 1.2
  Tuple[-2]: 10  
```

Tuple can be combines together. Example:

```Python
  Tuple2=Tuple1+("hard rock",10)
  Tuple2:("disco",10,1.2,"hard rock",10)
```

## Tuple Slicing:

We can slice the tuple using colon ":", the last index need to be 1 unit larger than the index of the last element

```Python
  tuple2[0:3]:('disco',10,1.2)
```

'len' command can be used to obtain the length of a tuple.

```Python
  len(tuple1):3
```

## Tuples: Immutable

We can change the tuples. However, we can assign another tuple to the variable. As a result, if we want to immutate a tuble, we can create a new tuple.

## Tuples: Nesting

A tuple can contain another tuple as well (nesting). We can access the 'sub' tuple by using the index of the outside tuple. We can visualize this like a tree

```Python
  NT=(1,2,('pop','rock'),(3,4))
  NT(2):('pop','rock')
  NT[2][1]:'rock'
```
## Lists

Lists are also ordered sequences. A list is represented with square brackets. List is mutable. Example:

```Python
  L=['Michael Jackson',10.2,1982]
```

List can contain str, int, float, bool, list, and tuple.

We can access the list through index like tuple. Example:

```
 L=['Michael Jacson',1,2,[2,3,4,5]]
 L[3][2]:4
```

We can use the negative index to access through negative number

We can also combine list together (like tuples)

## Lists: Slicing

We can slice the list to get the elements that we want. It is similar to tuples.

## Lists: mutable

Using extend to add more elements into list. Example:

```Python
  L=['Michael Jackson',10.1,1982]
  L. extend(['pop',10])
  L:['Michael Jackson',10.1,1982,'pop',10']
```

append can be used to add one element only into the original list. Example:

```Python
  L=['pop',10]
  L. append([1,2,3])
  L:['pop',10,[1,2,3]]
```

We can change the list individual element. Example:

```Python
  L=['pop',10]
  L[0]='rock'
  L:['rock',10]
```

We can use del to delete an element in the list. Example:

```Python
  L=['pop',10]
  L=del(L[0]) # 'pop' is deleted from list L.
  L:[10]
```

## Convert String to List:

Using command split:

```Python
  "hard rock".split()  split the string "hard rock" into the list ['hard','rock']
```

We can use split function to split a string based on the delimiter:

```Python
  'a,b,c,d'.split(',') the result is ['a','b','c','d']
```

## Lists: Aliasing

Multiple names referring to the same object is called aliasing.

If we create list A and then assign list B=A. If we change an element in list A, the element in list B will be changed too. To avoid this, we can use the clone

## Lists: Clone

Use the following syntax to clone a list:

```Python
  A=['rock',10,2]
  B=A[:]
```

In this case, variable B is a new copy or clone of the original list. As the result, if we change A, B is not changed.

We can use the help command to know more information: help(A)
