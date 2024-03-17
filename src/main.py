from util import *

print("Selamat datang di ...") # nanti kasih ascii art atau semacamnya

print("Silakan memilih algoritma\n1. Divide and Conquer\n2. Brute Force\n")
pilihan = input("Pilihan: ")
while (pilihan != "1" and pilihan != "2"):
    print()
    print("Pilihan tidak valid\nMohon pilih '1' atau '2'\n")
    print("Silakan memilih algoritma\n1. Divide and Conquer\n2. Brute Force\n")
    pilihan = input("Pilihan: ")

if (pilihan == "1"):
    print("\nPerhitungan dengan algoritma Divide and Conquer")
else: 
    print("\nPerhitungan dengan algoritma Brute Force")

flags = True
while (flags):
    n = input("Masukkan jumlah titik: ")
    if (not n.isnumeric()):
        print("Mohon masukkan angka (integer)")
    elif(int(n) < 3):
        print("Mohon masukkan angka lebih dari sama dengan 3")
    else:
        flags = False
        n = int(n)

print("\nMasukkan titik-titik kontrol")
list_control = input_points(n)

i = input("\nMasukkan jumlah iterasi: ")
while (not i.isnumeric()):
    print("Mohon masukkan angka (integer)")
    i = input("Masukkan jumlah iterasi: ")

print("\nMelakukan proses perhitungan...")
list_x_controls = [point[0] for point in list_control]
list_y_controls = [point[1] for point in list_control]
plt.plot(list_x_controls, list_y_controls, 'ro--', label='Control Points', markersize=2.5)
if (pilihan == "1"): 
    list_result = dnc_bezier(list_control, int(i))
else: # untuk brute force
    list_result = brute_force_bezier(list_control, int(i))
print("\nPerhitungan selesai\nMenampilkan grafik\n")

show_graph(list_result, list_control)
print("Terima kasih")