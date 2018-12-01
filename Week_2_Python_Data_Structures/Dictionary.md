#Dictionary

Dictionaries are a type of collection in Python.

The indexes of the list are like addresses of the correspondent elements.

The dictionary have keys and values.

Keys, like indexes, are addresses of the values.

Keys do not have to be int. They usually are characters (str).

To create dictionaries, we use curly brackets {}

The keys have to be immutable and unique.

The values can be immutable, mutable and duplicates.

Each key and value pair is separated by a comma.

For Example:

```Python
  ['key1':1,'key2':2,'key3':[3,3,3],('key4'):(4,4,4)]
```

The key is used to look up the value:

```Python
  DICT['key1']:1
```

We can add a new entry to the dictionary:

```Python
  DICT['key5']=55555555555
```

We can delete an entry:

```Python
  del(DICT['key5'])
```

We can verify the element in the dictionary:

```Python
  'key5' in DICT: True
```

We can see all the key in the dictionary:

```Python
  DICT.keys()=['key1','key2','key3','key4','key5']
```

Similarly, we can obtains all the values in the dictionary use DICT.values()
