import math

swimming_record =  float(input())
distance_meters = float(input())
time_seconds = float(input())

total_distance_seconds = distance_meters*time_seconds
additional_seconds = math.floor(distance_meters / 15) * 12.5

total_seconds =  total_distance_seconds + additional_seconds

if total_seconds < swimming_record:
    print(f"Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_seconds - swimming_record:.2f} seconds slower.")