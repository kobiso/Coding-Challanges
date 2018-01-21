""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import math
visited = -math.inf

# Inorder traversal using recursive function
def check_binary_search_tree_(root):
    global visited
    if not root: return True
    if not check_binary_search_tree_(root.left): return False
    if root.data <= visited: return False        
    visited = root.data
    if not check_binary_search_tree_(root.right): return False
    return True