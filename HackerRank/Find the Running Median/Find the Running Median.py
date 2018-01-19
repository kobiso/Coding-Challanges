# Find the Running Median
# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heappush, heappop
import sys

n = input()
maxH = [] # Invert the sign of integers to use min-heap as max-heap
minH = [] # Python 'heapq' only support min-heap
for inp in sys.stdin:
    if len(maxH) == 0:
        heappush(maxH,-int(inp))
    elif int(inp) < -maxH[0]:
        heappush(maxH,-int(inp))
        if len(maxH) > len(minH)+1:
            heappush(minH,-heappop(maxH))        
    elif int(inp) >= -maxH[0]:
        heappush(minH,int(inp))
        if len(maxH) < len(minH):
            heappush(maxH,-heappop(minH))
            
    if (len(maxH)+len(minH))%2 == 0: # Even numbers
        print ((-maxH[0]+minH[0])/2)
    else: # Odd numbers
        print (format(-maxH[0], "0.1f"))