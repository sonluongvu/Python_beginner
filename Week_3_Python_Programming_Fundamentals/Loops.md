# Loops

## Range:

Sometimes, you might want to repeat a given operation many times.
Repeated executions like this are performed by **loops**. Two most common types of loops, **for** loops and **while** loops.

Before discussing loops, let's discuss the **range** object. Range can be considered as an ordered list. For now, let's look at the simplest case. if we would like to generate a sequence that contains three elements ordered from 0 to 2 we simply use the following command:

``` Python
range(3)
```

  This create a list [0,1,2]

## The **for** loop:

The **for** loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.

Try to use a **for** loop to print all the years presented in the list **dates**

```Python
dates = [1982,1980,1973]
N=len(dates)

for i in range(N):
  print(dates[i])
```

The code above is executed **N times, each time the value of i** is increased by 1 for every execution. The statement executed is to **print** out the value in the list at index **i**.

### Example of printing out the elements of a list:

In this example we can print out a sequence of numbers from 0 to 7

```Python
for i in range(0,8):
  print(i)
```

In Python we can directly access the elements in the list:

```Python
dates = [1982,1980,1973]
for year in dates:
  print year
```

For each iteration, the value of the variable **years** behaves like the value of **dates[i]** in the first example.

We can change the elements in a list:

```Python
squares=['red','yellow','green','purple','blue']

for i in range(0,5):
  print 'before square', i, 'is', squares[i]
  squeres[i]='wight'
  print 'after square', i, 'is', squares[i]
```

## While Loops

As known, the **for** loop is used for a controlled flow of repetition.

However, what if we don't know when we want to stop the loop? What if we want to keep executing the code block until a certain condition is met? The **while** loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a **False** value.

```Python
dates = [1982,1980,1973,2000]

i=0;
year=0
while(year!=1973):
  year=dates[i]
  i=i+1
  print(year)

print('it took', i, 'repetitions to get out of loop')
```
