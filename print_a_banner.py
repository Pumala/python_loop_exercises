print "Bonus: Print a Banner"
# prompt user for text
# create a banner for the text that fits the around the text nicely

text = raw_input("Text? ")

for row_num in range(0, 3):
    length = len(text)
    row = "*" * (length + 4)
    if (row_num == 0) or (row_num == (3 - 1)):
        print row
    else:
        print "* " + text + " *"
