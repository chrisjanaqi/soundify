#!/usr/bin/env python3
"""
Test for color modules
"""

import numpy as np
import matplotlib.pyplot as plt
from colors import color2number

def main():
    """
    main function here
    """
    length = 100
    colors = np.array([1/length * np.array((i, j, k))
                       for i in range(length + 1)
                       for j in range(length + 1)
                       for k in range(length + 1)])

    numbers = color2number(colors)
    plt.figure(1)
    plt.plot(np.real(numbers), np.imag(numbers))
    plt.show()

if __name__ == "__main__":
    main()
