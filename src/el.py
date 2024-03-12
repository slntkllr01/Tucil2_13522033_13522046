# Ide Algoritma El

# Divide and Conquer
def bezier_curve(points, iteration):
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
        return bezier_curve([points[0]] + temp_points + [points[len(points) - 1]], iteration - 1)

print(bezier_curve([(1,3), (3,7), (5,2)], 1))
