import os
import timeit

heap_size = []
running_time = []

# timeit.timeit('os.system("java P2 <Factorial.java")', "import os", number=1)

for i in range(1024,1025):
	command = "os.system("
	running_time.append(timeit.timeit('os.system("java -Xms'+str(i)+'k -Xmx'+str(2*i)+'k P2 <Factorial.java")', "import os", number=1))
	heap_size.append(i)

print(running_time)