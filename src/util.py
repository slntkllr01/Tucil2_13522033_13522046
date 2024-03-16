# Ide Algoritma El

import matplotlib.pyplot as plt
from math import comb

# Input titik kontrol
def input_points(num_of_points):
    li = []
    for i in range(num_of_points):
        x = input("Masukkan sumbu-X ke-"+ str(i+1) + ": ")
        y = input("Masukkan sumbu-Y ke-"+ str(i+1) + ": ")
        while (not (x.isnumeric and y.isnumeric())):
            print("Mohon berikan koordinat dalam bentuk angka")
            x = input("Masukkan sumbu-X ke-"+ str(i+1) + ": ")
            y = input("Masukkan sumbu-Y ke-"+ str(i+1) + ": ")
        li.append((int(x),int(y)))
    return li

# Mencari titik tengah antara dua titik
def find_middle(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Mencari titik tengah dari seluruh titik
def find_all_middle(list_of_poinst):
    li = []
    for i in range (len(list_of_poinst) - 1):
        li.append(find_middle(list_of_poinst[i], list_of_poinst[i+1]))
    return li

# Mencari titik kontrol kurva bezier
def bezier_curve_n_helper(list_of_poinst, iteration):
    if iteration == 0:
        return []
    else:
        # Divide and Conquer
        initial_lenght = len(list_of_poinst)
        temp = [list_of_poinst[0], list_of_poinst[len(list_of_poinst) - 1]]
        i = 1
        while len(list_of_poinst) != 1:
            list_of_poinst = find_all_middle(list_of_poinst)
            temp.insert(i, list_of_poinst[0])
            temp.insert(i+1, list_of_poinst[len(list_of_poinst)-1])
            i += 1
        iteration -= 1
        # Merge
        return (bezier_curve_n_helper(temp[:initial_lenght], iteration) + list_of_poinst + bezier_curve_n_helper(temp[initial_lenght:], iteration))
        
# Mengembalikan titik awal pada kurva bezier
def bezier_curve_n(list_of_poinst, iteration):
    return [list_of_poinst[0]] + bezier_curve_n_helper(list_of_poinst, iteration) + [list_of_poinst[len(list_of_poinst)-1]]
# Divide and Conquer
# def bezier_curve_n(points, iteration):
#     # COMBINE
#     if iteration == 0:
#         return points
#     else:
#         temp_points = []
#         #DIVIDE
#         for i in range(len(points) - 1):
#             midpoint_x = (points[i][0] + points[i+1][0]) / 2
#             midpoint_y = (points[i][1] + points[i+1][1]) / 2
#             temp_points.append((midpoint_x, midpoint_y))
#         # CONQUER
#         return bezier_curve_n([points[0]] + temp_points + [points[len(points) - 1]], iteration - 1)

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

def show_graph(list_of_points, list_of_controls):
    list_x_points = [point[0] for point in list_of_points]
    list_y_points = [point[1] for point in list_of_points]
    list_x_controls = [point[0] for point in list_of_controls]
    list_y_controls = [point[1] for point in list_of_controls]
    plt.plot(list_x_controls, list_y_controls, 'ro-', label='Control Points')
    plt.plot(list_x_points, list_y_points, 'bo--', label='Bezier Curve')
    plt.legend()
    plt.title("Bezier Curve")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def brute_force_bezier(points, iteration):
    pol_degree = len(points) - 1
    num_points = 2**iteration + 1

    bezier_points = []

    for i in range (num_points):
        t = i / (num_points - 1)
        x, y = 0, 0
        for j in range (len(points)):
            point = points[j]
            bin_coeff = comb(pol_degree, j)
            weight = bin_coeff * (t ** j) * ((1 - t) ** (pol_degree - j))
            x += point[0] * weight
            y += point[1] * weight
        bezier_points.append((x, y))

    return bezier_points

print(bezier_curve_n([(1,3), (3,7), (5,2), (7,8), (4,5)], 2))
print(brute_force_bezier([(1,3), (3,7), (5,2), (7,8), (4,5)], 2))
# show_graph([(1,3), (3,7), (5,2), (7,8), (4,5)], (bezier_curve_n([(1,3), (3,7), (5,2), (7,8), (4,5)], 2)))
# print(bezier_curve_three((1,3), (3,7), (5,2), 2))



