# Monte Carlo Integration with Visualization

This Python project utilizes the Monte Carlo method to approximate the definite integral of a given function within specified limits. The Monte Carlo method is a statistical technique that uses random sampling to obtain numerical results.

## Overview

The primary goal of this project is to estimate the definite integral of a user-defined function over a specified range using the Monte Carlo integration method. The integration is visualized by generating random points and determining the ratio of points below the function curve to the total number of points, providing an approximation of the integral.

## Project Structure

The project consists of a single Python script (`montecarlo.py`) containing the following key components:

### 1. `find_points` Function

This function generates random points within specified x and y limits and categorizes them as either above or below the function curve.

### 2. `monte_carlo` Function

The main Monte Carlo integration function that calls `find_points` to generate points and calculates the approximate integral using the ratio of points below the function.

### 3. `main` Function

The main function initializes the parameters such as function, x and y limits, and the number of points. It then iterates over different numbers of points, calculates the Monte Carlo integration, and visualizes the results for each iteration.

## Usage

To use this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd monte_carlo_integration
   ```

3. Run the script:

   ```bash
   python montecarlo.py
   ```

   Adjust the parameters in the script, such as the function definition and the range of x and y values, to suit your specific integration needs.

## Dependencies

This project relies on the following Python libraries:

- `matplotlib`: Used for plotting the function curve and scattered points.
- `numpy`: Essential for numerical operations and generating random points.

Ensure these dependencies are installed before running the script:

```bash
pip install matplotlib numpy
```

## Results

The script generates visualizations for different numbers of points, providing insights into the convergence of the Monte Carlo integration as the number of points increases.

Feel free to modify the script to integrate your own functions and explore the behavior of the Monte Carlo method for different mathematical expressions.

**Note:** This README assumes that the user has a basic understanding of Monte Carlo integration and numerical methods. Further adjustments and optimizations can be made based on specific requirements and use cases.
