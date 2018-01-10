def isunique_naive(string):
    for i in range(len(string)):
        if string.find(string[i], i+1) != -1:
          return False # Char is not unique
    return True # All unique characters  

# O(N)
def isunique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char) # Char to ASCII
        if char_set[val]:
            return False # Char already found in string
        char_set[val] = True

    return True
