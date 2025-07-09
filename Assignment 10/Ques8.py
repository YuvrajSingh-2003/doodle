# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 10:20:35 2025

@author: lenovo
"""

import matplotlib.pyplot as plt

sem1 = [75, 80, 85, 90]
sem2 = [78, 82, 88, 91]
subjects = ['Math', 'Physics', 'Chemistry', 'Biology']

plt.figure(figsize=(10, 6))

plt.plot(subjects, sem1, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8, label='Semester 1')
plt.plot(subjects, sem2, marker='s', linestyle='--', color='green', linewidth=2, markersize=8, label='Semester 2')

plt.title("Semester-wise Subject Performance", fontsize=14, pad=20)
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Marks (%)", fontsize=12)
plt.xticks(fontsize=11)

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11, shadow=True)

plt.tight_layout()
plt.margins(x=0.1)

ax = plt.gca()
ax.spines[['top', 'right']].set_visible(False)
ax.spines[['bottom', 'left']].set_color('#333333')

max_val = max(max(sem1), max(sem2))