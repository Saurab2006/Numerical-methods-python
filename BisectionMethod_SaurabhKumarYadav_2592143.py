# Root Finding Method
"""My bisection code first checks whether the selected interval has opposite signs.
Then it repeatedly calculates the midpoint of the interval.
If the midpoint gives a function value close to zero, it returns that midpoint as the root.
Otherwise, it keeps the half interval where the sign change occurs.
This process continues until the required tolerance is reached or the maximum iteration limit is exceeded."""
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    x = np.linspace(a, b, 500) #Creates 500 equally spaced values between a and b.
    y = func(x)
    plt.figure()
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='k', linewidth=0.8) #Draws horizontal line:
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')
    plt.legend() #creates the name
    plt.grid(True) # horizontal and vertical guide lines in the graph background
    plt.show()


def bisection_method(func, a, b, tol=1e-6, max_iter=100):#required accuracy; Tolerance means the allowed small error in the answer.
    """
    Bisection method to find the root of a function within a given interval.

    Parameters:
    - func: The function for which the root is to be found.
    - a, b: Interval [a, b] within which the root is searched for.
    - tol: Tolerance level for checking convergence of the method.
    - max_iter: Maximum number of iterations.

    Returns:
    - root: Approximation of the root.
    
    Example
    --------
    >>> fun = lambda x: x**2 - x - 1
    >>> root = bisection_method(fun, 1, 2, max_iter=20)
    """

    # Check if the interval is valid (signs of f(a) and f(b) are different)
    if func(a) * func(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs. Choose a different interval.")

    # Main loop starts here
    iter_count = 1
    root = (a + b) / 2
    while iter_count <= max_iter:
        c = (a + b) / 2 #This calculates the midpoint of the current interval.
        root = c
        if abs(func(c)) <= 1e-10 or (b - a) <= tol: 
            return root, iter_count
        iter_count += 1
        if np.sign(func(c)) == np.sign(func(a)):
            a = c
        else:
            b = c

    print("Warning! Exceeded the maximum number of iterations.")
    return root, max_iter


# Example usage:
if __name__ == "__main__": #This ensures code runs only when file is executed directly.

    # FUNCTION 1:  f(x) = x^2 - x - 1
    func = lambda x: x**2 - x - 1  # First Function

    # Call plot_function to plot graph of the function
    plot_function(func, -2, 3)

    # Set the interval [a, b] for the search
    a_1 = 1;  b_1 = 2;   # For first root
    a_2 = -1; b_2 = 0;   # For second root

    # Call the bisection method
    our_root_1, iter_1 = bisection_method(func, a_1, b_1)
    our_root_2, iter_2 = bisection_method(func, a_2, b_2)

    # Call SciPy method root, which we consider as a reference method.
    x0 = (a_1 + b_1) / 2
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()

    x0 = (a_2 + b_2) / 2
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()

    # Print the result
    print("\n--- Function 1: f(x) = x^2 - x - 1 ---")
    print("1st root: interval = [{}, {}], iterations = {}, Bisection Method = {:0.8f}.".format(a_1, b_1, iter_1, our_root_1))
    print("1st root found by SciPy = {:0.8f}".format(sp_root_1))

    print("2nd root: interval = [{}, {}], iterations = {}, Bisection Method = {:0.8f}.".format(a_2, b_2, iter_2, our_root_2))
    print("2nd root found by SciPy = {:0.8f}".format(sp_root_2))


    # FUNCTION 2:  f(x) = x^3 - x^2 - 2x + 1
  
    func = lambda x: x**3 - x**2 - 2*x + 1  # Second Function

    # Call plot_function to plot graph of the function
    plot_function(func, -2, 3)

    # Set the interval [a, b] for the three roots
    a_1 = -2; b_1 = -1;  # For first root
    a_2 =  0; b_2 =  1;  # For second root
    a_3 =  1; b_3 =  2;  # For third root

    # Call the bisection method
    our_root_1, iter_1 = bisection_method(func, a_1, b_1)
    our_root_2, iter_2 = bisection_method(func, a_2, b_2)
    our_root_3, iter_3 = bisection_method(func, a_3, b_3)

    # Call SciPy method root, which we consider as a reference method.
    x0 = (a_1 + b_1) / 2
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()

    x0 = (a_2 + b_2) / 2
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()

    x0 = (a_3 + b_3) / 2
    sp_result_3 = sp.optimize.root(func, x0)
    sp_root_3 = sp_result_3.x.item()

    # Print the result
    print("\n--- Function 2: f(x) = x^3 - x^2 - 2x + 1 ---")
    print("1st root: interval = [{}, {}], iterations = {}, Bisection Method = {:0.8f}.".format(a_1, b_1, iter_1, our_root_1))
    print("1st root found by SciPy = {:0.8f}".format(sp_root_1))

    print("2nd root: interval = [{}, {}], iterations = {}, Bisection Method = {:0.8f}.".format(a_2, b_2, iter_2, our_root_2))
    print("2nd root found by SciPy = {:0.8f}".format(sp_root_2))

    print("3rd root: interval = [{}, {}], iterations = {}, Bisection Method = {:0.8f}.".format(a_3, b_3, iter_3, our_root_3))
    print("3rd root found by SciPy = {:0.8f}".format(sp_root_3))
