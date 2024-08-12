import math

# Function to calculate the Euclidean distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# A simple function to find the distance between the closest pair of points in a small subset (brute force approach)
def brute_force(points):
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if dist(points[i], points[j]) < min_dist:
                min_dist = dist(points[i], points[j])
    return min_dist

# A utility function to find the smallest distance in the strip of points near the dividing line
def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda p: p[1])  # Sort points by their y-coordinate
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
            j += 1
    
    return min_dist

# The main function that implements the divide-and-conquer approach
def closest_pair_rec(points):
    if len(points) <= 3:
        return brute_force(points)
    
    mid = len(points) // 2  # Find the midpoint
    mid_point = points[mid]

    # Recursively find the smallest distance in the left and right halves
    dl = closest_pair_rec(points[:mid])
    dr = closest_pair_rec(points[mid:])
    
    # Find the smaller of the two distances
    d = min(dl, dr)
    
    # Build an array strip[] that contains points close to the dividing line
    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)
    
    # Find the closest points in strip. Return the minimum of d and closest distance in strip
    return min(d, strip_closest(strip, d))

# The main function that calls the recursive function and initializes necessary steps
def closest_pair(points):
    points.sort(key=lambda p: p[0])  # Sort points by x-coordinate
    return closest_pair_rec(points)

# Example usage:
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("The smallest distance is:", closest_pair(points))
