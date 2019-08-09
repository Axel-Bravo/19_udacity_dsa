# Project Explanation
Explanation of the different project submodules

## Project 1
For the __LRU_Cache__ problem, after thinking of using different approaches (included previous failures), it has been
decided to use the __OrderedDict()__, specifically the use of the _method_ __.popitem(last=False)__. It allows to 
remove the _first added element_, which is basic for the __priority construction__ demanded. 

### Time and Space complexity
In respects to the limitation of the _cache_, any hashing approach has been discarded, as the __risk of collision__, 
hence the necessity of adding a __nested hash__ (reaching __O(n)__). Finally deciding for this approach that satisfies
the __O(1)__ requirement. As in therms of _space complexity_, the structure requires the usage of __c__, being __c__
the desired *LRU_Cache* capacity; being it in the end assimilable to __O(n)__.

## Project 2
The recursion process, is based on the visit of each folder, on each folder we keep the files that match the desired
pattern and we keep on going deeper on the folder structure by launching subsequent calls to the function. The 
decision not to use the provided assistance to detect if it was a __file__ or a __folder__, has been decided after 
not being able to properly use it (and also seeing the facility of coding my own solutions).

### Time and Space complexity
In therms of __time complexity__, trying to be guided by the
[Master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)), tough not being able to 
quantify the size of _n/b_ (as it's a folders depth and it needs not to be splitted proportionally). Thus, using
another approach, the time complexity is dependant on the number of iterations that are launched. Being in this case
dependent on __depth__ and __width__ of folders, resulting in a __O(d*w)__. As for the space complexity, in this case, 
it is directly dependent on the number of returns the function does, hence, the number of found files __f__, __O(f)__.

## Project 3
The implementation of the [__Huffmann Algorithm__](https://en.wikipedia.org/wiki/Huffman_coding), has consisted _as
pseudo code tasks were resolved_, in the construction of several __classes__, being:
1. Node
2. Queue
3. Tree
4. HuffmanEncoder 

This has allowed to have a more encapsulated development, as well as, providing the project with a more consistent
structure. The compresing algorithm has shown, for the tested example a reduction of almost 50% of its size. 

### Time and Space complexity
In respects to the study of the _time complexity_, would be __O(Ln)__, being _**L**_ the maximum length of a codeword; 
more references see [here](https://en.wikipedia.org/wiki/Huffman_coding#Optimality). If I had not used a _built it_ 
function for sorting the input that takes __O(n*log(n))__; ending up the time complexity being __O(n*log(n))__. In 
respects to the _space complexity_, it is directly related to the __size of the employed alphabet__, in this case
**_k_**, resulting in __O(k)__.

## Project 4 
The requirement to create an efficient algorithm that searches into this encapsulated structure, like a
[_Matryoshka dolls_](https://en.wikipedia.org/wiki/Matryoshka_doll), as been satisfied by a __recursive algorithm__. 

### Time and Space complexity
The time complexity of this algorithm is dependant on the number of iterations that are launched. Being in this case
dependent on __encapsulation of groups__ and __number of users__ of folders, resulting in a __O(g*u)__. As for the 
_space complexity_, it is directly dependent on the number of returns the function does, hence, in this case __O(1)__.

## Project 5
This project is based on the creation of a linked list, though, in this case the list is __traversed backwards__ and
has the attribute of __inmutability__. This has provoked, that some of the methods developed during the course for 
_linked list_ are not available for the _Blockchain list_:
- prepend
- remove
- pop 
- insert

### Time and Space complexity
As for the time complexity, being a __linked list__ in its core structure, it has:

- append: __O(1)__
- search: __O(n)__
- size: __O(n)__
- to_list: __O(n)__

In respect to _space complexity_, it is directly dependant on the number of __nodes__ our BlockChain incorporates,
resulting in __O(n)__.

## Project 6 
For the __union and intersection__ problem, the approach has been to transform the _linked lists_, a format which is
harder to work with, on something much __simpler__ as is a list. Once the transformation has been done, the combination
with the handy _object_ __sets__, has done all the work.

### Time and Space complexity
In the study of the __time complexity__, we find that the transformation from _linked list_ to list, takes __O(n)__
 time complexity, the the set function is in the __same or less__ order of magnitude, as for the variations:
- _Union_: we find the creation of the final array, again __O(n)__, making __n*O(n)__ be resulting to __O(n)__
- _Intersection_: we find the creation of the final array, which is a _double for-loop_ (operation _x in s_, acts with 
 __O(n)__), resulting finally in __O(n^n)__

In respect to the _space time complexity_, we generate for both functions, 3 auxiliary lists, being _O(3n)_; and 
resulting in __O(n)__.