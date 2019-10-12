# We use the `left` parameter to keep track of the number of elements to the left of our index that we've thrown away.
def recursive_binary_search(target, source, left=0):
    # Base case - if we're searching an empty list, the element isn't there.
    if len(source) == 0:
        return None
    
    # Find the center of our list
    center = (len(source)-1) // 2
    
    # If we've found the target, return the center index (plus anything to the left we've previously thrown away)
    if source[center] == target:
        return center + left
    
    # if not, repeat the process
    elif source[center] < target:
        # we're searching the upper half of the array in this case, 
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)
     
fibonacci = [1, 2, 3, 5, 8, 13]
for num in range(1, 16):
    print(recursive_binary_search(num, fibonacci))
