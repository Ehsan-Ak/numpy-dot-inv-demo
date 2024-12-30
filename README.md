# numpy-dot-inv-demo Benchmarking BLAS Implementations in NumPy

Calculating the time to multiply two square matrices and the inverse of a square matrix of dimensions 20,000


This project benchmarks various BLAS implementations in the NumPy library. For installing different linear algebra accelerator libraries along with NumPy, you can refer to the NumPy installation guide.

## Prerequisites

- Programming Language: Python 3.x
- Libraries: NumPy, time
- Operating System: Windows, Mac, Linux

## Installing Libraries

To install the necessary libraries, you can use the following commands:

### Intel and AMD Systems (x86)

```bash
pip install numpy

Benchmark Calculations
In this benchmark, we perform the following calculations:

Multiplication of two square matrices of equal dimensions

Inversion of a square matrix

Matrix Sizes
For both tasks, use matrices of sizes 10000 and 20000.

Using the time Library
To measure the execution time, use the time library in Python.

Test Results
I ran this test on my system, and the results are shown in the images below:

Processor: Intel i5-4300M

Memory: 16GB RAM


References
