# Quiz: Find the first recurring character in a string

# Naive way takes O(n^2)
def isDouble_naive(str):
  # For each 'i'th char, we check whether it occurs double
  for i in range(len(str)):
    for j in range(i+1, len(str)):
      if str[i] == str[j]:
        return str[i]
  return None
  
# Better way using dict takes O(n)
def isDouble_dict(str):
  # Using dictionary (hash table)
  ht = dict()
  for c in str:
    if c not in ht: # O(1) for average case, O(n) for worst case
      ht[c]=1 # O(1)
    else:
      return c
  return None

# Better way using set takes O(n)  
def isDouble_set(str):
  # Using dictionary (hash table)
  ht = set()
  for c in str:
    if c not in ht: # O(1) for average case, O(n) for worst case
      ht.add(c) # O(1)
    else:
      return c
  return None
  
print (isDouble_set('cdeab'))
    
