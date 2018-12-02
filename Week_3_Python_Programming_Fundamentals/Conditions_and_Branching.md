# Conditions and Branching

## Comparison Operators

Comparison operations compare some value or operand, based on a condition, they produce a Boolean. When comparing two values, we can use these oprators:

  - equal: ==
  - not equal: !=
  - greater than: >
  - less than: <
  - greater than or equal to: >=
  - less than or equal to: <=

Let's say we assign **a** a value of 6. We can use the equality operator **==** to determine if two values are equal:

```Python
a=5
a==6
```

The result above is False (5 does not equal 6)

Consider the following equality comparison operator **i>5**. If the value of the left is less than the value on the right operand, then the condition becomes **True** or else we get a **False**. Example:

```Python
i=6
i>5 #this generates True

i=2
i>5 #this generages False
```
These rule for inequality is the same. Inequality can be applied for str as well:

```Python
'ACDC'=='Michael Jackson' # This generates False
'ACDC'!='Michael Jackson' # This generates True
```

We can perform inequality operations, the the order of the leter depends on ASCII value.

For example, the decimal equivalent of **!** is 21, while the decimal equivalent of **+** is 43. Therefore, **+** is larger than **!**. If there are multiple letters, the first letter takes precedence in ordering

```Python
'+' > '!'
'BA'>'AB'
```

## Branching:

Branching allows us to run different statements for different inputs. It is helpful to think of an **if statement** as a locked room, if the statement is true you can enter room and your program will run some predefined task but if the statement is false your program will skip the task.

For example, consider the blue rectangle representing an ACDC concert. If the individual is 18 or older they can enter the ACDC concert. if they are under the age of 18, they cannot enter the concert. We have the if statement and we have the expression that can be **True** or **False**, the brackets are not necessary. We have a colon within an indent; then we have the expression that is run if the condition is **True**. The statements after the **if statement** will run regardless of whether the condition is true or false.

``Python
age=19
#age=18

#expression that can be true or false
if age>18:

  #within an indent, we have the expression that is run if the condition is true.
  print('you can enter')

#The statements after the if statement will run regardless if the condition is true or false.
print('move on')
```

**Go to Conditions_and_Branching.py to test the example.

The **else** statement will run a different block of code if the same condition is false. Let's use the ACDC concert analogy again. If the user is 17 they can not go to the ACDC concert, but they can go to the Meatloaf concert. The syntax of the **else** statement is similar, we simply append the statement **else** with the new condition. Try changing the values of **age** to see what happens:

```Python
age=18
#age=19
if age >18:
  print('you can enter')
else:
  print ('go see Meat Loaf')
print('move on')
```

the **elif** statement, short for else if, allows us to check additional conditions if the proceeding condition is false. Example:

```Python
age=18
if age>18:
  print 'you can enter'
elif age == 18:
  print 'go see Pink Floyd'
else:
  print 'go see Meat Loaf'
print 'move on'
```
