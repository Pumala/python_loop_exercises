print "Multiplication Table"
# Print the multiplication table from numbers 1 - 10.

for num in range(1, 11):
    for num2 in range(1, 11):
        product = num * num2
        print str(num) + " x " + str(num2) + " =", product
