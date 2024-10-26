import numerical_methods as nm


def runge_kutta(f, x0, y0, val, h):
    while x0 < val:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + (h / 2), y0 + (k1 / 2))
        k3 = h * f(x0 + (h / 2), y0 + (k2 / 2))
        k4 = h * f(x0 + h, y0 + k3)
        k = (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        y0 += k
        y0 = round(y0, 6)
        x0 += h
        x0 = round(x0, 6)

    print("Your answer is :", y0)


def solve_using_runge_kutta_method():
    f = nm.take_func_rk()

    x0 = float(input("Enter the value of x0: "))
    y0 = float(input("Enter the value of y0: "))
    val = float(input("Enter the target value of x : "))
    h = float(input("Enter the step size h : "))

    runge_kutta(f, x0, y0, val, h)
