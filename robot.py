def robot(position, movements):
    for m in movements:
        if m == 'M':
            if position[2] == 'N':
                position[1] += 1
        if m == 'L':
            if position[2] == 'N':
                position[2] = 'W'
    return position
