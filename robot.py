X, Y, FACE = 0, 1, 2
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
            position[X] += MOVEMENTS[position[FACE]].get('x', 0)
            position[Y] += MOVEMENTS[position[FACE]].get('y', 0)
        position[FACE] = TURNS[m].get(position[FACE], position[FACE]) if m in TURNS else position[FACE]
    return position
