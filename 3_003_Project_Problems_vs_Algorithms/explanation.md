# Project Explanation
Explanation of the different project submodules

## Problem 1
The principle of this algorithm is to "think" that the square root of a number has the property of being the number to 
the power of 2, hence the _floored squared root_ is given __when the floored divion result is the same as the divisor__.

### Time complexity:
In this case time complexity is __O(log(n))__, as we transverse all integer number till finding n (being _s_ the 
number of times this is done); using the formula __s² = n__ , which is equivalent to __log(n)=s__.

## Problem 2
The principle employed in this algorithms is based directly in the _binary search_ algorithms, differently, to this 
implementations, in its structure, it has been decided to be employed a __more divide approach__, rather than
computationally expensive on previous levels to _spare_ some division; e.g. when the lists are of size 2, both values
could have been checked (though this would have increased our __time complexity__). 

### Time complexity
The time complexity being an algorithm based on binary search is __O(log(n))__.  The number of iterations we perform,
i.e. recursive depth, follows the rule of _recursive_depth^2 = n_. Thus if we isolate the number of iterations in
relation to the __input space__ (n), we obtain __log(n) = recursive_depth__.

## Problem 3


### Time complexity 