import numpy as np
import time

def time_inv(n):
    A = np.random.rand(n, n)
    start = time.time()
    inv_A = np.linalg.inv(A)
    end = time.time()
    return end - start

print(f"Time calculate inverse matrices with dimensions of 20000:",time_inv(20000))
