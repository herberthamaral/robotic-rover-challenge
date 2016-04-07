def robot(position, movements):
    for m in movements:
        if m == 'M':
            if position[2] == 'N':
                position[1] += 1
    return position
