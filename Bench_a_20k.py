import numpy as np
import time
def time_matmul(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    start = time.time()
    C = np.dot(A, B)
    end = time.time()
    return end - start
for i in range(4):

    print(f"Time for matrices with dimensions of 5000: ",time_matmul(5000))