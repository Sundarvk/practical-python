# bounce.py
#
# Exercise 1.5
height = 100 # meters
bounce_height = 3/5 # bounce height
bounce = 1

while bounce <= 10:
	height = height * bounce_height
	bounce = bounce + 1
	print (bounce, round(height,4))

