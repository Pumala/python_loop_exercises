print "Print a Triangle II Exercise"
# print a triangle made up of "*" characters
# prompt user for height of the triangle

height = int(raw_input("Height: "))

gap = height - 1
star = 1

for num in range(0, height):
    new_gap = " " * gap
    print new_gap + ("*" * star) + new_gap
    star += 2
    gap -= 1
