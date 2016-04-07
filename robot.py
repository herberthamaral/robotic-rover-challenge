# encoding: utf-8
from __future__ import print_function
X, Y, FACE = 0, 1, 2
TURNS = {
    'L':{'N':'W', 'E':'N', 'S':'E', 'W':'S'},
    'R':{'N':'E', 'E':'S', 'S':'W', 'W':'N'}
}
MOVEMENTS = {
    'N': {'y':1}, 'S':{'y': -1}, 'E': {'x':1}, 'W':{'x':-1}
}
def robot(position, movements):
    for m in movements:
        if m == 'M':
            position[X] += MOVEMENTS[position[FACE]].get('x', 0)
            position[Y] += MOVEMENTS[position[FACE]].get('y', 0)
        position[FACE] = TURNS[m].get(position[FACE], position[FACE]) if m in TURNS else position[FACE]
    return position

def main():
    board = raw_input() #descartado, não é relevante para o problema
    robots = []
    positions = []
    movements = []
    while True:
        position = list(raw_input().replace(' ',''))
        if not position:
            break
        movements = raw_input().replace(' ','')
        position[0] = int(position[0])
        position[1] = int(position[1])
        robots.append(dict(position=position, movements=movements))
    for r in robots:
        final_position = robot(**r)
        print('{} {} {}'.format(*final_position))

if __name__ == '__main__':
    main()
