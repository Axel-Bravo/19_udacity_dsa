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
This problem, as stated to be solved in _time complexity_ of __O(n*log(n))__, has given the clue to be tackled by a 
variation of the __merge sort__ algorithm. Indeed, it is a _merge sort_ algorithm, except for the particular treatment 
if gives to the comparison of results coming from the previous recursion, if we are on the _first level_ of the
recursion. In this case, it does the _comparison_, as usual, but then starts saving the results on 
__alternative lists__, which are then returned as the results. 

The usage of this _alternative list saving_ is due to the fact that having the list perfectly sorted, if we start from
the index[0] and give alternatively a value to each list, occuping this value an increasing digit position, we 
__always__ obtain a combination that satisfies the condition of having a __maximum sum of two numbers__ and __maximum a
digit of difference between them__.  

### Time complexity 
As the base of the algorithm is the __merge sort__, having a time complexity of __O(n*log(n))__, and there have been no
substantial modifications to the algorithm; just the addition of __O(1)__ operations, the time complexity remains 
_equal_.

## Problem 4
This problem is tackler as the construction of a output list, issue form the triple transverse of the elements, not the
most elegant solution in therms of _time complexity_, though extremely efficient from a programing time point of view.

### Time complexity
In this case the _time complexity_ is precisely, _O(3n)_, being assimilated to __O(n)__.

## Problem 5
This problem is focused on the development of the of a __trie__ a data structure derived from a _tree_, suited for a good ratio between _time and space_ complexity.

### Time complexity
For the __trie__, time complexity of **searching and inserting** from a trie depends on the length of the word **a** that’s being searched for, inserted, and the number of total words, **n**, making the runtime of these operations __O(a*n__).

## Problem 6
This problem focuses on __finding max and min values__ from an unsorted array, we are not required to nothing extra and here _lies the key_, not being required to sort anything, we can solve the problem with a single transversal and two placeholders, as reference for _min_ and _max_ values.

### Time complexity
In this case, we perform a __single transverse__ of the whole input, being the time complexity of __O(n)__.
