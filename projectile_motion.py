import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def calculate_and_plot():
    try:
        v = float(entry_velocity.get())
        angle_input = float(entry_angle.get())
        if not (0 <= angle_input <= 90):
            raise ValueError("Angle must be between 0 and 90 degrees.")

        g = 9.8
        angles = []
        ranges = []

        # Calculate range vs angle curve for 0-90 degrees
        for angle in range(0, 91):
            theta = math.radians(angle)
            r = (v ** 2) * math.sin(2 * theta) / g
            angles.append(angle)
            ranges.append(r)

        max_range = max(ranges)
        optimal_angle = angles[ranges.index(max_range)]

        # Calculate trajectory for user input angle
        theta_input = math.radians(angle_input)
        time_of_flight = 2 * v * math.sin(theta_input) / g
        t_vals = [time_of_flight * i / 100 for i in range(101)]
        x_vals = [v * math.cos(theta_input) * t for t in t_vals]
        y_vals = [v * math.sin(theta_input) * t - 0.5 * g * t ** 2 for t in t_vals]

        # Plot range vs angle
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(angles, ranges, color='blue', linewidth=2)
        plt.title(f"Projectile Range vs Launch Angle (v={v} m/s)")
        plt.xlabel("Angle (degrees)")
        plt.ylabel("Range (meters)")
        plt.grid(True)
        plt.axvline(x=optimal_angle, color='red', linestyle='--', label=f'Max Range at {optimal_angle}°')
        plt.legend()

        # Plot trajectory for input angle
        plt.subplot(1, 2, 2)
        plt.plot(x_vals, y_vals, color='green', linewidth=2)
        plt.title(f"Trajectory at {angle_input}° and {v} m/s")
        plt.xlabel("Horizontal distance (meters)")
        plt.ylabel("Height (meters)")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        messagebox.showinfo("Results",
            f"Maximum range: {max_range:.2f} meters at {optimal_angle}°\n"
            f"Trajectory plotted for angle {angle_input}°."
        )
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

root = tk.Tk()
root.title("Projectile Motion Calculator")

tk.Label(root, text="Initial Velocity (m/s):").pack(pady=(10, 0))
entry_velocity = tk.Entry(root)
entry_velocity.pack(pady=5)

tk.Label(root, text="Launch Angle (degrees, 0-90):").pack(pady=(10, 0))
entry_angle = tk.Entry(root)
entry_angle.pack(pady=5)

btn_calc = tk.Button(root, text="Calculate & Plot", command=calculate_and_plot)
btn_calc.pack(pady=20)

root.mainloop()
