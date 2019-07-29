# Project Explanation
Explanation of the different project submodules

## Project 1
For the __LRU_Cache__ problem, after thinking of using different approaches, like _queue, heap ..._, it has been decided
to use a construction based on a dictionary for the __cache__ and a list for the __priority__. In respects to the
limitation of the _cache_, any hashing approach has been discarded, as the __risk of collision__, hence the necessity 
of adding a __nested hash__ (reaching __O(n)__). Finally deciding for this approach that satisfies the __O(1)__ 
requirement. 
