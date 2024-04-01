import math

name = input()
time_episode = int(input())
time_break = int(input())

time_for_lunch = time_break * 1/8
time_for_chill = time_break * 1/4
time_left_break = time_break - time_for_lunch - time_for_chill

time_left = math.ceil(abs(time_left_break - time_episode))
if time_left_break >= time_episode:
    print(f"You have enough time to watch {name} and left with {time_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {time_left} more minutes.")