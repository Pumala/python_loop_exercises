print "Bonus: Factor a Number"
# Prompt user for a number and print all its factors

user_num = int(raw_input("Enter a number: "))

for num in range(1, user_num + 1):
    product = user_num / num
    if user_num == (product * num):
        print num
