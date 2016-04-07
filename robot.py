TURNS = {
    'L':{'N':'W', 'E':'N', 'S':'E', 'W':'S'},
    'R':{'N':'E', 'E':'S', 'S':'W', 'W':'N'}
}
def robot(position, movements, debug=False):
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
            position[2] = TURNS[m][position[2]]
        elif m == 'R':
            position[2] = TURNS[m][position[2]]
    return position
