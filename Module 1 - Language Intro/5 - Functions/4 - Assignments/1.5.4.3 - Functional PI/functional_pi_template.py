import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    a = 1
    b = 1 /math.sqrt(2)
    t = 0.25
    p = 1
    # change this so an actual value is returned
    while True:
        a_next = (a + b) / 2
        b_next = math.sqrt(a * b)
        t_next = t - p * (a - a_next) ** 2
        p_next = 2 * p

        pi_approximation = (a_next + b_next) ** 2 / (4 * t_next)

        if abs(pi_approximation - math.pi) < target_error:
            break

        a = a_next
        b = b_next
        t = t_next
        p = p_next
        
    return pi_approximation




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
