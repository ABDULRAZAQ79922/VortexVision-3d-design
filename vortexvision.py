import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def generate_vortex():
    center_x = float(entry_center_x.get())
    center_y = float(entry_center_y.get())
    num_points = int(entry_num_points.get())

    theta = np.linspace(0, 4*np.pi, num_points)
    radius = np.linspace(0, 1, num_points)
    x = center_x + radius * np.cos(theta)
    y = center_y + radius * np.sin(theta)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, theta, color='purple', linewidth=2)
    ax.set_title('3D Vortex', fontsize=16)
    ax.set_xlabel('X Axis', fontsize=12)
    ax.set_ylabel('Y Axis', fontsize=12)
    ax.set_zlabel('Theta', fontsize=12)
    plt.show()

root = tk.Tk()
root.title('3D Vortex Generator')

label_center_x = ttk.Label(root, text="Center X:")
label_center_x.grid(row=0, column=0, padx=5, pady=5)
entry_center_x = ttk.Entry(root)
entry_center_x.grid(row=0, column=1, padx=5, pady=5)

label_center_y = ttk.Label(root, text="Center Y:")
label_center_y.grid(row=1, column=0, padx=5, pady=5)
entry_center_y = ttk.Entry(root)
entry_center_y.grid(row=1, column=1, padx=5, pady=5)

label_num_points = ttk.Label(root, text="Number of Points:")
label_num_points.grid(row=2, column=0, padx=5, pady=5)
entry_num_points = ttk.Entry(root)
entry_num_points.grid(row=2, column=1, padx=5, pady=5)

generate_button = ttk.Button(root, text="Generate Vortex", command=generate_vortex)
generate_button.grid(row=3, columnspan=2, padx=5, pady=10)

root.mainloop()
