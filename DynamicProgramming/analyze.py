import pandas as pd
import matplotlib.pyplot as plt
from Fibonacci import lateralus

fib1 = pd.read_csv('res3.csv', header=0)
dp = pd.read_csv('res2.csv')

fib_elements = lateralus(49, return_data=True)

indices = [n for n in range(50)]
plt.plot(indices, fib1['fib'].tolist(), label="Recursive")
plt.plot(indices, dp['dp'].tolist(), label="Dynamic Programming")
plt.plot(indices, fib_elements, label="Fibonacci Sequence") # for funsies


plt.legend()
plt.xlabel('nth element of Fibonacci Sequence')
plt.ylabel('Time to compute (seconds)')
plt.title('Dynamic Programming vs Recursion')
plt.axis([0, 50, 0, max(fib1['fib'].tolist())])
plt.show()

