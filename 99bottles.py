# 99 Bottles
# Author: John Kelly


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

bottleSong()