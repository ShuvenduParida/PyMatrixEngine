🧮 Matrix Class — Custom Python Data Type for Matrix Operations
🚀 Overview

Matrix is a custom Python data type that behaves like a built-in numeric type — but for matrices.
It supports matrix arithmetic, scalar operations, transpose, determinant, and comparisons — all powered by Python’s magic methods (__add__, __mul__, etc.).

This class makes matrix manipulation intuitive, safe, and Pythonic.

✨ Key Features

✅ Matrix Validation:
If you give invalid data (like rows of different lengths or non-list input), the class automatically checks and raises a meaningful error — preventing you from creating broken matrices.

💬 “If you gave the values as input and you have not checked whether it will actually form a valid matrix, this datatype will do that for you — and if 
there’s an issue, it will sweetly raise an error instead of letting bugs sneak in.”

✅ Operator Overloading:
Use familiar mathematical syntax:

A + B      # Matrix addition
A - B      # Matrix subtraction
A * B      # Matrix multiplication
A * 3      # Scalar multiplication
A / 2      # Scalar division


✅ Extra Functionalities:

A.transpose() — Transpose of the matrix

A.determinant() — Determinant (for square matrices)

A.copy() — Deep copy of the matrix

abs(A), -A, A == B — Just like regular numbers

✅ User-Friendly Printing:
Beautifully formatted output when printed — looks like a real matrix!

✅ Error Handling:
Automatically detects invalid dimensions during operations (like adding a 2×2 matrix to a 3×3 one) and raises descriptive ValueErrors.

🧠 Example Usage
from matrix import Matrix   # or directly use the class if in same file

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("A =\n", A)
print("\nB =\n", B)

print("\nA + B =\n", A + B)
print("\nA * B =\n", A * B)
print("\nA * 3 =\n", A * 3)
print("\nA / 2 =\n", A / 2)
print("\nTranspose of A =\n", A.transpose())
print("\nDeterminant of A =", A.determinant())


Output:

A =
1	2
3	4

B =
5	6
7	8

A + B =
6	8
10	12

A * B =
19	22
43	50

Transpose of A =
1	3
2	4

Determinant of A = -2

⚙️ Internals — What Makes It Special
Method	Description
__init__	Constructor — validates data and ensures it’s a proper matrix
__repr__, __str__	Beautiful object representation for printing and debugging
__add__, __sub__, __mul__, __truediv__	Arithmetic operators for matrix and scalar operations
__eq__	Checks equality between two matrices
__getitem__	Allows indexing like A[0][1]
.transpose()	Returns transposed matrix
.determinant()	Calculates determinant (square matrices only)
🧩 Why This Helps Others

Working with matrices in plain Python lists is tedious and error-prone —
you constantly need to check dimensions, ensure uniform row sizes, and handle exceptions manually.

This Matrix class:

Makes your math code cleaner and safer.

Eliminates manual input validation — it’s done automatically.

Uses object-oriented design and operator overloading so your code reads like pure math.

🧡 In short: this datatype lets you focus on what you want to compute, not how to handle errors or data structure details.
