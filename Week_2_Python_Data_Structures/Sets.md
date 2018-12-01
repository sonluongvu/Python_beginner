#Sets

Is a type of collection

  - Like lists and tuples, different Python types can be inputted into Sets.

Unlike lists and tuples, they are unordered.
  - Sets do not record element position.

Sets only have unique elements
  - This means there is only one of a particular element in a set.

## Creating a Set:

```Python
  Set1={'pop','rock','soul','hard rock','rock','R&B','rock','disco'}
```

When the actual set are created, duplicated items will not be presented.

We can convert a list to a set by use set()

```Python
  album_list=['Michael Jackson','Thriller','Thriller',1982]
  album_set=set(album_list)
  album_set: ('Michael Jackson','Thriller',1982)
```

## Set Operations:

Can be use to change a set.

``` Python
A={'Thriller','Back in Black','AC/DC'}
A.add('NSYNC')
A: {'Thriller','Back in Black','AC/DC','NSYNC'}
```

To remove, use the A.remove(item)

We can verify use item_name in set_name

## Sets: Mathematical set operations:

set_1 & set_2: the intersection of 2 sets.

set_1.union(set_2): new set with all elements in set_1 and set_2

set_3.issubset(set_1): check if set 3 is a sub set of set_1 (True/False)
