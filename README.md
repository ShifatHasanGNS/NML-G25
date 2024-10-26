

## Console Application Development Using Numerical Methods

> ### Numerical Methods Lab - Group 25

> KUET-**CSE '21**, **2nd**-_Year_ **2nd**-_Semester_

> - 2107067 - Md. **Shifat** Hasan
> - 2107007 - Asif **Jawad**
> - 2107113 - **Ankon** Roy

---

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

---

### 2. Solution of Non-linear Equations

> Bisection Method:

A bracketing method that divides the interval in half repeatedly until it converges to a root.

> False Position Method:

Similar to the bisection method, but instead of using the midpoint, it uses a point based on a linear interpolation between the function values.

> Secant Method:

Uses a line through two recent approximations to estimate the next point where the function is zero.

> Newton-Raphson Method:

A root-finding algorithm that uses function values and their derivatives to iteratively converge to a root.

---

### 3. Solution of Differential Equations

> Runge-Kutta Method:

A family of iterative methods used to approximate the solutions of ordinary differential equations. The 4th order Runge-Kutta method is commonly used due to its balance between accuracy and computational cost.

---

### 4. Matrix Inversion

The project includes a function for matrix inversion, which is useful for solving systems of linear equations and other applications involving linear transformations.

---

## Algorithms' Descriptions

### 1. Jacobi Iterative Method

An iterative algorithm that computes successive approximations to the solution of a system of linear equations. It assumes initial guesses for the solution and updates them iteratively based on the equations in the system.

### 2. Gauss-Seidel Iterative Method

A refinement of the Jacobi method where the update of each variable uses the latest available values from the current iteration. This leads to faster convergence in many cases compared to the Jacobi method.

### 3. Gauss Elimination

Transforms a system of linear equations into an upper triangular form using elementary row operations, after which the solution is found by back substitution.

### 4. Gauss-Jordan Elimination

An extension of Gauss elimination, where the system is reduced further to make the coefficient matrix the identity matrix. This allows for a direct read-off of the solutions.

### 5. LU Factorization

A matrix decomposition method that expresses a matrix as the product of a lower triangular matrix and an upper triangular matrix. This decomposition simplifies the process of solving systems of linear equations.

### 6. Bisection Method

A simple and robust method to find roots of a function by repeatedly halving the interval in which the root lies and selecting the subinterval that contains the root.

### 7. False Position Method

Similar to the bisection method, but instead of dividing the interval equally, it uses the function values at the endpoints to estimate the root by linear interpolation.

### 8. Secant Method

An iterative method that approximates the root of a function using a secant line through two recent approximations. It doesn't require the calculation of derivatives, unlike the Newton-Raphson method.

### 9. Newton-Raphson Method

A widely-used iterative method that approximates the root of a function by linearizing the function at an initial guess and using the derivative to refine the estimate of the root.

### 10. Runge-Kutta Method

A method used to solve ordinary differential equations by approximating the solution at discrete points using weighted averages of function values at intermediate points.

### 11. Matrix Inversion

A method to find the inverse of a square matrix, which is useful for solving systems of linear equations and other applications involving linear transformations.

---

### Recap

This project implements various numerical methods for solving linear and non-linear equations, differential equations, and matrix operations. The algorithms are implemented in Python and can be used to solve mathematical problems efficiently. The user interface prompts the user to enter the required inputs and then displays the results based on the selected method.

---
