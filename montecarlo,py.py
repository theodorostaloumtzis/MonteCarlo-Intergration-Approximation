import matplotlib.pyplot as plt
import numpy as np


# Function to find points
def find_points(N, function, x_lims, y_lims):
    points_above = np.zeros((N, 2))
    points_below = np.zeros((N, 2))
    for i in range(N):
        x = np.random.uniform(x_lims[0], x_lims[1])
        y = np.random.uniform(y_lims[0], y_lims[1])
        fx = function(x)
        if y < fx:
            points_below[i, 0] = x
            points_below[i, 1] = y
        else:
            points_above[i, 0] = x
            points_above[i, 1] = y
    return points_above, points_below


# Monte Carlo method
def monte_carlo(N, function, x_lims, y_lims):
    above, below = find_points(N, function, x_lims, y_lims)
    area = (x_lims[1] - x_lims[0]) * (y_lims[1] - y_lims[0])
    l = below[below[:, 0] != 0, :2]
    print(len(l))
    val = len(l) / N * area
    return val, above, below


def main():
    # Seed for reproducibility
    # set the number of the seed if you want
    # np.random.seed(42)

    # Function and limits
    x_lims = [-1.0, 1.0]
    y_lims = [0.0, 4.0]

    # Function
    # you can change the function to any function you want
    function = lambda x: np.cos(2 * x) + 3 * np.sin(4 * x) ** 2

    # Number of points
    N = [100, 1_000, 10_000, 100_000, 1_000_000]
    montecarlo_data = []
    above_data_x = []
    above_data_y = []
    below_data_x = []
    below_data_y = []
    error_data = []
    error_percent_data = []
    integration_data = []

    for n in N:
        montecarlo, above, below = monte_carlo(n, function, x_lims, y_lims)
        integration = np.trapz(function(np.linspace(x_lims[0], x_lims[1], 10000)),
                               np.linspace(x_lims[0], x_lims[1], 10000))
        error = abs(integration - montecarlo)
        error_percent = error / integration * 100
        montecarlo_data.append(montecarlo)
        temp1 = above[(above[:, 0] != 0) & (above[:, 1] != 0)]
        temp2 = below[(below[:, 0] != 0) & (below[:, 1] != 0)]
        above_data_x.append(temp1[:, 0])
        above_data_y.append(temp1[:, 1])
        below_data_x.append(temp2[:, 0])
        below_data_y.append(temp2[:, 1])
        error_data.append(error)
        error_percent_data.append(error_percent)
        integration_data.append(integration)

    x_vals = np.linspace(x_lims[0], x_lims[1], 10000)
    # Plotting
    plt.figure(1)
    plt.subplot(111)
    plt.plot(x_vals, function(x_vals), label='f(x)')
    plt.scatter(above_data_x[0], above_data_y[0], color='red', marker='o', label='Points Above')
    plt.scatter(below_data_x[0], below_data_y[0], color='blue', marker='o', label='Points Below')
    plt.xlim(x_lims)
    plt.ylim(y_lims)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(
        f" N={N[0]},MC_val={montecarlo_data[0]:.4f}, I={integration_data[0]:.4f} Error={error_data[0]:.4f}, Error %={error_percent_data[0]:.4f}")
    plt.legend()

    plt.figure(2)
    plt.subplot(111)
    plt.plot(x_vals, function(x_vals), label='f(x)')
    plt.scatter(above_data_x[1], above_data_y[1], color='red', marker='o', label='Points Above')
    plt.scatter(below_data_x[1], below_data_y[1], color='blue', marker='o', label='Points Below')
    plt.xlim(x_lims)
    plt.ylim(y_lims)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(
        f" N={N[1]},MC_val={montecarlo_data[1]:.4f}, I={integration_data[1]:.4f} Error={error_data[1]:.4f}, Error %={error_percent_data[1]:.4f}")
    plt.legend()

    plt.figure(3)
    plt.subplot(111)
    plt.plot(x_vals, function(x_vals), label='f(x)')
    plt.scatter(above_data_x[2], above_data_y[2], color='red', marker='o', label='Points Above')
    plt.scatter(below_data_x[2], below_data_y[2], color='blue', marker='o', label='Points Below')
    plt.xlim(x_lims)
    plt.ylim(y_lims)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(
        f" N={N[2]},MC_val={montecarlo_data[2]:.4f}, I={integration_data[2]:.4f} Error={error_data[2]:.4f}, Error %={error_percent_data[2]:.4f}")
    plt.legend()

    plt.figure(4)
    plt.subplot(111)
    plt.plot(x_vals, function(x_vals), label='f(x)')
    plt.scatter(above_data_x[3], above_data_y[3], color='red', marker='o', label='Points Above')
    plt.scatter(below_data_x[3], below_data_y[3], color='blue', marker='o', label='Points Below')
    plt.xlim(x_lims)
    plt.ylim(y_lims)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(
        f" N={N[3]},MC_val={montecarlo_data[3]:.4f}, I={integration_data[3]:.4f} Error={error_data[3]:.4f}, Error %={error_percent_data[3]:.4f}")
    plt.legend()

    plt.figure(5)
    plt.subplot(111)
    plt.plot(x_vals, function(x_vals), label='f(x)')
    plt.scatter(above_data_x[4], above_data_y[4], color='red', marker='o', label='Points Above')
    plt.scatter(below_data_x[4], below_data_y[4], color='blue', marker='o', label='Points Below')
    plt.xlim(x_lims)
    plt.ylim(y_lims)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(
        f" N={N[4]},MC_val={montecarlo_data[4]:.4f}, I={integration_data[4]:.4f} Error={error_data[4]:.4f}, Error %={error_percent_data[4]:.4f}")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
