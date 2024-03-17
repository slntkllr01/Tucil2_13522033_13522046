# Ide Algoritma El

import matplotlib.pyplot as plt
from math import comb

# Cek float valid
def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# Input titik kontrol
def input_points(num_of_points):
    li = []
    for i in range(num_of_points):
        print("\nTitik ke-" + str(i+1))
        x = input("Masukkan sumbu-X ke-"+ str(i+1) + ": ")
        y = input("Masukkan sumbu-Y ke-"+ str(i+1) + ": ")
        while (not (is_float(x) and is_float(y))):
            print("Mohon berikan koordinat dalam bentuk angka (float)")
            print("\nTitik ke-" + str(i+1))
            x = input("Masukkan sumbu-X ke-"+ str(i+1) + ": ")
            y = input("Masukkan sumbu-Y ke-"+ str(i+1) + ": ")
        li.append((float(x),float(y)))
    return li

def show_graph(list_of_points, list_of_controls):
    plt.clf()
    list_x_points = [point[0] for point in list_of_points]
    list_y_points = [point[1] for point in list_of_points]
    list_x_controls = [point[0] for point in list_of_controls]
    list_y_controls = [point[1] for point in list_of_controls]
    plt.plot(list_x_controls, list_y_controls, 'ro--', label='Control Points', markersize=2.5)
    plt.plot(list_x_points, list_y_points, 'bo-', label='Bezier Curve', markersize=2.5)
    plt.legend()
    plt.title("Bezier Curve")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

'''
ALGORITMA DIVIDE AND CONQUER
'''
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
def dnc_bezier_helper(list_of_poinst, iteration):
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
        plt.plot(list_of_poinst[0][0], list_of_poinst[0][1], marker='.', color="black", markersize=2.5)
        plt.pause(0.01)
        # Merge
        return (dnc_bezier_helper(temp[:initial_lenght], iteration) + list_of_poinst + dnc_bezier_helper(temp[initial_lenght:], iteration))
        
# Mengembalikan titik awal pada kurva bezier
def dnc_bezier(list_of_poinst, iteration):
    return [list_of_poinst[0]] + dnc_bezier_helper(list_of_poinst, iteration) + [list_of_poinst[len(list_of_poinst)-1]]

'''
ALGORITMA BRUTE FORCE
'''
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
        plt.plot(x,y, marker='.', color="black", markersize=2.5)
        plt.pause(0.01)

    return bezier_points