count_pages = int(input())
pages_per_hour = int(input())
count_days = int(input())
time = count_pages//pages_per_hour
hours = time // count_days
print(hours)