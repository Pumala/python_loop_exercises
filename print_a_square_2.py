print "Print a Square II"
# prompt user for a num to determine square amt
# ex: user_input = 5, 5 = 5 rows of 5 "*"

square_size = int(raw_input("How big is the square? "))
for row in range(0, square_size):
    print "*" * square_size
