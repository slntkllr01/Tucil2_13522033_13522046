from util import *

print("Selamat datang di ...") # nanti kasih ascii art atau semacamnya
x = "y"
while (x == "y"):
    print("Silakan memilih algoritma\n1. Divide and Conquer\n2. Brute Force (hanya untuk 3 titik kontrol)\n")
    pilihan = input("Pilihan: ")
    while (pilihan != "1" or pilihan != "2"):
        print()
        print("Pilihan tidak valid\nMohon pilih '1' atau '2'\n")
        print("Silakan memilih algoritma\n1. Divide and Conquer\n2. Brute Force (hanya untuk 3 titik kontrol)\n")
        pilihan = input("Pilihan: ")

    if (pilihan == "1"):
        print("Perhitungan dengan algoritma Divide and Conquer")
        n = input("Masukkan jumlah titik: ")
        while (not n.isnumeric()):
            print("Mohon masukkan angka")
            n = input("Masukkan jumlah titik: ")
        n = int(n)
    else: 
        print("Perhitungan dengan algoritma Brute Force")
        n = 3

    print("Masukkan titik-titik kontrol")
    list_control = input_points(n)

    i = input("Masukkan jumlah iterasi: ")
    while (not i.isnumeric()):
        print("Mohon masukkan berupa integer")
        i = input("Masukkan jumlah iterasi: ")

    print("\nMelakukan proses perhitungan...")
    if (pilihan == "1"):
        list_result = bezier_curve_n(list_control, int(i))
    # else: # untuk brute force
    print("\nPerhitungan selesai\n")

    show_graph(list_result, list_control)
        
    


    
