""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
from collections import deque
import math

def check_binary_search_tree_(root):
    dq = deque([(root, -math.inf, math.inf)])
    while dq:
        node_now, minV, maxV = dq.popleft()
        if node_now == None: continue
        if node_now.data <= minV or node_now.data >= maxV: return False
        if node_now.left: dq.append((node_now.left, minV, node_now.data))
        if node_now.right: dq.append((node_now.right, node_now.data, maxV))
    return True