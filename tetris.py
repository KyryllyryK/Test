SIZE_N = 5
SIZE_M = 5

pers_x = 0
pers_y = 0

exit_x = 4
exit_y = 4
while True:
    game_map = ""
    for j in range(SIZE_M):
        road = "|"
        for i in range(SIZE_N):
            if pers_x == i and pers_y == j:
                road += "x|"
            elif exit_x == i and exit_y == j:
                road += "o|"
            else:
                road += " |"
        game_map += f"{road}\n"
    print(game_map)
    if pers_x == exit_x and pers_y == exit_y:
        print("win")
        break
    movement = input("Enter direction( u / d / l / r ) ")
    if movement == "u" and pers_y > 0:
        pers_y -= 1
    elif movement == "d" and pers_y < 4:
        pers_y += 1
    elif movement == "l" and pers_x > 0:
        pers_x -= 1
    elif movement == "r" and pers_x < 4:
        pers_x += 1
