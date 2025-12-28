def lagrange_interpolation(x_points, y_points, x):
    """
    Perform Lagrange interpolation.
    
    Parameters:
    x_points : list of known x-values
    y_points : list of known y-values
    x        : the point at which to evaluate the polynomial
    
    Returns:
    interpolated value at x
    """
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        # Compute L_i(x)
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result


# Example usage:
x_points = [0, 1, 2]
y_points = [1, 3, 2]   # f(0)=1, f(1)=3, f(2)=2

# Interpolate at x=1.5
# x_eval = 1.5
x_eval = float(input("Enter the number you want to interpolate: "))
# print("You entered:", x_eval)

y_eval = lagrange_interpolation(x_points, y_points, x_eval)

print(f"Interpolated value at x={x_eval} is {y_eval}")
