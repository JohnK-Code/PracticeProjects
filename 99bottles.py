# 99 Bottles
# Author: John Kelly


# Function used to print 99 Bottles song
# Range 99 to -1 by subtracting 1 on each loop
# Conditional statement that runs below indented code if condition met
# The %s placeholder adds the string value of i to the print statement
def bottleSong():
    for i in range(99, -1, -1):
        if i > 2:
            print('%s bottles of beer on the wall, %s bottles of beer.' % (i, i))
            print('Take one down and pass it around,',i-1,' bottles of beer on the wall.')
        elif i == 2:
            print('%s bottles of beer on the wall, %s bottles of beer.' % (i, i))
            print('Take one down and pass it around,', i - 1, ' bottle of beer on the wall.')
        elif i == 1:
            print('%s bottle of beer on the wall, %s bottle of beer.' % (i, i))
            print('Take one down and pass it around, no more bottles of beer on the wall.')
        else:
            print('No more bottles of beer on the wall, no more bottles of beer.')
            i = 99
            print('Go to the store and buy some more, %s bottles of beer on the wall.' % i)


bottleSong()  # Calls the bottlesong function
