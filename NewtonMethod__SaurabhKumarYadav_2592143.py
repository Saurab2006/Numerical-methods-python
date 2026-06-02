# Root Finding Method
#In my Newton method code, I first pass the function, its derivative, and an initial guess.
#The code checks whether the derivative is close to zero to avoid division error. 
#Then it applies the Newton formula x1 = x0 - f(x0)/f'(x0). The new value x1 becomes the next guess. 
#This process repeats until f(x0) is close to zero or the maximum iteration limit is reached.
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    x = np.linspace(a, b, 500)
    y = func(x)
    plt.figure()
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='k', linewidth=0.8)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def newton_method(func, grad, x0, tol=1e-6, max_iter=100):
    '''Approximate solution of f(x)=0 by Newton-Raphson's method.

        Parameters
        ----------
        func : function 
            Function value for which we are searching for a solution f(x)=0,
        grad: function ;  grad = derivative of the function
            Gradient value of function f(x)
        x0 : number
            Initial guess for a solution f(x)=0.
        tol : number
            Stopping criteria is abs(f(x)) < tol.
        max_iter : integer
            Maximum number of iterations of Newton's method.

        Returns
        -------
        xn : root

        Example
        --------
        >>> fun = lambda x: x**2 - x - 1
        >>> grad = lambda x: 2*x - 1
        >>> root = newton_method(fun, grad, 1, max_iter=20)
        '''
    # Main Loop starts here
    iter_count = 1
    root = x0
    while iter_count <= max_iter:
        if abs(grad(x0)) <= 1e-12:
            print("Mathematical Error! Found root may not be correct.")
            return x0, iter_count
        x1 = x0 - func(x0) / grad(x0) #new guess = old guess - function value / derivative value
        x0 = x1
        root = x0
        if abs(func(x0)) <= tol:
            return root, iter_count
        iter_count += 1

    print("Warning! Exceeded the maximum number of iterations.")
    return root, max_iter


# Main Driver Function:
if __name__ == "__main__":

    # FUNCTION 1:  f(x) = x^2 - x - 1
   
    func = lambda x: x**2 - x - 1
    grad = lambda x: 2*x - 1

    # Call plot_function to plot graph of the function
    plot_function(func, -2, 3)

    x0 = 1.5  # Initial guess for 1st root
    # Call the Newton's method for 1st root
    our_root_1, iter_1 = newton_method(func, grad, x0)

    # Call SciPy method (reference method) for 1st root
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()

    # Call the Newton's method for 2nd root
    x0 = -0.5  # Initial guess for 2nd root
    our_root_2, iter_2 = newton_method(func, grad, x0)

    # Call SciPy method (reference method) for 2nd root
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()

    # Print the result
    print("\n--- Function 1: f(x) = x^2 - x - 1 ---")
    print("1st root: initial guess x0 = 1.5, iterations = {}, Newton's Method = {:0.8f}.".format(iter_1, our_root_1))
    print("1st root found by SciPy = {:0.8f}".format(sp_root_1))

    print("2nd root: initial guess x0 = -0.5, iterations = {}, Newton's Method = {:0.8f}.".format(iter_2, our_root_2))
    print("2nd root found by SciPy = {:0.8f}".format(sp_root_2))


    # FUNCTION 2:  f(x) = x^3 - x^2 - 2x + 1

    func = lambda x: x**3 - x**2 - 2*x + 1
    grad = lambda x: 3*x**2 - 2*x - 2

    # Call plot_function to plot graph of the function
    plot_function(func, -2, 3)

    x0 = -1.5  # Initial guess for 1st root
    # Call the Newton's method for 1st root
    our_root_1, iter_1 = newton_method(func, grad, x0)

    # Call SciPy method (reference method) for 1st root
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()

    x0 = 0.5  # Initial guess for 2nd root
    # Call the Newton's method for 2nd root
    our_root_2, iter_2 = newton_method(func, grad, x0)

    # Call SciPy method (reference method) for 2nd root
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()

    x0 = 1.5  # Initial guess for 3rd root
    # Call the Newton's method for 3rd root
    our_root_3, iter_3 = newton_method(func, grad, x0)

    # Call SciPy method (reference method) for 3rd root
    sp_result_3 = sp.optimize.root(func, x0)
    sp_root_3 = sp_result_3.x.item()

    # Print the result
    print("\n--- Function 2: f(x) = x^3 - x^2 - 2x + 1 ---")
    print("1st root: initial guess x0 = -1.5, iterations = {}, Newton's Method = {:0.8f}.".format(iter_1, our_root_1))
    print("1st root found by SciPy = {:0.8f}".format(sp_root_1))

    print("2nd root: initial guess x0 = 0.5, iterations = {}, Newton's Method = {:0.8f}.".format(iter_2, our_root_2))
    print("2nd root found by SciPy = {:0.8f}".format(sp_root_2))

    print("3rd root: initial guess x0 = 1.5, iterations = {}, Newton's Method = {:0.8f}.".format(iter_3, our_root_3))
    print("3rd root found by SciPy = {:0.8f}".format(sp_root_3))
