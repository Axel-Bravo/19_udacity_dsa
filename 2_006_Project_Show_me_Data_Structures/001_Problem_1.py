#%% Imports and function declaration
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.priority = []
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        try:  # If value in the cache

            # Update priority due to access
            self.priority.remove(key)
            self.priority.append(key)
            return self.cache[key]

        except KeyError and ValueError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        if key in self.priority:  # Update priority due to access
            self.priority.remove(key)
            self.priority.append(key)
            self.cache[key] = value
        else:  # Add to cache
            if len(self.priority) < self.capacity:  # Still space on cache
                self.cache[key] = value
                self.priority.append(key)
            else:  # No space available on cache
                key_remove = self.priority.pop(0)
                self.cache.pop(key_remove)

                self.cache[key] = value
                self.priority.append(key)


#%% Testing Official
# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1

