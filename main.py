import numerical_methods as nm

if __name__ == '__main__':
    print("\n# ----- Welcome from NML::G25 ----- #")

    try:
        while True:
            should_continue = input("\n\nDo you want to continue? (y/n): ")

            nm.clear_screen()

            if should_continue.lower() == 'n':
                print("\n\n# ----- Thank you for using NML::G25 ----- #\n")
                break

            print("\n<<---- Application Catalog ---->>")
            print('''
    1. Solution of Linear Equations
       a. Jacobi iterative method
       b. Gauss-Seidel iterative method
       c. Gauss elimination
       d. Gausss-Jordan elimination
       e. LU factorization
    2. Solution of Non-linear Equations
       a. Bi-section method
       b. False position method
       c. Secant method
       d. Newton-Raphson method
    3. Solution of Differential Equations
       a. Runge-Kutta method
    4. Matrix Inversion
                  ''')

            choice_dictionary = {
                "1a": {"title": "Solution of Linear Equations > Jacobi iterative method", "method": nm.solve_using_jacobi_method},
                "1b": {"title": "Solution of Linear Equations > Gauss-Seidel iterative method", "method": nm.solve_using_gauss_seidel_method},
                "1c": {"title": "Solution of Linear Equations > Gauss elimination", "method": nm.solve_using_gaussian_elimination_method},
                "1d": {"title": "Solution of Linear Equations > Gausss-Jordan elimination", "method": nm.solve_using_jordan_elimination_method},
                "1e": {"title": "Solution of Linear Equations > LU factorization", "method": nm.solve_using_lu_factorization_method},
                "2a": {"title": "Solution of Non-linear Equations > Bi-section method", "method": nm.solve_using_bisection_method},
                "2b": {"title": "Solution of Non-linear Equations > False position method", "method": nm.solve_using_false_position_method},
                "2c": {"title": "Solution of Non-linear Equations > Secant method", "method": nm.solve_using_secant_method},
                "2d": {"title": "Solution of Non-linear Equations > Newton-Raphson method", "method": nm.solve_using_newton_raphson_method},
                "3a": {"title": "Solution of Differential Equations > Runge-Kutta method", "method": nm.solve_using_runge_kutta_method},
                "4a": {"title": "Matrix Inversion", "method": nm.inverse_matrix},
                "4": {"title": "Matrix Inversion", "method": nm.inverse_matrix},
            }

            choice = input("Enter your choice [example: 1d]:  ")

            nm.clear_screen()

            if choice in choice_dictionary:
                print(
                    f"\n<<---- {choice_dictionary[choice]['title']} ---->>\n")
                choice_dictionary[choice]['method']()
                print()
            else:
                print("\nInvalid choice. Please try again.\n")

    except Exception as e:
        print(f"Error: {e}")
