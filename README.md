## Console Application Development Using Numerical Methods

> ### Numerical Methods Lab - Group 25

> KUET-**CSE '21**, **2nd**-_Year_ **2nd**-_Semester_

> - 2107067 - Md. **Shifat** Hasan
> - 2107007 - Asif **Jawad**
> - 2107 113 - **Ankon** Roy

#

**To clone this Repository:**

```bash
git clone https://github.com/ShifatHasanGNS/NML-G25.git
```

---

**Objectives of this Academic Project:**

> - Implement solutions for various numerical methods for solving linear and non-linear equations, differential equations, and matrix operations.

> - Develop a console application that allows users to interact with the implemented algorithms.

> - Provide a user-friendly interface for entering inputs and displaying results.

> - Encourage collaborative development and understanding of numerical methods.

---

## Application Structure

**The application is divided into following sections:**

### 1. Solution of Linear Equations

> Jacobi Iterative Method:

An iterative technique where each equation in a linear system is solved for the corresponding variable, using the previous iteration's values for the other variables.

> Gauss-Seidel Iterative Method:

A modification of the Jacobi method where the most recent values of the variables are used as soon as they are available.

> Gauss Elimination:

A direct method that reduces a system of linear equations to upper triangular form and then solves it by back substitution.

> Jordan or Gauss-Jordan Elimination:

An extension of Gauss elimination that transforms the coefficient matrix into the identity matrix, solving the system directly.

> LU Factorization:

Decomposes the coefficient matrix into a lower triangular matrix (L) and an upper triangular matrix (U), then solves the system by forward and backward substitution.

#

### 2. Solution of Non-linear Equations

> Bisection Method:

A bracketing method that divides the interval in half repeatedly until it converges to a root.

> False Position Method :

Similar to the bisection method, but instead of using the midpoint, it uses a point based on a linear interpolation between the function values.

> Secant Method:

Uses a line through two recent approximations to estimate the next point where the function is zero.

> Newton-Raphson Method:

A root-finding algorithm that uses function values and their derivatives to iteratively converge to a root.

#

### 3. Solution of Differential Equations

> Runge-Kutta Method:

A family of iterative methods used to approximate the solutions of ordinary differential equations. The 4th order Runge-Kutta method is commonly used due to its balance between accuracy and computational cost.

#

### 4. Matrix Inversion

The project includes a function for matrix inversion, which is useful for solving systems of linear equations and other applications involving linear transformations.

---

# Algorithms' Descriptions

### 1. Jacobi Iterative Method

An iterative algorithm that computes successive approximations to the solution of a system of linear equations. It assumes initial guesses for the solution and updates them iteratively based on the equations in the system.

> pseudocode

```
function Jacobi(A, b, x0, max_iterations, tolerance):
    n = length(b)
    x = x0

    for k = 1 to max_iterations do:
        x_new = new array of size n

        for i = 1 to n do:
            sum = 0
            for j = 1 to n do:
                if j != i then:
                    sum = sum + A[i][j] * x[j]
            x_new[i] = (b[i] - sum) / A[i][i]

        // Check for convergence
        if ||x_new - x|| < tolerance then:
            return x_new

        x = x_new

    return x
```

#

### 2. Gauss-Seidel Iterative Method

A refinement of the Jacobi method where the update of each variable uses the latest available values from the current iteration. This leads to faster convergence in many cases compared to the Jacobi method.

> pseudocode

```
function GaussSeidel(A, b, x0, maxIterations, tolerance):
    n = length(b)
    x = x0

    for k from 1 to maxIterations:
        x_old = x

        for i from 1 to n:
            sum1 = 0
            sum2 = 0

            for j from 1 to i-1:
                sum1 = sum1 + A[i][j] * x[j]

            for j from i+1 to n:
                sum2 = sum2 + A[i][j] * x_old[j]

            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        if ||x - x_old|| < tolerance:
            break

    return x
```

#

### 3. Gauss Elimination

Transforms a system of linear equations into an upper triangular form using elementary row operations, after which the solution is found by back substitution.

> pseudocode

```
function GaussElimination(augmented_matrix):
    n = number of rows in augmented_matrix

    for k from 0 to n-1:
        // Pivoting
        for i from k+1 to n-1:
            factor = augmented_matrix[i][k] / augmented_matrix[k][k]
            for j from k to n:
                augmented_matrix[i][j] = augmented_matrix[i][j] - factor * augmented_matrix[k][j]

    // Back substitution
    solution = array of zeros with size n
    for i from n-1 down to 0:
        sum = 0
        for j from i+1 to n-1:
            sum = sum + augmented_matrix[i][j] * solution[j]
        solution[i] = (augmented_matrix[i][n] - sum) / augmented_matrix[i][i]

    return solution
```

#

### 4. Gauss-Jordan Elimination

An extension of Gauss elimination, where the system is reduced further to make the coefficient matrix the identity matrix. This allows for a direct read-off of the solutions.

> pseudocode

```
function GaussJordanElimination(A):
    n = number of rows in A
    m = number of columns in A

    for i from 0 to n-1:
        // Make A[i][i] equal to 1
        pivot = A[i][i]
        for j from 0 to m-1:
            A[i][j] = A[i][j] / pivot

        // Make all other entries in column i equal to 0
        for k from 0 to n-1:
            if k ≠ i:
                factor = A[k][i]
                for j from 0 to m-1:
                    A[k][j] = A[k][j] - factor * A[i][j]

    return A
```

#

### 5. LU Factorization

A matrix decomposition method that expresses a matrix as the product of a lower triangular matrix and an upper triangular matrix. This decomposition simplifies the process of solving systems of linear equations.

> pseudocode

```
function LU_Factorization(A):
    n = number of rows in A
    L = identity matrix of size n
    U = copy of A

    for k from 1 to n-1:
        for i from k to n-1:
            factor = U[i][k-1] / U[k-1][k-1]
            L[i][k-1] = factor
            for j from k-1 to n-1:
                U[i][j] = U[i][j] - factor * U[k-1][j]

    return L, U
```

#

### 6. Bisection Method

A simple and robust method to find roots of a function by repeatedly halving the interval in which the root lies and selecting the subinterval that contains the root.

> pseudocode

```
function BisectionMethod(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return "No root found in the interval [a, b]"

    while (b - a) / 2 > tol:
        c = (a + b) / 2           # Midpoint
        if f(c) == 0:
            return c              # c is a root
        else if f(a) * f(c) < 0:
            b = c                 # Root lies in [a, c]
        else:
            a = c                 # Root lies in [c, b]

    return (a + b) / 2            # Approximate root
```

#

### 7. False Position Method

Similar to the bisection method, but instead of dividing the interval equally, it uses the function values at the endpoints to estimate the root by linear interpolation.

> pseudocode

```
function false_position(f, a, b, tolerance, max_iterations)
    if f(a) * f(b) >= 0
        return "No root in the interval"

    for i from 1 to max_iterations
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))  // Calculate the false position

        if abs(f(c)) < tolerance
            return c  // Found the root

        if f(c) * f(a) < 0
            b = c  // Root is in the left subinterval
        else
            a = c  // Root is in the right subinterval

    return "Max iterations reached, root is approximately " + c
```

#

### 8. Secant Method

An iterative method that approximates the root of a function using a secant line through two recent approximations. It doesn't require the calculation of derivatives, unlike the Newton-Raphson method.

> pseudocode

```
function secantMethod(f, x0, x1, tol, maxIter):
    iter = 0
    while iter < maxIter:
        if abs(f(x1)) < tol:
            return x1
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iter += 1
    return "No convergence"
```

#

### 9. Newton-Raphson Method

A widely-used iterative method that approximates the root of a function by linearizing the function at an initial guess and using the derivative to refine the estimate of the root.

> pseudocode

```
function NewtonRaphson(f, df, x0, tol, max_iter)
    x = x0
    for i from 1 to max_iter do
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol then
            return x_new
        end if
        x = x_new
    end for
    return x // or indicate failure
end function
```

#

### 10. Runge-Kutta Method

A method used to solve ordinary differential equations by approximating the solution at discrete points using weighted averages of function values at intermediate points.

> pseudocode

```
function RungeKutta(f, y0, t0, t_end, h)
    n = (t_end - t0) / h
    y = y0
    t = t0

    for i from 1 to n do
        k1 = f(t, y)
        k2 = f(t + h/2, y + k1/2)
        k3 = f(t + h/2, y + k2/2)
        k4 = f(t + h, y + k3)
        y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h

    return y
```

#

### 11. Matrix Inversion

A method to find the inverse of a square matrix, which is useful for solving systems of linear equations and other applications involving linear transformations.

> pseudocode

```
function matrixInversion(A):
    n = number of rows in A
    Create augmented matrix [A | I] where I is the identity matrix

    for i from 0 to n - 1:
        if A[i][i] == 0:
            Swap rows i and k (where A[k][i] != 0)
        Scale row i by 1 / A[i][i]

        for j from 0 to n - 1:
            if j != i:
                Subtract A[j][i] * row i from row j

    return right half of augmented matrix
```

---

### Recap

This project implements various numerical methods for solving linear and non-linear equations, differential equations, and matrix operations. The algorithms are implemented in Python and can be used to solve mathematical problems efficiently. The user interface prompts the user to enter the required inputs and then displays the results based on the selected method.

#
