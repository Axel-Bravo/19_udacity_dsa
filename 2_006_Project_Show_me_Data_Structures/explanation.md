# Project Explanation
Explanation of the different project submodules

## Project 1
[pending]

## Project 2
The recursion process, is based on the visit of each folder, on each folder we keep the files that match the desired pattern and we keep on going deeper on the folder structure by launching subsequent calls to the function. The decision not to use the provided assitance to detect if it was a __file__ or a __folder__, has been decided after not being able to properly use it (and also seeing the facility of coding my own solutions).

In therms of __time complexity__, trying to be guided by the [Master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)), tough not being able to quantify the size of _n/b_ (as it's a folders depth and it needs not to be splitted proportionally). I would infer that __Big O__ notation would give a time complexity of _O(n^n)_.

## Project 3
The implementation of the [__Huffmann Algorithm__](https://en.wikipedia.org/wiki/Huffman_coding), has consisted _as pseudo code tasks were resolved_, in the construction of several __classes__, being:
1. Node
2. Queue
3. Tree
4. HuffmanEncoder 

This has allowed to have a more encapsulated development, as well as, provinding the project with a more consistent structure. The compresing algorithm has shown, for the tested example a reduction of almost 50% of its size. 

In respects to the study of the _time xomplexity_, is __O(Ln)__, being _**L**_ the maximum length of a codeword; more references see [here](https://en.wikipedia.org/wiki/Huffman_coding#Optimality).

## Project 4 
The requirement to create an efficient algorithm that searches into this encapsulated structure, like a [_Matryoshka dolls_](https://en.wikipedia.org/wiki/Matryoshka_doll), as been satisfied by a __recursive algorithm__. 

The time complexity of this algorithm is dependent on the size and structure employed to safe the data. Being the worst case of type __*O(n^n)*__.

## Project 5
This project is based on the creation of a linked list, though, in this case the list is __traversed backwards__ and has the attribute of __inmutability__. This has provoked, that some of the methods developped during the course for _linked list_ are not available for the _BLockchain list_:
- prepend
- remove
- pop 
- insert

As for the time complexity, being a __linked list__ in its core strucutre, it has:

- append: __O(1)__
- search: __O(n)__
- size: __O(n)__
- to_list: __O(n)__
