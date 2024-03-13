# Ide Algoritma El

import matplotlib.pyplot as plt


def find_middle(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Divide and Conquer
def bezier_curve_n(points, iteration):
    # COMBINE
    if iteration == 0:
        return points
    else:
        temp_points = []
        #DIVIDE
        for i in range(len(points) - 1):
            midpoint_x = (points[i][0] + points[i+1][0]) / 2
            midpoint_y = (points[i][1] + points[i+1][1]) / 2
            temp_points.append((midpoint_x, midpoint_y))
        # CONQUER
        return bezier_curve_n([points[0]] + temp_points + [points[len(points) - 1]], iteration - 1)

def bezier_curve_helper(Point1, Point2, Point3, iteration):
    if iteration > 0:
        # Divide and Conquer
        mid12 = find_middle(Point1, Point2)
        mid23 = find_middle(Point2, Point3)
        mid = find_middle(mid12, mid23)
        iteration -= 1
        # Merge
        return (bezier_curve_helper(Point1, mid12, mid, iteration) + [mid] + bezier_curve_helper(mid, mid23, Point3, iteration))
    else: return []

def bezier_curve_three(p1, p2, p3, n):
    return [p1] + (bezier_curve_helper(p1, p2, p3, n)) + [p3]

def show_graph(list_of_points):
    list_x = [point[0] for point in list_of_points]
    list_y = [point[1] for point in list_of_points]
    plt.plot(list_x, list_y)
    plt.show()

# print(bezier_curve_n([(1,3), (3,7), (5,2)], 2))
points = (bezier_curve_three((1,3), (3,7), (5,2), 10))