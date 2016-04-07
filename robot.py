def robot(position, movements):
    for m in movements:
        if m == 'M':
            if position[2] == 'N':
                position[1] += 1
            elif position[2] == 'S':
                position[1] -= 1
            elif position[2] == 'E':
                position[0] += 1
            elif position[2] == 'W':
                position[0] -= 1
        elif m == 'L':
            if position[2] == 'N':
                position[2] = 'W'
        elif m == 'R':
            if position[2] == 'N':
                position[2] = 'E'
            elif position[2] == 'E':
                position[2] = 'S'
            elif position[2] == 'S':
                position[2] = 'W'
            elif position[2] == 'W':
                position[2] = 'N'
    return position
