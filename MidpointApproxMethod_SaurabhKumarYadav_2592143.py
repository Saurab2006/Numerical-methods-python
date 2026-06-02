"""In my midpoint method code, I first divide the interval [a, b] into N equal subintervals.
 Then I calculate the midpoint of each subinterval using a + (i + 0.5) * dx.
   After that, I find the function value at each midpoint and add them together. 
   Finally, I multiply the total by dx to get the approximate integral.
     I compare this approximation with the actual value using the antiderivative and calculate the absolute error."""
import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    x = np.linspace(a, b, 400)
    y = func(x)

    plt.figure()
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.8) #This draws the horizontal x-axis line where y = 0.
    plt.axvline(0, color='black', linewidth=0.8) #This draws the vertical y-axis line where x = 0.
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


def midpoint_approx(func, a, b, N):
    '''Compute the Midpoint Approximation of Definite Integral of a function over the interval [a,b].'''
    '''func = function to integrate
    a = lower limit
    b = upper limit
    N = number of subintervals'''
    dx = (b - a) / N
    total = 0

    for i in range(N):
        midpoint = a + (i + 0.5) * dx
        total += func(midpoint) #This calculates the function value at the midpoint and adds it to total.

    result = dx * total #This calculates the final midpoint approximation.
    return result


if __name__ == "__main__": #This means the following code will run only when the file is executed directly.
    # 1st Function to be integrated
    func_1 = lambda x : x/(x**2 + 1)
    antiderivative_1 = lambda x: 0.5 * np.log(1 + x**2) #This defines the exact antiderivative of function 1.
    #It is used to calculate the actual value of the integral for comparison.

    # 2nd Function to be integrated
    func_2 = lambda x : np.exp(x)
    antiderivative_2 = lambda x: np.exp(x)
    
    # End points
    a1 = 0; b1 = 5  
    a2 = 0; b2 = 5  

    plot_function(func_1, a1, b1)
    plot_function(func_2, a2, b2)

    # partitions list 
    partitions = [10, 30, 50, 100, 500]

    #FUNCTION 1
    print("\n--- Function 1 ---")

    for N1 in partitions:

        a = a1
        b = b1

        midpoint_approx_1 = midpoint_approx(func_1, a, b, N1)
        definite_integral_1 = antiderivative_1(b) - antiderivative_1(a)
        error_1 = np.abs(midpoint_approx_1 - definite_integral_1) #This calculates the absolute error.

        print("\nN =", N1)
        print("Subinterval width = {:0.6f}".format((b-a)/N1))
        print("Midpoint Approximation = {:0.6f}".format(midpoint_approx_1))
        print("Actual Value = {:0.6f}".format(definite_integral_1))
        print("Absolute error = {:0.8f}".format(error_1))

    # FUNCTION 2 
    print("\n--- Function 2 ---")

    for N2 in partitions:

        a = a2
        b = b2

        midpoint_approx_2 = midpoint_approx(func_2, a, b, N2)
        definite_integral_2 = antiderivative_2(b) - antiderivative_2(a)
        error_2 = np.abs(midpoint_approx_2 - definite_integral_2)

        print("\nN =", N2)
        print("Subinterval width = {:0.6f}".format((b-a)/N2))
        print("Midpoint Approximation = {:0.6f}".format(midpoint_approx_2))
        print("Actual Value = {:0.6f}".format(definite_integral_2))
        print("Absolute error = {:0.8f}".format(error_2)) #True value - Approximate value