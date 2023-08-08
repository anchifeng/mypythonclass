"""
File: class_reviews.py
Name: Feng An Chi
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO: The evaluation analysis program of the class SC001, SC101.
    """
    s = input('Which class? ')
    if s == '-1':
        print('No class scores were entered')
    else:
        i = int(input('Score: '))
        if s.upper() == 'SC001':
            max_001 = i
            min_001 = i
            total_001 = i
            times_001 = 1
            max_101 = 0
            min_101 = 200
            total_101 = 0
            times_101 = 0
        elif s.upper() == 'SC101':
            max_101 = i
            min_101 = i
            total_101 = i
            times_101 = 1
            max_001 = 0
            min_001 = 200
            total_001 = 0
            times_001 = 0
        while True:
            s = input('Which class? ')
            if s == '-1':
                break
            else:
                i = int(input('Score: '))
                if s.upper() == 'SC001':
                    if i > max_001:
                        max_001 = i
                    if i < min_001:
                        min_001 = i
                    total_001 += i
                    times_001 += 1
                elif s.upper() == 'SC101':
                    if i > max_101:
                        max_101 = i
                    if i < min_101:
                        min_101 = i
                    total_101 += i
                    times_101 += 1
        print('=============SC001=============')
        if times_001 != 0:
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(float(total_001) / times_001))
        else:
            print('No score for SC001')
        print('=============SC101=============')
        if times_101 != 0:
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(float(total_101) / times_101))
        else:
            print('No score for SC101')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
