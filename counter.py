#this program will count your same value without comparing...
#with collections library we can say.
import collections
c = collections.Counter()
for word in ['red', 'red', 'blue', 'white']:
     c[word] += 1
print(c)
