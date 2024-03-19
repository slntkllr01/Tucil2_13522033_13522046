import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import util as u

def draw_dnc_plot(canvas, list_of_points, iteration_value):
    fig_dnc = Figure(figsize=(5, 4), dpi=100)
    ax_dnc = fig_dnc.add_subplot(111)

    dnc_result = u.dnc_bezier(list_of_points, iteration_value)

    canvas_dnc = FigureCanvasTkAgg(fig_dnc, master=canvas)
    canvas_dnc_widget = canvas_dnc.get_tk_widget()
    canvas_dnc_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot(current_iteration, show_iteration):
        if current_iteration >= 0:
            ax_dnc.clear()
            temp = []
            for i in range(0, len(dnc_result), 2**current_iteration):
                temp.append(dnc_result[i])
            ax_dnc.plot([p[0] for p in temp], [p[1] for p in temp], 'go-', markersize=2.5)
            ax_dnc.set_title(f"Iterasi: {show_iteration}")
            canvas_dnc.draw()
            canvas.after(500, update_plot, current_iteration-1, show_iteration+1)
        else:
            ax_dnc.clear()
            ax_dnc.plot([p[0] for p in dnc_result], [p[1] for p in dnc_result], 'go-', markersize=2.5, label="DNC Bezier Curve")
            ax_dnc.plot([p[0] for p in list_of_points], [p[1] for p in list_of_points], 'ro--', label="Control Points")
            ax_dnc.legend()
            canvas_dnc.draw()

    update_plot(iteration_value, 0)


def draw_brute_force_plot(canvas, list_of_points, iteration_value):
    fig_bf = Figure(figsize=(5, 4), dpi=100)
    ax_bf = fig_bf.add_subplot(111)
    
    brute_force_result = u.brute_force_bezier(list_of_points, iteration_value)

    canvas_bf = FigureCanvasTkAgg(fig_bf, master=canvas)
    canvas_bf_widget = canvas_bf.get_tk_widget()
    canvas_bf_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot(current_iteration, show_iteration):
        if current_iteration >= 0:
            ax_bf.clear()
            temp = []
            for i in range(0, len(brute_force_result), 2**current_iteration):
                temp.append(brute_force_result[i])
            ax_bf.plot([p[0] for p in temp], [p[1] for p in temp], 'bo-', markersize=2.5)
            ax_bf.set_title(f"Iterasi: {show_iteration}")
            canvas_bf.draw()
            canvas.after(500, update_plot, current_iteration-1, show_iteration+1)
        else:
            ax_bf.clear()
            ax_bf.plot([p[0] for p in brute_force_result], [p[1] for p in brute_force_result], 'bo-', markersize=2.5, label="Brute Force Bezier Curve")
            ax_bf.plot([p[0] for p in list_of_points], [p[1] for p in list_of_points], 'ro--', label="Control Points")
            ax_bf.legend()
            canvas_bf.draw()

    update_plot(iteration_value, 0)

def start_pressed():
    list_of_points.clear()
    index = 0
    for point_frame in control_points_inner_frame.winfo_children():
        x_entry = point_frame.children[f'x_entry_{index}']
        y_entry = point_frame.children[f'y_entry_{index}']
        x = float(x_entry.get())
        y = float(y_entry.get())
        list_of_points.append((x, y))
        index += 1

    time_1 = time.time() * 1000
    dnc_result = u.dnc_bezier(list_of_points, iteration_value)
    dnc_time = (time.time() * 1000 - time_1)
    brute_force_result = u.brute_force_bezier(list_of_points, iteration_value)
    bf_time = (time.time() * 1000 - time_1)

    for widget in canvas_divide_conquer.winfo_children():
        widget.destroy()
    for widget in canvas_brute_force.winfo_children():
        widget.destroy()

    draw_dnc_plot(canvas_divide_conquer, list_of_points, iteration_value)

    draw_brute_force_plot(canvas_brute_force, list_of_points, iteration_value)

    time_brute_force_label.config(text=f"Brute Force Execution Time : {bf_time:.2f} ms")
    time_divide_conquer_label.config(text=f"Divide & Conquer Execution Time : {dnc_time:.2f} ms")

def update_control_points():
    num_points_entry = points_entry.get()
    if num_points_entry.strip().isdigit():
        num_points = int(num_points_entry)
        for widget in control_points_inner_frame.winfo_children():
            widget.destroy()
        for i in range(num_points):
            create_point_frame(i)

iteration_value = 0

def update_iteration_value(*args):
    global iteration_value
    iteration_input = iteration_entry.get()
    if iteration_input.isdigit() and iteration_input:
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

root = tk.Tk()
root.title("Bezier Curve Maker")

list_of_points = []

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

input_frame = tk.Frame(main_frame)
input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

points_label = tk.Label(input_frame, text="Banyak Point")
points_label.pack(pady=5)
points_entry = tk.Entry(input_frame, width=10)
points_entry.pack(pady=5)

iteration_label = tk.Label(input_frame, text="Iterasi")
iteration_label.pack(pady=5)
iteration_entry = tk.Entry(input_frame, width=10)
iteration_entry.pack(pady=5)

points_entry.bind("<KeyRelease>", lambda event: update_control_points())
iteration_entry.bind("<KeyRelease>", lambda event: update_iteration_value())

control_points_frame = tk.Frame(input_frame)
control_points_frame.pack(pady=10)

control_points_scrollbar = tk.Scrollbar(control_points_frame, orient=tk.VERTICAL)
control_points_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

control_points_canvas = tk.Canvas(control_points_frame, yscrollcommand=control_points_scrollbar.set)
control_points_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

control_points_scrollbar.config(command=control_points_canvas.yview)

control_points_inner_frame = tk.Frame(control_points_canvas)
control_points_canvas.create_window((0, 0), window=control_points_inner_frame, anchor=tk.NW)

def update_scroll_region(event=None):
    control_points_canvas.update_idletasks()
    control_points_canvas.config(scrollregion=control_points_canvas.bbox("all"))

control_points_inner_frame.bind("<Configure>", update_scroll_region)

start_button = tk.Button(input_frame, text="START", command=start_pressed)
start_button.pack(pady=10)

graph_frame = tk.Frame(main_frame, bd=2, relief=tk.SUNKEN)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

scroll_canvas = tk.Canvas(graph_frame)
scroll_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(graph_frame, command=scroll_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

scroll_canvas.configure(yscrollcommand=scrollbar.set)

scroll_frame = tk.Frame(scroll_canvas)
scroll_canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

scroll_frame.bind("<Configure>", lambda event, canvas=scroll_canvas: onFrameConfigure(canvas))

canvas_brute_force = tk.Canvas(scroll_frame, bg='white', height=150)
canvas_brute_force.pack(fill=tk.X)
time_brute_force_label = tk.Label(scroll_frame, text="Brute Force Execution Time : 0 ms")
time_brute_force_label.pack()

canvas_divide_conquer = tk.Canvas(scroll_frame, bg='white', height=150)
canvas_divide_conquer.pack(fill=tk.X)
time_divide_conquer_label = tk.Label(scroll_frame, text="Divide & Conquer Execution Time : 0 ms")
time_divide_conquer_label.pack()

status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()