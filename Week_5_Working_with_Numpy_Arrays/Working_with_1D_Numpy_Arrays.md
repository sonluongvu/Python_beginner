# Working with 1D-Numpy Arrays

## Numpy in Python:

```Python
import time
import sys
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline
```

```Python
def Plotvec(u,z,v):
    #This function is used in code 
    ax = plt.axes()
    as.arrow(0, 0, *u, head_width=0.05, color = 'r' head_length=0.1)
    plt.text(*(u+0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05,color='b', head_length=0.1)
    plt.text(*(v+0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z+0.1), 'z')
    plt.ylim(-2,2)
    plt.xlim(-2,2)
```

Recalled, a Python list is a container that allows us to store and access data. We can create a Python List as follows:

```Python
a=['0',1,'two','3',4]
```

We can access the data via an index.

We can access each element using a square bracket:

A numpy array is similar to a list, it's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing numpy:

```Python
import numpy as np
```

We then cast the list as follows

```Python
a=np.array([0,1,2,3,4])
a
```

Each element is of the same type, in this case int.

As with lists we can access each element via a square bracket:

```Python
print 'a[0:', a[0]
```

The valu of 'a' is stored

If we check the type of 'a', we get 'numpy.ndarray'

As numpy arrays contain data of the same type, we can use the attribute **dtype** to obtain the Data-type of the array's elements. In this case a 64-bit int: `a.dtype`

We can create a numpy array with real numbers

```Python
b=np.array([3.1, 11.02, 6.2, 213.2, 5.2])
```

When we check the type of the array we get 'numpy.ndarray'

If we examine the attribute **dtype** we see float 64, as the elements are not int

We can change the value of the array, consider the array'c':

```Python
c=np.array([20,1,2,3,4])
```

We can change the 1st element of the array to 100:

```Python
c[0]=100
```

We can slice the numpy array, and we can select the elements from 1 to 3 and assign it to a new numpy array 'd':

```Python
d-c[1:4]
d
```
We can assign the corresponding indexes to new values:
```Python
c[3:5]= 300,400
```

Similarly, we can use a list to select a specific index. The list 'select' contains several values:

```Python
select=c[0,2,3]
```

We can use the list as an argument in the brackets. The out put is the elements corresponding to the particular index.

We can assign the specified elements to a new value

```Python
c[select]=10000
```

## Some basic array attributes:

- Attribute size is the Number of Elements in the array

- The attribute **ndim** represents the number of array dimensions or the rank of the array

- The attribute 'shape' is a tuple of integers, indicating the size of the array in each dimension

- The other attributes:
    - mean
    - std (standar deviation)
    - max
    - min

## Array addition

The addition of array is equivalent to vector addition. Similar with multiplicaiton, and substraction.

