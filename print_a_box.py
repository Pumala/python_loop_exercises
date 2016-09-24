print "Print a Box Exercise"
# print a box with different numbers representing
# height and width

width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

for row in range(0, height):
    if (row == 0) or (row == height - 1):
        print "*" * width
    else:
        print "*" + (" " * (width - 2)) + "*"
