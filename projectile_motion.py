import math
import matplotlib.pyplot as plt


g = 9.8  
initial_velocity = 30 


angles = []
ranges = []

# Loop through angles from 0 to 90 degrees
for angle in range(0, 91, 1):
    theta_rad = math.radians(angle)
    range_val = (initial_velocity ** 2) * math.sin(2 * theta_rad) / g
    angles.append(angle)
    ranges.append(range_val)


max_range = max(ranges)
optimal_angle = angles[ranges.index(max_range)]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(angles, ranges, color='blue', linewidth=2)
plt.title("Projectile Range vs. Launch Angle")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid(True)
plt.axvline(x=optimal_angle, color='red', linestyle='--', label=f'Max Range at {optimal_angle}°')
plt.legend()
plt.tight_layout()
plt.show()

print(f"\nThe maximum range occurs at approximately {optimal_angle} degrees.")
print(f"Maximum range: {max_range:.2f} meters")
