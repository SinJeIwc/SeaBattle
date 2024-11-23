import random
import os
import time

def clear_all():
    os.system('clear')

def print_field(your_field):
    print('  1 2 3 4 5 6 7')
    left = 'ABCDEFG'
    for i in range(7):
        print(left[i], end=' ')
        for j in range(7):
            print(your_field[i][j], end=' ')
        print()

def check_on(field_your, x, y, your_direction, your_length, ships_xy):
    for i in range(your_length):
        xi = x + (i if your_direction == "horizontally" else 0)
        yi = y + (i if your_direction == "vertically" else 0)
        if xi > 6 or yi > 6:
            return False
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                if 0 <= xi + j < 7 and 0 <= yi + k < 7:
                    if field_your[yi + k][xi + j] == 'x':
                        return False
        # ships_xy.append([xi, yi])

    for i in range(your_length):
        xi = x + (i if your_direction == "horizontally" else 0)
        yi = y + (i if your_direction == "vertically" else 0)
        ships_xy.append([xi, yi])
    return True

def on_field(your_field):
    ships = [3, 2, 2, 1, 1, 1, 1]
    for length in ships:
        while True:
            x = random.randint(0, 6)
            y = random.randint(0, 6)
            direction = random.choice(['horizontally', 'vertically'])
            if check_on(your_field, x, y, direction, length, ships_xy):
                for j in ships_xy:
                    your_field[j[1]][j[0]] = 'x'
                break

def game(your_field):
    counts = [1 for _ in range(11)]
    counts_of_user = 0
    name = input('Write your name: ')
    already = []
    while True:
        # h = [3, 2, 2, 1, 1, 1, 1]
        print_field(field_for_game)

        cmd = input('Write your coordinates (like E1 or g2): ')
        if len(cmd) == 2 and (x := cmd[0].upper()) in "ABCDEFG" and (y := cmd[1]) in "1234567":
            check_y = 'ABCDEFG'.index(x)
            check_x = int(y) - 1
            if [check_x, check_y] in already:
                clear_all()
                print('This point has already been attached, try again!')
                time.sleep(2)

                continue
            coordinates = your_field[check_y][check_x]
            counts_of_user += 1
            already.append([check_x, check_y])

        else:
            clear_all()
            print('Your coordinates should be like E1 or g2 and in A-G, 1-7 ranges, try again')
            time.sleep(3)
            continue

        if coordinates == 'x':
            your_field[check_y][check_x] = 'H'
            for i in range(len(ships_xy)):
                if ships_xy[i] == [check_x, check_y]:
                    counts[i] = 0

        elif coordinates == '.':
            your_field[check_y][check_x] = 'M'

        field_for_game[check_y][check_x] = field[check_y][check_x]

        if sum(counts[:3]) == 0:
            for i in ships_xy[:3]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[:3] = [2, 2, 2]
        elif sum(counts[3:5]) == 0:
            for i in ships_xy[3:5]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[3:5] = [2, 2]
        elif sum(counts[5:7]) == 0:
            for i in ships_xy[5:7]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[5:7] = [2, 2]
        elif counts[7] == 0:
            for i in ships_xy[7:8]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[7] = 2
        elif counts[8] == 0:
            for i in ships_xy[8:9]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[8] = 2
        elif counts[9] == 0:
            for i in ships_xy[9:10]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[9] = 2
        elif counts[10] == 0:
            for i in ships_xy[10:11]:
                field_for_game[i[1]][i[0]] = 'S'
            counts[10] = 2

        if sum(counts) == 22:
            print('WON')
            time.sleep(2)
            break

        clear_all()
    names[name] = counts_of_user
    print('Your score: ', names[name])


def do_you():
    while True:
        b = input('Do you want continue (yes or no): ')
        if b == 'yes':
            return False
        elif b == 'no':
            return True
        else:
            print('Write yes or no!')
            time.sleep(2)

while True:
    print('''Hello! Remember:
    Hit - H
    Sunk - S
    Miss - M''')
    names = {}
    ships_xy = []
    field = [['.' for _ in range(7)] for _ in range(7)]
    field_for_game = [['.' for _ in range(7)] for _ in range(7)]
    on_field(field)
    print(ships_xy)
    game(field)
    if do_you():
        clear_all()
        names = sorted(names.items(), key=lambda item: item[1], reverse=True)
        for i in names:
            print(i[0], i[1])
        break
clear_all()
print('THANKS!')