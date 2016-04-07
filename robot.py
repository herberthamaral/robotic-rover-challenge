TURNS = {
    'L':{'N':'W', 'E':'N', 'S':'E', 'W':'S'},
    'R':{'N':'E', 'E':'S', 'S':'W', 'W':'N'}
}
MOVEMENTS = {
    'N': {'y':1}, 'S':{'y': -1}, 'E': {'x':1}, 'W':{'x':-1}
}
def robot(position, movements, debug=False):
    for m in movements:
        if m == 'M':
            position[0] += MOVEMENTS[position[2]].get('x', 0)
            position[1] += MOVEMENTS[position[2]].get('y', 0)
        elif m == 'L':
            position[2] = TURNS[m][position[2]]
        elif m == 'R':
            position[2] = TURNS[m][position[2]]
    return position
