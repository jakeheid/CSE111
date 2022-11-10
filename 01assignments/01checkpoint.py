age = int(input("What be your age? "))

max_bpm = 220
bpm = int(max_bpm - age)

low_rate = int(bpm * 0.65)
high_rate = int(bpm * 0.85)

healthy_bpm = print(f"Your heart rate should range from {low_rate} to {high_rate} when exercising.")



