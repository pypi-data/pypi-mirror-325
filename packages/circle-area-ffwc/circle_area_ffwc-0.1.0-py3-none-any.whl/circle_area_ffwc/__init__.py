# circle_area/__init__.py

def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius.

    Args:
        radius: The radius of the circle (a non-negative number).

    Returns:
        The area of the circle (a float).

    Raises:
        TypeError: If the radius is not a number.
        ValueError: If the radius is negative.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number (int or float).")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    import math  # Import math inside the function to avoid unnecessary global imports.
    return math.pi * radius**2


# Example usage (optional - can be removed for the package)
if __name__ == "__main__":
    radius = 5
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is: {area}")

    try:
        calculate_circle_area(-2)  # Example of negative radius
    except ValueError as e:
        print(f"Error: {e}")

    try:
        calculate_circle_area("abc") # Example of invalid type
    except TypeError as e:
        print(f"Error: {e}")