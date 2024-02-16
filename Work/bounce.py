# bounce.py
#
# Exercise 1.5
# Height for 10 bounces

height = 100 # in meters
num_bounce = 1

while num_bounce <= 10:
    height = height * 3 / 5
    print(f"Bounce # {num_bounce}, Height: {round(height, 4)}m")
    num_bounce += 1
    
