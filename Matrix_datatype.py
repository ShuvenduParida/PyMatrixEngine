import copy

class Matrix:
    def __init__(self, data):
        # Validate input
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Matrix must be initialized with a list of lists.")
        if len({len(row) for row in data}) != 1:
            raise ValueError("All rows in the matrix must have the same length.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return f"Matrix({self.data})"

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __getitem__(self, idx):
        return self.data[idx]

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix dimensions must match for addition.")
            result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = [[self.data[i][j] + other for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(result)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix dimensions must match for subtraction.")
            result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = [[self.data[i][j] - other for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(result)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Invalid dimensions for matrix multiplication.")
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                       for j in range(other.cols)] for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(result)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero.")
            result = [[self.data[i][j] / other for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(result)
        else:
            return NotImplemented

    def __neg__(self):
        return Matrix([[-x for x in row] for row in self.data])

    def __abs__(self):
        return Matrix([[abs(x) for x in row] for row in self.data])

    def transpose(self):
        transposed = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed)

    def determinant(self):
        # Only for square matrices
        if self.rows != self.cols:
            raise ValueError("Determinant is only defined for square matrices.")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0]*self.data[1][1] - self.data[0][1]*self.data[1][0]
        det = 0
        for c in range(self.cols):
            minor = [[self.data[i][j] for j in range(self.cols) if j != c] for i in range(1, self.rows)]
            det += ((-1)**c) * self.data[0][c] * Matrix(minor).determinant()
        return det

    def copy(self):
        return Matrix(copy.deepcopy(self.data))
