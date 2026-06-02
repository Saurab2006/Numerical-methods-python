"""In my trapezoidal method code, I divide the interval [a, b] into N equal subintervals. 
Then I calculate the function values at the endpoints of each subinterval. 
Each small area is treated as a trapezium. I add all trapezium areas using the formula dx/2 times the sum of endpoint values. 
Finally, I compare the approximate value with the actual integral value and calculate the absolute error."""
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
    # Draw x-axis and y-axis
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


def trapezoidal_approx(func, a, b, N):
    '''Compute the Trapezoidal Approximation of Definite Integral of a function over the interval [a,b].

    Parameters
    ----------
    func : function
           Vectorized function of one variable
    a , b : numbers
        Endpoints of the interval [a,b]
    N : integer
        Number of subintervals of equal length in the partition of [a,b]

    Returns
    -------
    float
        Approximation of the definite integral by Trapezoidal Approximation.
    '''

    dx = (b - a) / N  # Step size
    x = np.linspace(a, b, N+1)  # Equidistant partition points
    result = 0.5 * dx * np.sum(func(x[:-1]) + func(x[1:]))  # Trapezoidal Approximation of Definite Integral
    return result


if __name__ == "__main__":
    # 1st Function to be integrated
    func_1 = lambda x : x/(x**2 + 1)
    # Indefinite Integral of the function
    antiderivative_1 = lambda x : 0.5 * np.log(1 + x**2) #This defines its antiderivative, used to calculate the actual value.
    
    # 2nd Function to be integrated
    func_2 = lambda x : np.exp(x)
    # Indefinite Integral of the function
    antiderivative_2 = lambda x : np.exp(x)
    
    # End points for 1st Function
    a1 = 0; b1 = 5
    # End points for 2nd Function
    a2 = 0; b2 = 5

    # Call the function to Plot the graph of the functions
    plot_function(func_1, a1, b1)
    plot_function(func_2, a2, b2)
    
    # Different partition values
    partitions = [10, 30, 50, 100, 500]

    print("\n--- Function 1: f(x) = x/(x^2 + 1) ---")

    # Loop through all partition values for 1st function
    for N1 in partitions:

        trapezoidal_approx_1 = trapezoidal_approx(func_1, a1, b1, N1)
        definite_integral_1 = antiderivative_1(b1) - antiderivative_1(a1)
        error_1 = np.abs(trapezoidal_approx_1 - definite_integral_1)

        print("\nN =", N1)
        print("Subinterval width = {:0.6f}".format((b1-a1)/N1))
        print("Trapezoidal Approximation for 1st Function = {:0.6f}".format(trapezoidal_approx_1))
        print("Actual Value for 1st Function = {:0.6f}".format(definite_integral_1))
        print("Absolute error between the above methods = {:0.8f}".format(error_1))

    print("\n--- Function 2: f(x) = e^x ---")

    # Loop through all partition values for 2nd function
    for N2 in partitions:

        trapezoidal_approx_2 = trapezoidal_approx(func_2, a2, b2, N2)
        definite_integral_2 = antiderivative_2(b2) - antiderivative_2(a2)
        error_2 = np.abs(trapezoidal_approx_2 - definite_integral_2)

        print("\nN =", N2)
        print("Subinterval width = {:0.6f}".format((b2-a2)/N2))
        print("Trapezoidal Approximation for 2nd Function = {:0.6f}".format(trapezoidal_approx_2))
        print("Actual Value for 2nd Function = {:0.6f}".format(definite_integral_2))
        print("Absolute error between the above methods = {:0.8f}".format(error_2))
        
        """The trapezoidal method is a numerical integration method used to approximate the area under a curve. 
        It divides the area into trapeziums and adds their areas together."""