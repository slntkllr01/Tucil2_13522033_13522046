import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import util as u

def draw_dnc_plot(canvas, list_of_points, iteration_value):
    # Buat figure dan axes untuk DNC
    fig_dnc = Figure(figsize=(5, 4), dpi=100)
    ax_dnc = fig_dnc.add_subplot(111)
    
    # Gunakan fungsi dari modul utilitas untuk mendapatkan data plot DNC
    dnc_result = u.dnc_bezier(list_of_points, iteration_value)
    
    # Plot proses animasi setiap iterasi
    '''
    DI SINI EL, AKU MAU GAMBAR TEMP TIAP ITERASI
    '''
    while iteration_value >=0:
        ax_dnc.clear()
        temp = []
        for i in range(0, len(dnc_result), 2**iteration_value):
            temp.append(dnc_result[i])
        ax_dnc.plot([p[0] for p in temp], [p[1] for p in temp], 'bo-', markersize=2.5)
        FigureCanvasTkAgg(fig_dnc, master=canvas).draw()
        FigureCanvasTkAgg(fig_dnc, master=canvas).get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        time.sleep(1)
        iteration_value -= 1

    # Plot hasil DNC menggunakan matplotlib
    ax_dnc.plot([p[0] for p in dnc_result], [p[1] for p in dnc_result], 'bo-', markersize=2.5, label="DNC Bezier Curve")
    ax_dnc.plot([p[0] for p in list_of_points], [p[1] for p in list_of_points], 'ro--', label="Control Points")
    ax_dnc.legend()
    
    # Tanamkan plot DNC ke dalam Tkinter Canvas
    plot_widget_dnc = FigureCanvasTkAgg(fig_dnc, master=canvas)
    plot_widget_dnc.draw()
    plot_widget_dnc.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def draw_brute_force_plot(canvas, list_of_points, iteration_value):
    # Buat figure dan axes untuk Brute Force
    fig_bf = Figure(figsize=(5, 4), dpi=100)
    ax_bf = fig_bf.add_subplot(111)
    
    # Gunakan fungsi dari modul utilitas untuk mendapatkan data plot Brute Force
    brute_force_result = u.brute_force_bezier(list_of_points, iteration_value)

    # Plot proses animasi setiap iterasi
    '''
    DI SINI EL, AKU MAU GAMBAR TEMP TIAP ITERASI
    '''
    while iteration_value >=0:
        ax_bf.clear()
        temp = []
        for i in range(0, len(brute_force_result), 2**iteration_value):
            temp.append(brute_force_result[i])
        ax_bf.plot([p[0] for p in temp], [p[1] for p in temp], 'bo-', markersize=2.5)
        FigureCanvasTkAgg(fig_bf, master=canvas).draw()
        FigureCanvasTkAgg(fig_bf, master=canvas).get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        time.sleep(1)
        iteration_value -= 1

    # Plot hasil Brute Force menggunakan matplotlib
    ax_bf.plot([p[0] for p in brute_force_result], [p[1] for p in brute_force_result], 'bo-', markersize=2.5, label="Brute Force Bezier Curve")
    ax_bf.plot([p[0] for p in list_of_points], [p[1] for p in list_of_points], 'ro--', label="Control Points")
    ax_bf.legend()
    
    # Tanamkan plot Brute Force ke dalam Tkinter Canvas
    plot_widget_bf = FigureCanvasTkAgg(fig_bf, master=canvas)
    plot_widget_bf.draw()
    plot_widget_bf.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def start_pressed():
    print("START button pressed")
    list_of_points.clear()  # Pastikan list_of_points kosong sebelum diisi
    index = 0
    for point_frame in control_points_inner_frame.winfo_children():
        # Menggunakan nama yang diberikan saat pembuatan untuk mengakses setiap Entry
        x_entry = point_frame.children[f'x_entry_{index}']
        y_entry = point_frame.children[f'y_entry_{index}']
        x = float(x_entry.get())
        y = float(y_entry.get())
        list_of_points.append((x, y))
        index += 1
    print("List of Points:", list_of_points)
    print("Iteration Value:", iteration_value)

    # Panggil fungsi Bezier untuk Divide & Conquer dan Brute Force
    dnc_result = u.dnc_bezier(list_of_points, iteration_value)
    brute_force_result = u.brute_force_bezier(list_of_points, iteration_value)

    print(dnc_result)
    print(brute_force_result)

    # Bersihkan canvas sebelumnya jika ada
    for widget in canvas_divide_conquer.winfo_children():
        widget.destroy()
    for widget in canvas_brute_force.winfo_children():
        widget.destroy()

    # Gambar plot untuk DNC
    draw_dnc_plot(canvas_divide_conquer, list_of_points, iteration_value)

    # Gambar plot untuk Brute Force
    draw_brute_force_plot(canvas_brute_force, list_of_points, iteration_value)

def update_control_points():
    num_points_entry = points_entry.get()
    if num_points_entry.strip().isdigit():
        num_points = int(num_points_entry)
        # Menghapus semua kotak "Control Points" yang ada
        for widget in control_points_inner_frame.winfo_children():
            widget.destroy()
        # Membuat kotak "Control Points" sebanyak num_points
        for i in range(num_points):
            create_point_frame(i)

# Variabel untuk menyimpan nilai iteration
iteration_value = 0

def update_iteration_value(*args):
    global iteration_value
    iteration_input = iteration_entry.get()
    if iteration_input.isdigit() and iteration_input:  # Memeriksa apakah input bukan kosong dan merupakan digit
        iteration_value = int(iteration_input)

def create_point_frame(index):
    point_frame = tk.Frame(control_points_inner_frame)
    point_frame.pack(pady=5)

    title = tk.Label(point_frame, text=f"Point {index+1}")
    title.pack()

    x_label = tk.Label(point_frame, text="X:")
    x_label.pack(side=tk.LEFT)
    x_entry = tk.Entry(point_frame, width=5, name=f'x_entry_{index}')
    x_entry.pack(side=tk.LEFT, padx=(0, 10))

    y_label = tk.Label(point_frame, text="Y:")
    y_label.pack(side=tk.LEFT)
    y_entry = tk.Entry(point_frame, width=5, name=f'y_entry_{index}')
    y_entry.pack(side=tk.LEFT)


# Inisialisasi Tkinter
root = tk.Tk()
root.title("Bezier Curve Maker")

# List untuk menyimpan titik-titik
list_of_points = []

# Membuat frame utama
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Frame untuk input dan tombol
input_frame = tk.Frame(main_frame)
input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Jumlah poin dan iterasi
points_label = tk.Label(input_frame, text="Banyak Point")
points_label.pack(pady=5)
points_entry = tk.Entry(input_frame, width=10)
points_entry.pack(pady=5)

iteration_label = tk.Label(input_frame, text="Iterasi")
iteration_label.pack(pady=5)
iteration_entry = tk.Entry(input_frame, width=10)
iteration_entry.pack(pady=5)

# Memanggil fungsi update_control_points saat nilai pada entri "Banyak Point" berubah
points_entry.bind("<KeyRelease>", lambda event: update_control_points())
iteration_entry.bind("<KeyRelease>", lambda event: update_iteration_value())

# Frame untuk kotak-kotak "Control Points" dengan scrollbar vertikal
control_points_frame = tk.Frame(input_frame)
control_points_frame.pack(pady=10)

# Scrollbar vertikal untuk frame "Control Points"
control_points_scrollbar = tk.Scrollbar(control_points_frame, orient=tk.VERTICAL)
control_points_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvas untuk menampung kotak-kotak "Control Points"
control_points_canvas = tk.Canvas(control_points_frame, yscrollcommand=control_points_scrollbar.set)
control_points_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Menyambungkan scrollbar ke canvas "Control Points"
control_points_scrollbar.config(command=control_points_canvas.yview)

# Membuat frame untuk menempatkan widget "Control Points"
control_points_inner_frame = tk.Frame(control_points_canvas)
control_points_canvas.create_window((0, 0), window=control_points_inner_frame, anchor=tk.NW)

# Fungsi untuk mengatur ukuran canvas saat ukuran frame berubah
def update_scroll_region(event=None):
    control_points_canvas.update_idletasks()
    control_points_canvas.config(scrollregion=control_points_canvas.bbox("all"))

control_points_inner_frame.bind("<Configure>", update_scroll_region)

# Tombol start
start_button = tk.Button(input_frame, text="START", command=start_pressed)
start_button.pack(pady=10)

# Frame untuk grafik dan waktu eksekusi
graph_frame = tk.Frame(main_frame, bd=2, relief=tk.SUNKEN)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Placeholder untuk grafik brute force
canvas_brute_force = tk.Canvas(graph_frame, bg='white', height=150)
canvas_brute_force.pack(fill=tk.X)
time_brute_force_label = tk.Label(graph_frame, text="Time Brute Force: 0 ms")
time_brute_force_label.pack()

# Placeholder untuk grafik divide & conquer
canvas_divide_conquer = tk.Canvas(graph_frame, bg='white', height=150)
canvas_divide_conquer.pack(fill=tk.X)
time_divide_conquer_label = tk.Label(graph_frame, text="Time Divide & Conquer: 0 ms")
time_divide_conquer_label.pack()

# Status bar di bawah
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
