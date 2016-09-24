print "Print a Triangle Exercise"
# print a specific triangle made up of "*" characters

extra = "*"
width = 7
space = width - 1
new_space = space / 2
height = 4
count = 0

while count < height:
    print (new_space * " ") + extra + (new_space * " ")
    extra += ("*" * 2)
    new_space -= 1
    count += 1
