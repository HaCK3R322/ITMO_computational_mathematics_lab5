import LagrangeInterpolator
from read_values_from_file import read_file
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

from LagrangeInterpolator import LagrangeInterpolator
from NewtonInterpolator import NewtonInterpolator


def read_data():
    answer = input("How do you want to read data? (file -> f/from file \"data.txt\" -> 1/console -> c)\n>>> ")
    if answer == "f":
        file_path = input("Enter file path:\n>>> ")
        return read_file(file_path)
    elif answer == "1":
        file_path = "data.txt"
        return read_file(file_path)
    elif answer == "c":
        x_values, y_values = [], []
        n = int(input("Enter number of points:\n>>> "))
        print("Enter " + str(n) + " points if format <x> <y>:")
        for i in range(n):
            line = input("x" + str(i) + " y" + str(i) + ": ")
            x_values.append(float(line.split()[0]))
            y_values.append(float(line.split()[1]))
        return {'xarr': x_values, 'yarr': y_values}
    else:
        raise ValueError


def lab5():
    xarr, yarr = [], []
    try:
        data = read_data()
        xarr = data['xarr']
        yarr = data['yarr']
    except (ValueError, TypeError) as some_error:
        print("Wrong input type. Try again!")
        return
    except FileNotFoundError:
        print("File not found. Try again!")
        return

    print("\nGot data:")
    print(DataFrame({'x': xarr, 'y': yarr}))

    x = float(input("Enter x:\n>>> "))

    # Lagrange
    interpolated_y = LagrangeInterpolator.interpolate(xarr, yarr, x)
    print("Lagrange-interpolated y for x = " + str(x) + ":", interpolated_y)

    large_xarr = np.linspace(xarr[0], xarr[len(xarr) - 1], len(xarr) * 10)
    interpolated_yarr = LagrangeInterpolator.calculate_interpolations(xarr, yarr, large_xarr)

    plt.title("Lagrange polynom interpolation")
    plt.plot(xarr, yarr, 'bo')
    plt.plot(large_xarr, interpolated_yarr, 'r')
    plt.plot([x], [interpolated_y], 'go')
    plt.show()

    # Newton
    interpolated_y = NewtonInterpolator.interpolate(xarr, yarr, x)
    print("Newtone-interpolated y for x = " + str(x) + ":", interpolated_y)

    large_xarr = np.linspace(xarr[0], xarr[len(xarr) - 1], len(xarr) * 10)
    interpolated_yarr = NewtonInterpolator.calculate_interpolations(xarr, yarr, large_xarr)

    plt.title("Newtone polynom interpolation")
    plt.plot(xarr, yarr, 'bo')
    plt.plot(large_xarr, interpolated_yarr, 'r')
    plt.plot([x], [interpolated_y], 'go')
    plt.show()


if __name__ == '__main__':
    lab5()
