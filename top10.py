import heapq
import itertools
from operator import itemgetter

things = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
	"four" : 4,
	"five" : 5,
	"six" : 6,
	"seven" : 7,
	"eight" : 8,
	"nine" : 9,
	"ten" : 10,
	"eleven" : 11
}

top10 = heapq.nlargest(10, things.items(), itemgetter(1,0))
for key,value in top10:
   print (value, key)