# Actual answer = 365

from statistics import mean
values_from_crowd = [1000, 1010, 1785, 2000, 1500, 100, 120, 150, 150, 170, 175, 180, 197, 200, 200, 200, 200, 200, 220, 220, 220, 220, 234, 250, 250, 250, 250, 250, 250, 250, 250, 250, 263, 270, 275, 275, 286, 300, 300, 300, 300, 300, 300, 300, 300, 300, 320, 350, 350, 400, 400, 400, 400, 400, 450, 467, 500, 500, 500, 500, 500, 500, 500, 550, 550, 600, 650, 700, 700, 720]
values_from_crowd.sort()

trimmed_value = int(0.1 * len(values_from_crowd))
values_from_crowd = values_from_crowd[trimmed_value:]
values_from_crowd = values_from_crowd[:len(values_from_crowd) - trimmed_value]

print(mean(values_from_crowd))

